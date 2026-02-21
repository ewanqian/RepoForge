<!-- VIRTURA定位开始 自动生成请勿手动修改 -->
# 仓库锻造 自动化运维工具 RepoForge
&gt; 生态角色：生态自动化技术中台
&gt; 核心定位：面向创意从业者的GitHub全项目自动化管理开源工具，为多项目管理、标准化迭代、自动化运维提供完整的解决方案
&gt; 官方文档：https://ewanqian.github.io/RepoForge
<!-- VIRTURA定位结束 -->

# RepoForge

&gt; 仓库锻造 - 简单高效的 GitHub 项目管理工具

## ⚠️ 重要提示

**此仓库包含作者个人的配置和内容**，仅供参考学习使用。如果你想使用 RepoForge 管理你自己的项目，请按照下面的"快速开始"步骤进行配置，不要直接 fork 后使用作者的个人配置。

## 快速开始

### 1. 复制示例配置文件

```bash
# 复制示例 secrets 配置
cp config/secrets.example.yaml config/secrets.yaml

# 复制示例项目配置
cp config/projects.example.yaml config/projects.yaml
```

### 2. 配置你的信息

编辑 `config/secrets.yaml`，填入你的真实信息：

```yaml
github_token: "ghp_你的github_token"
github_username: "你的用户名"
local_workspace_root: "/path/to/你的工作区"
```

编辑 `config/projects.yaml`，配置你自己的项目列表。

### 3. 管理仓库

```bash
# 预览操作（不执行实际修改）
python3 scripts/auto_manage_repos.py --preview

# 执行实际操作
python3 scripts/auto_manage_repos.py --run
```

## 项目结构

```
RepoForge/
├── config/                  # 配置文件
│   ├── projects.example.yaml # 项目配置示例（使用请复制为 projects.yaml）
│   └── secrets.example.yaml  # Secrets 配置示例（使用请复制为 secrets.yaml）
├── scripts/                 # 脚本
│   ├── auto_manage_repos.py # 仓库自动管理主脚本
│   ├── scan_ecosystem.py    # 生态系统扫描脚本（示例）
│   └── deep_scan.py         # 深度扫描脚本（示例）
├── README.md
├── LICENSE
└── .gitignore
```

**注意**：以下目录/文件不会被提交到 Git（已在 .gitignore 中）：
- `config/secrets.yaml` - 你的敏感信息
- `config/projects.yaml` - 你的个人项目配置
- `backup/` - 备份目录
- `tasks/` - 任务目录
- `logs/` - 日志目录
- 其他个人内容

## 功能特性

- 📦 **批量管理仓库** - 统一管理多个 GitHub 仓库
- 🏷️ **标准化标签** - 为所有仓库设置统一的标签
- 📝 **统一描述** - 自动更新仓库描述和 README 头部
- 🔄 **自动同步** - 同步本地工作区和 GitHub 仓库
- 🛡️ **安全配置** - 敏感信息不会被提交到 Git

## 许可证

MIT
