# 给其他 AI Agent 的提示：RepoForge 项目结构更新

## 📢 重要更新

从现在开始，**RepoForge** 和 **Forge** 是两个分开的仓库，分工明确：

---

## 🏗️ 仓库分工

| 仓库 | 可见性 | 位置 | 用途 |
|------|--------|------|------|
| **RepoForge** | 公开 | GitHub: ewanqian/RepoForge | 仅用于展示 - 包含开源代码、示例配置、文档 |
| **Forge** | 私有 | GitHub: ewanqian/Forge | 实际使用 - 包含个人配置、任务、敏感信息 |

---

## 📂 你应该操作哪个仓库？

### 如果你要：
- ✅ **修改开源代码** → 用 **RepoForge**
- ✅ **更新示例配置** → 用 **RepoForge**
- ✅ **写文档** → 用 **RepoForge**
- ✅ **管理 Ewan 的实际项目** → 用 **Forge**
- ✅ **执行自动化任务** → 用 **Forge**
- ✅ **访问个人配置** → 用 **Forge**

---

## 🔑 RepoForge（公开）包含：
- `scripts/` - 开源脚本（auto_manage_repos.py, scan_ecosystem.py, deep_scan.py）
- `config/secrets.example.yaml` - 示例 secrets 配置
- `config/projects.example.yaml` - 示例项目配置
- `docs/` - 文档
- `README.md` - 使用说明
- `.gitignore` - 忽略规则

**注意**：RepoForge 里没有 `config/secrets.yaml` 和 `config/projects.yaml`（这些在 .gitignore 里）

---

## 🔐 Forge（私有）包含：
- Ewan 的实际 `config/secrets.yaml`
- Ewan 的实际 `config/projects.yaml`
- `tasks/` - 任务目录
- `backup/` - 备份目录
- `logs/` - 日志目录
- 其他个人内容

---

## 💡 工作流程建议

1. 先确认你要做什么
2. 选择正确的仓库（RepoForge vs Forge）
3. 如果是开源相关的改进，在 RepoForge 里做
4. 如果是管理 Ewan 的实际项目，在 Forge 里做

---

## 📝 最后更新

- 日期：2026年2月22日
- 执行人：钱誉文 Ewan Qian
