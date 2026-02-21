import os
import yaml
import shutil
from datetime import datetime
from github import Github
import argparse
import re
# 读取配置
def load_config():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 读取项目配置
    config_path = os.path.join(script_dir, "../config/projects.yaml")
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    
    # 读取 secrets - 支持多个位置（按优先级）
    secrets_paths = [
        os.path.join(script_dir, "../config/secrets.yaml"),  # 项目内
        os.path.expanduser("~/.repoforge/secrets.yaml"),      # 用户主目录
        os.path.expanduser("~/.config/repoforge/secrets.yaml"),  # XDG 标准位置
    ]
    
    secrets = None
    for path in secrets_paths:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                secrets = yaml.safe_load(f)
            print(f"✅ 已加载 secrets: {path}")
            break
    
    if secrets is None:
        raise FileNotFoundError(
            "找不到 secrets.yaml 配置文件。请创建以下任一位置的文件:\n"
            "  1. ~/.repoforge/secrets.yaml (推荐)\n"
            "  2. ~/.config/repoforge/secrets.yaml\n"
            "  3. ../config/secrets.yaml (项目内，不推荐)\n"
            "\n文件格式:\n"
            "  github_token: \"your_token_here\"\n"
            "  github_username: \"your_username\"\n"
            "  local_workspace_root: \"/path/to/workspace\""
        )
    
    return config, secrets
# 初始化GitHub
def init_github(secrets):
    return Github(secrets["github_token"])
# 备份现有仓库
def backup_repos(config, secrets, preview=False):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    backup_dir = os.path.join(script_dir, f"../backup/{datetime.now().strftime('%Y%m%d_%H%M%S')}")
    if not preview:
        os.makedirs(backup_dir, exist_ok=True)
    print(f"=== 备份环节（备份到：{backup_dir}）===")
    for project in config["projects"]:
        local_readme_path = os.path.join(secrets["local_workspace_root"], project["folder_name"], "README.md")
        if os.path.exists(local_readme_path):
            print(f"✅ 备份项目：{project['name']} 的README")
            if not preview:
                shutil.copy(local_readme_path, os.path.join(backup_dir, f"{project['repo_name']}_README.md"))
    print("备份完成\n")
    return backup_dir
# 更新现有仓库信息
def update_existing_repos(config, secrets, g, preview=False):
    print("=== 更新现有仓库信息环节 ===")
    for project in config["projects"]:
        try:
            repo = g.get_repo(f"{secrets['github_username']}/{project['repo_name']}")
            print(f"处理项目：{project['name']}")
            # 打印更新前后对比
            old_desc = repo.description
            new_desc = f"{project['name']}：{project['description']}"
            old_tags = repo.get_topics()
            new_tags = project["tags"]
            print(f"  原描述：{old_desc}")
            print(f"  新描述：{new_desc}")
            print(f"  原标签：{old_tags}")
            print(f"  新标签：{new_tags}")
            # 更新本地README头部
            local_readme_path = os.path.join(secrets["local_workspace_root"], project["folder_name"], "README.md")
            if os.path.exists(local_readme_path):
                with open(local_readme_path, "r", encoding="utf-8") as f:
                    content = f.read()
                # 替换定位块，没有的话自动加在最前面
                new_header = f"""<!-- VIRTURA定位开始 自动生成请勿手动修改 -->
# {project['name']} {project['english_name']}
> 生态角色：{project['role']}
> 核心定位：{project['description']}
> 官方文档：{project['homepage']}
<!-- VIRTURA定位结束 -->
"""
                if "<!-- VIRTURA定位开始" in content:
                    new_content = re.sub(r"<!-- VIRTURA定位开始.*?<!-- VIRTURA定位结束 -->", new_header, content, flags=re.DOTALL)
                else:
                    new_content = new_header + "\n" + content
                print(f"  ✅ 已更新README头部")
                if not preview:
                    # 更新本地文件
                    with open(local_readme_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    # 同步到GitHub
                    repo.update_file("README.md", "chore: 标准化定位信息", new_content, repo.get_contents("README.md").sha)
            # 更新GitHub仓库信息
            if not preview:
                repo.edit(
                    description=new_desc,
                    homepage=project["homepage"]
                )
                # 单独更新 topics
                repo.replace_topics(new_tags)
            print(f"  ✅ 已更新仓库信息\n")
        except Exception as e:
            if "404" in str(e):
                print(f"ℹ️  项目 {project['name']} 尚未创建，跳过更新\n")
            else:
                print(f"❌ 项目 {project['name']} 更新失败：{str(e)}\n")
# 创建空白仓库
def create_new_repos(config, secrets, g, preview=False):
    print("=== 创建空白仓库环节 ===")
    # 预写死的标准化模板
    readme_template = """<!-- VIRTURA定位开始 自动生成请勿手动修改 -->
# {name} {english_name}
> 生态角色：{role}
> 核心定位：{description}
> 官方文档：{homepage}
<!-- VIRTURA定位结束 -->
## 项目介绍
本项目为VIRTURA纬图太空港生态体系的组成部分，所有规则遵循生态统一规范。
## 快速开始
待补充
## 开源协议
MIT
"""
    gitignore_template = """# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.env
secrets.yaml
# Node
node_modules/
# Blender
*.blend1
*.blend2
# 3D资产
*.fbx
*.obj
*.glb
!/examples/*.glb
# OS
.DS_Store
Thumbs.db
"""
    license_template = """MIT License
Copyright (c) 2024 VIRTURA Spaceport
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
    for project in config["projects"]:
        try:
            repo = g.get_repo(f"{secrets['github_username']}/{project['repo_name']}")
            print(f"ℹ️  项目 {project['name']} 已存在，跳过创建\n")
        except Exception as e:
            if "404" in str(e):
                print(f"创建项目：{project['name']}")
                print(f"  仓库名：{project['repo_name']}")
                print(f"  描述：{project['description']}")
                print(f"  标签：{project['tags']}")
                if not preview:
                    # 创建远程仓库
                    repo = g.get_user().create_repo(
                        name=project["repo_name"],
                        description=f"{project['name']}：{project['description']}",
                        homepage=project["homepage"],
                        private=False,
                        has_issues=True,
                        has_wiki=False,
                        has_downloads=True,
                        auto_init=True
                    )
                    # 设置标签
                    repo.replace_topics(project["tags"])
                    # 上传标准化文件
                    readme_content = readme_template.format(**project)
                    repo.update_file("README.md", "chore: 初始化标准化仓库", readme_content, repo.get_contents("README.md").sha)
                    repo.create_file(".gitignore", "chore: 添加标准化.gitignore", gitignore_template)
                    repo.create_file("LICENSE", "chore: 添加MIT协议", license_template)
                    # 克隆到本地工作区
                    local_repo_path = os.path.join(secrets["local_workspace_root"], project["folder_name"])
                    workspace_path = secrets["local_workspace_root"]
                    # 使用 subprocess 替代 os.system 以处理路径中的空格
                    import subprocess
                    try:
                        subprocess.run(
                            ["git", "clone", repo.clone_url],
                            cwd=workspace_path,
                            check=True,
                            capture_output=True
                        )
                        print(f"  ✅ 已克隆到本地")
                    except subprocess.CalledProcessError as e:
                        print(f"  ⚠️  克隆失败: {e}")
                print(f"  ✅ 创建完成\n")
            else:
                print(f"❌ 项目 {project['name']} 创建失败：{str(e)}\n")
# 归档冗余仓库
def archive_repos(config, secrets, g, preview=False):
    print("=== 归档冗余仓库环节 ===")
    for repo_name in config["archive_repos"]:
        try:
            repo = g.get_repo(f"{secrets['github_username']}/{repo_name}")
            print(f"归档仓库：{repo_name}")
            if not preview:
                repo.edit(archived=True)
            print(f"  ✅ 归档完成\n")
        except Exception as e:
            print(f"❌ 仓库 {repo_name} 归档失败：{str(e)}\n")
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='RepoForge 仓库自动化管理工具')
    parser.add_argument('--preview', action='store_true', help='仅预览操作，不执行实际修改')
    parser.add_argument('--run', action='store_true', help='执行实际操作')
    args = parser.parse_args()
    if not args.preview and not args.run:
        print("请指定 --preview 预览或 --run 执行")
        exit()
    config, secrets = load_config()
    g = init_github(secrets)
    # 按顺序执行
    backup_repos(config, secrets, preview=args.preview)
    update_existing_repos(config, secrets, g, preview=args.preview)
    create_new_repos(config, secrets, g, preview=args.preview)
    archive_repos(config, secrets, g, preview=args.preview)
    print("=== 全部操作完成 ===")