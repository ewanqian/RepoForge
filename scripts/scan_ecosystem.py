import os
import yaml
from github import Github

def load_config():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    config_path = os.path.join(script_dir, "../config/projects.yaml")
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    
    secrets_paths = [
        os.path.join(script_dir, "../config/secrets.yaml"),
        os.path.expanduser("~/.repoforge/secrets.yaml"),
    ]
    
    secrets = None
    for path in secrets_paths:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                secrets = yaml.safe_load(f)
            break
    
    if secrets is None:
        raise FileNotFoundError("找不到 secrets.yaml")
    
    return config, secrets

def scan_repos():
    config, secrets = load_config()
    g = Github(secrets["github_token"])
    user = g.get_user()
    
    print("=" * 80)
    print("📊 Ewan Qian 生态知识网络扫描")
    print("=" * 80)
    
    print(f"\n👤 用户: {user.name} (@{user.login})")
    print(f"📍 位置: {user.location if user.location else '未知'}")
    print(f"📝 Bio: {user.bio if user.bio else '无'}")
    print(f"🏆 公开仓库: {user.public_repos}")
    
    print("\n" + "=" * 80)
    print("🌐 生态中台矩阵")
    print("=" * 80)
    
    repos_by_role = {}
    for project in config["projects"]:
        role = project["role"]
        if role not in repos_by_role:
            repos_by_role[role] = []
        repos_by_role[role].append(project)
    
    for role in sorted(repos_by_role.keys()):
        print(f"\n🔹 {role}")
        for project in repos_by_role[role]:
            print(f"  - {project['name']} ({project['english_name']})")
            print(f"    📌 {project['description'][:60]}...")
    
    print("\n" + "=" * 80)
    print("🧠 核心主张与研究方向")
    print("=" * 80)
    
    core_insights = [
        "1. 媒介越复杂，越需要更严格的审美准则与制作标准",
        "2. 把一次性发生的演出与展览，延伸为可保存、可再体验、可迁移的数字资产",
        "3. 推动将作品沉淀为可复用的数字资产与氛围资产库",
        "4. 面向空间计算媒介（Apple Vision Pro）的迁移实践",
        "5. 让一次制作获得更长的生命周期与更可持续的回报",
    ]
    
    for insight in core_insights:
        print(f"\n💡 {insight}")
    
    print("\n" + "=" * 80)
    print("🚀 技术路线图")
    print("=" * 80)
    
    roadmap = [
        {
            "phase": "Phase 1: 资产化",
            "items": [
                "舞台/演出数字化保存",
                "音画活动资产库建设",
                "可复用组件标准化"
            ]
        },
        {
            "phase": "Phase 2: 空间化",
            "items": [
                "Apple Vision Pro 沉浸式体验迁移",
                "从 2D 到 3D 叙事转换",
                "低门槛分发沉浸版本"
            ]
        },
        {
            "phase": "Phase 3: 产品化",
            "items": [
                "LiveForge 全链路工作流",
                "SceneForge 场景查看器",
                "Mac → Vision Pro 串流方案"
            ]
        }
    ]
    
    for phase in roadmap:
        print(f"\n📍 {phase['phase']}")
        for item in phase["items"]:
            print(f"  ➜ {item}")
    
    print("\n" + "=" * 80)
    print("🤝 合作方式")
    print("=" * 80)
    
    collaboration = [
        {
            "type": "现场演出视觉交付",
            "desc": "音乐现场、舞蹈/剧场、展演空间的视觉设计与技术实现"
        },
        {
            "type": "沉浸式内容制作",
            "desc": "面向 Apple Vision Pro 等空间计算媒介的沉浸体验开发"
        },
        {
            "type": "数字资产沉淀",
            "desc": "一次性演出/展览转化为可复用、可分发的数字资产"
        },
        {
            "type": "技术咨询",
            "desc": "LiveForge / SceneForge 生态体系应用咨询"
        }
    ]
    
    for collab in collaboration:
        print(f"\n🎯 {collab['type']}")
        print(f"   {collab['desc']}")
    
    print("\n" + "=" * 80)
    print("📌 下一步（经纪人建议）")
    print("=" * 80)
    
    next_steps = [
        "1. 整理已有的音画活动记录，建立资产库索引",
        "2. 用 Blender 做三维模型动画练习，为 Vision Pro 开发做准备",
        "3. 基于 LiveForge，开发 Mac → Vision Pro 的串流场景查看器原型",
        "4. 完善 portfolio 的作品展示部分",
        "5. 建立清晰的报价体系与合作流程"
    ]
    
    for step in next_steps:
        print(f"\n✅ {step}")
    
    print("\n" + "=" * 80)
    print("扫描完成！")
    print("=" * 80)

if __name__ == "__main__":
    scan_repos()
