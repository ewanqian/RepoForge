<!-- VIRTURA定位开始 自动生成请勿手动修改 -->
# 仓库锻造 自动化运维工具 RepoForge
> 生态角色：公开治理工具壳
> 核心定位：面向创意从业者的 GitHub 多仓库治理与自动化开源工具，用于多项目管理、标准化迭代与自动化运维
> 官方文档：https://ewanqian.github.io/RepoForge
<!-- VIRTURA定位结束 -->

# RepoForge

> 仓库锻造 - 面向创意从业者的公开治理工具壳

---

## 📌 重要声明

**这是一个展示用的开源项目。**

所有实际的个人配置、私有任务管理、个人判断逻辑和自动化操作，主要在私有仓库 **Forge** 中进行。

RepoForge 的作用不是暴露私有系统，而是把以下内容以公开方式整理出来：

- GitHub 多仓库治理思路
- 标准化迭代方法
- 自动化运维脚本
- skills-based governance 的公开说明
- 可供参考的公开结构与示例

- 📖 想了解项目故事？请看 [docs/PROJECT_STORY.md](docs/PROJECT_STORY.md)

---

## 这是什么

RepoForge 是一个 **Public Tool Shell**。

它主要面向以下场景：

- 管理多个 GitHub 仓库
- 标准化 README、标签、描述与基础元信息
- 整理公开可复用的 repo 管理逻辑
- 解释如何用 skills 的方式组织仓库治理与协作

它不是个人私有主脑，也不是实际生产环境中的全部系统。

---

## 四层结构

当前整个系统建议按四层理解：

### 1. `VIRTURA-SpacePort`
**Skill Source Layer**

- 公共技能母本层
- 团队理论与方法母本
- 可共享的 source skills

### 2. `Forge`
**Personal Installed Layer**

- 私有记忆
- 个人判断方式
- persona skills
- personal ops skills
- 个人主系统

### 3. `workforge`
**Work Execution Layer**

- 工作技能
- 项目推进
- 客户沟通
- 交付与复盘
- 日常执行

### 4. `RepoForge`
**Public Tool Shell**

- 对外解释治理方式
- 公开脚本与文档
- 展示 repo 管理逻辑
- 展示 skills-based governance 的公开模型

---

## 什么是 skills

这里说的 skills，不是零散 prompt，也不是一次性的聊天模板。

skills 的目标，是把高频动作和关键判断压缩成可调用的单元。  
一个合格的 skill 至少应包含：

- Purpose
- Best For
- Not For
- Inputs
- Source of Truth
- Output Format
- Failure Modes
- Escalation

这样做的原因是：

- 减少 agent 漂移
- 降低协作者理解成本
- 让弱模型也能做稳定动作
- 让 repo 治理不再完全依赖单人记忆

---

## RepoForge 的作用边界

RepoForge 适合公开：

- skill 模型
- repo 治理方法
- 公共示例
- 自动化脚本
- 仓库标准化结构

RepoForge 不负责公开：

- 私有记忆
- 私有 persona skills
- 个人长期判断系统
- 私有任务与工作细节
- 私有 RAG 配置

---

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

---

## 项目结构

```
RepoForge/
├── config/                   # 配置文件
│   ├── projects.example.yaml # 项目配置示例
│   └── secrets.example.yaml  # Secrets 配置示例
├── scripts/                  # 公开脚本
│   ├── auto_manage_repos.py  # 仓库自动管理主脚本
│   ├── scan_ecosystem.py     # 多仓库扫描脚本（示例）
│   └── deep_scan.py          # 深度扫描脚本（示例）
├── docs/                     # 文档
│   ├── PROJECT_STORY.md
│   ├── SKILLS_OVERVIEW.md
│   ├── FORGE_VS_WORKFORGE_VS_REPOFORGE.md
│   └── PUBLIC_SKILL_MODEL.md
├── examples/                 # 公开示例
├── README.md
├── LICENSE
└── .gitignore
```

---

## 功能特性

- 📦 **批量管理仓库** - 统一管理多个 GitHub 仓库
- 🏷️ **标准化标签** - 为仓库设置统一标签
- 📝 **统一描述** - 自动更新仓库描述和 README 头部
- 🔄 **自动同步** - 同步本地工作区和 GitHub 仓库
- 🧭 **公开治理说明** - 用文档解释多仓库治理与协作结构
- 🧩 **Skills 模型展示** - 展示如何把高频动作压缩成稳定 skill
- 🛡️ **安全配置** - 敏感信息不进入公开仓库

---

## 当前建议阅读顺序

如果你第一次进入 RepoForge，建议按下面顺序看：

1. [README.md](README.md)
2. docs/[SKILLS_OVERVIEW.md](SKILLS_OVERVIEW.md)
3. docs/[FORGE_VS_WORKFORGE_VS_REPOFORGE.md](FORGE_VS_WORKFORGE_VS_REPOFORGE.md)
4. docs/[PUBLIC_SKILL_MODEL.md](PUBLIC_SKILL_MODEL.md)
5. docs/[PROJECT_STORY.md](PROJECT_STORY.md)

---

## 当前状态

RepoForge 当前不是为了变成一个"全都能做"的重系统，而是先把以下事情讲清楚：

- repo 如何被治理
- 什么应该公开，什么留在私有层
- skills 如何进入 repo management
- 多仓库结构如何避免失控

---

## 许可证

MIT
