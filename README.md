<!-- VIRTURA定位开始 自动生成请勿手动修改 -->
# 仓库锻造 自动化运维工具 RepoForge
&gt; 生态角色：生态自动化技术中台
&gt; 核心定位：面向创意从业者的GitHub全项目自动化管理开源工具，为多项目管理、标准化迭代、自动化运维提供完整的解决方案
&gt; 官方文档：https://ewanqian.github.io/RepoForge
&lt;!-- VIRTURA定位结束 --&gt;

# RepoForge

&gt; 仓库锻造 - 简单高效的 GitHub 项目管理工具

## 快速开始

### 1. 配置 Token

创建 `~/.repoforge/secrets.yaml` 文件：

```yaml
github_token: "ghp_你的token"
github_username: "ewanqian"
local_workspace_root: "/path/to/你的工作区"
```

### 2. 管理仓库

```bash
# 预览操作（不执行实际修改）
python3 scripts/auto_manage_repos.py --preview

# 执行实际操作
python3 scripts/auto_manage_repos.py --run
```

### 3. 与云端机器人协作

- **任务**: 放在 `tasks/pending/` 目录，用 Markdown 写清楚
- **日志**: 操作记录放在 `logs/` 目录
- **交接**: 查看 `handover/README.md` 了解协作流程

## 项目结构

```
RepoForge/
├── config/              # 配置文件
│   ├── projects.yaml    # 所有项目信息
│   └── secrets.example.yaml
├── scripts/             # 脚本
│   └── auto_manage_repos.py
├── tasks/               # 任务
│   ├── pending/         # 待处理
│   └── completed/       # 已完成
├── logs/                # 操作日志
├── handover/            # 工作交接文档
├── backup/              # 备份目录
├── README.md
├── LICENSE
└── .gitignore
```

## 许可证

MIT
