# RepoForge 项目说明：来源、使用与开发者后日谈

## 📌 重要声明

**RepoForge 现在是一个展示用的开源项目！**

所有实际的个人配置、任务管理和自动化操作都已经迁移到私有仓库 **Forge** 中。

---

## 🎯 仓库分工

| 仓库 | 可见性 | 用途 |
|------|--------|------|
| **RepoForge** | 公开 | 展示用 - 包含开源代码、示例配置、说明文档 |
| **Forge** | 私有 | 实际使用 - 包含个人配置、任务、敏感信息 |

---

## 💡 灵感来源

RepoForge 的想法来自于一个创意从业者的痛点：

### 问题场景
作为一名现场演出与沉浸视觉制作人，我同时维护着 20+ 个 GitHub 仓库：
- 技术中台项目（SceneForge、LiveForge、EHNA...）
- 艺术实践项目（少媒体艺术、混沌媒体艺术...）
- 趣味项目（MAGI系统、众生之门...）
- 个人作品集...

每次要更新仓库描述、添加标签、统一 README 格式时，都要一个一个手动改，非常耗时。

### 灵光一闪
"如果有一个机器人能帮我批量管理这些仓库就好了！"

于是 RepoForge 诞生了。

---

## 🚀 它是如何工作的

### 核心功能
1. **批量更新仓库信息** - 统一描述、标签、主页
2. **标准化 README 头部** - 自动添加 VIRTURA 生态定位信息
3. **创建标准化仓库** - 一键生成带 README、LICENSE、.gitignore 的新仓库
4. **本地与云端同步** - 保持本地工作区和 GitHub 同步

### 技术实现
- 使用 **PyGithub** 库操作 GitHub API
- 使用 **PyYAML** 管理配置
- 设计了清晰的配置文件结构，方便扩展

---

## 📖 使用指南（对于其他开发者）

如果你想使用 RepoForge 管理你自己的项目，非常简单：

### 1. 复制示例配置
```bash
cp config/secrets.example.yaml config/secrets.yaml
cp config/projects.example.yaml config/projects.yaml
```

### 2. 填入你的信息
编辑 `config/secrets.yaml`：
```yaml
github_token: "ghp_你的token"
github_username: "你的用户名"
local_workspace_root: "/path/to/你的工作区"
```

编辑 `config/projects.yaml`，添加你自己的项目。

### 3. 运行
```bash
# 预览
python3 scripts/auto_manage_repos.py --preview

# 执行
python3 scripts/auto_manage_repos.py --run
```

---

## 🎤 开发者后日谈

### 为什么要拆分成两个仓库？

最初，RepoForge 是一个"私人使用顺便开源"的项目。但很快发现了问题：

1. **隐私风险** - 不小心可能把 secrets.yaml 提交上去
2. **个人内容混杂** - 我的备份、任务、日志都在里面，别人 clone 了也没法用
3. **混淆** - 用户分不清哪些是示例，哪些是我个人的配置

### 解决方案
- **RepoForge（公开）** - 只保留开源代码、示例、文档
- **Forge（私有）** - 我自己实际用的，包含所有个人内容

这样既保证了开源精神，又保护了隐私，还让项目结构更清晰！

### 学到的东西
1. **开源项目从一开始就要设计好** - 想清楚哪些要公开，哪些要私有
2. **示例配置很重要** - 不要让用户看你的个人配置来学习
3. **.gitignore 是你的好朋友** - 仔细规划哪些文件不提交

### 未来计划
- 让 RepoForge 支持插件系统
- 添加更多生态扫描和分析功能
- 制作更好的文档和教程

---

## 🙏 感谢

感谢所有 VIRTURA 生态的参与者，感谢开源社区！

---

*钱誉文 Ewan Qian*
*2026年2月*
