# RepoForge 工作交接

&gt; 本地操作者 ↔ 云端机器人 简单协作

## 核心原则

**用 Markdown 文件说话，简单直接。**

---

## 目录结构

```
RepoForge/
├── tasks/
│   ├── pending/      # 待处理任务（放这里）
│   └── completed/    # 已完成任务（做完移到这里）
├── logs/             # 操作日志（随便写）
└── handover/         # 本文档
```

---

## 协作流程

### 本地 → 云端机器人

1. **写任务**：在 `tasks/pending/` 创建一个 Markdown 文件
2. **写清楚**：任务描述、步骤、优先级、分配给谁
3. **提交推**：git add, commit, push
4. **机器人看**：云端机器人会去 pending 目录找活干

### 云端机器人 → 本地

1. **机器人写**：机器人在 `tasks/pending/` 写任务给你
2. **你看**：pull 下来看看有什么事
3. **你做**：做完移到 `tasks/completed/`
4. **提交推**：git add, commit, push

---

## 任务模板

```markdown
# [任务标题]

## 信息
- **创建时间**: 2026-02-21
- **分配给**: cloud_bot  # 或者 local
- **优先级**: high/medium/low

## 描述
简单说一下要干什么。

## 步骤
1. 步骤一
2. 步骤二
3. 步骤三

## 备注
随便写点什么。
```

---

## 常用命令

```bash
# 管理仓库
python3 scripts/auto_manage_repos.py --preview
python3 scripts/auto_manage_repos.py --run
```

---

就这么简单，干就完了！
