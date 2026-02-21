#!/usr/bin/env python3
import os
import yaml
from github import Github

def load_config():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    config_path = os.path.join(script_dir, "../config/projects.yaml")
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    
    secrets_path = os.path.join(script_dir, "../config/secrets.yaml")
    with open(secrets_path, "r", encoding="utf-8") as f:
        secrets = yaml.safe_load(f)
    
    return config, secrets

def deep_scan():
    config, secrets = load_config()
    g = Github(secrets["github_token"])
    user = g.get_user()
    
    print("=" * 100)
    print("🔍 Ewan Qian GitHub 仓库深度扫描")
    print("=" * 100)
    
    # 获取配置中的仓库列表
    configured_repos = {p["repo_name"]: p for p in config["projects"]}
    
    print(f"\n📊 配置文件中定义的仓库数量: {len(configured_repos)}")
    print(f"📊 GitHub 上实际的公开仓库数量: {user.public_repos}")
    
    # 获取所有GitHub仓库
    all_github_repos = list(user.get_repos())
    
    print("\n" + "=" * 100)
    print("📦 所有 GitHub 仓库详情")
    print("=" * 100)
    
    missing_repos = []
    existing_repos_in_config = []
    
    for repo in all_github_repos:
        if repo.owner.login != "ewanqian":
            continue
            
        print(f"\n{'=' * 100}")
        print(f"📁 仓库名: {repo.name}")
        print(f"{'=' * 100}")
        print(f"  描述: {repo.description or '无'}")
        print(f"  语言: {repo.language or '未知'}")
        print(f"  Star: {repo.stargazers_count}")
        print(f"  Fork: {repo.forks_count}")
        print(f"  创建时间: {repo.created_at}")
        print(f"  更新时间: {repo.updated_at}")
        print(f"  主页: {repo.homepage or '无'}")
        print(f"  私有: {repo.private}")
        
        # 检查是否在配置中
        if repo.name in configured_repos:
            print(f"  ✅ 状态: 已在 projects.yaml 中配置")
            existing_repos_in_config.append(repo.name)
        else:
            print(f"  ⚠️  状态: 未在 projects.yaml 中配置")
            missing_repos.append({
                "name": repo.name,
                "description": repo.description or "",
                "language": repo.language,
                "created_at": repo.created_at,
                "updated_at": repo.updated_at,
                "homepage": repo.homepage or "",
                "private": repo.private
            })
    
    print("\n" + "=" * 100)
    print("📋 扫描总结")
    print("=" * 100)
    
    print(f"\n✅ 已配置的仓库数: {len(existing_repos_in_config)}")
    print(f"⚠️  未配置的仓库数: {len(missing_repos)}")
    
    if missing_repos:
        print(f"\n🔍 未配置的仓库列表:")
        for repo in missing_repos:
            privacy = "🔒私有" if repo["private"] else "🌐公开"
            print(f"  - {repo['name']} [{privacy}]")
            print(f"    {repo['description'][:80] if repo['description'] else '无描述'}...")
    
    # 检查配置中有但GitHub上没有的仓库
    print("\n" + "=" * 100)
    print("🔍 配置中有但GitHub上可能不存在的仓库")
    print("=" * 100)
    
    github_repo_names = {r.name for r in all_github_repos if r.owner.login == "ewanqian"}
    config_only = []
    
    for repo_name in configured_repos.keys():
        if repo_name not in github_repo_names:
            config_only.append(repo_name)
    
    if config_only:
        for repo_name in config_only:
            print(f"  ⚠️  {repo_name}")
    else:
        print("  ✅ 所有配置的仓库在GitHub上都存在")
    
    print("\n" + "=" * 100)
    print("扫描完成！")
    print("=" * 100)
    
    return missing_repos

if __name__ == "__main__":
    deep_scan()
