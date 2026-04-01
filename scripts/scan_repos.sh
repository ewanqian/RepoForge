#!/bin/bash
# Script to scan all ewanqian repos and collect status

WORKSPACE="/root/.openclaw/workspace"
REPORTS_DIR="$WORKSPACE/reports"
mkdir -p "$REPORTS_DIR"

REPO_LIST=($(gh repo list ewanqian --limit 100 --json name --jq '.[].name'))

echo "Scanning ${#REPO_LIST[@]} repositories..."

for REPO in "${REPO_LIST[@]}"; do
  echo "Processing $REPO..."
  REPORT_FILE="$REPORTS_DIR/$REPO-status.md"
  
  echo "# $REPO Status" > "$REPORT_FILE"
  echo "" >> "$REPORT_FILE"
  
  # Repo basic info
  gh repo view "ewanqian/$REPO" --json name,description,visibility,updatedAt,defaultBranchRef,pushedAt,isArchived,isDisabled,isFork,isMirror,isTemplate,url >> "$REPORT_FILE.tmp"
  jq -r '
    "## 基本信息",
    "- 名称: \(.name)",
    "- 描述: \(.description)",
    "- 可见性: \(.visibility)",
    "- 最后更新: \(.updatedAt)",
    "- 最后推送: \(.pushedAt)",
    "- 默认分支: \(.defaultBranchRef.name // "unknown")",
    "- 是否归档: \(.isArchived)",
    "- 是否禁用: \(.isDisabled)",
    "- 是否Fork: \(.isFork)",
    "- 是否镜像: \(.isMirror)",
    "- 是否模板: \(.isTemplate)",
    "- URL: \(.url)"
  ' "$REPORT_FILE.tmp" >> "$REPORT_FILE"
  
  echo "" >> "$REPORT_FILE"
  
  # Last 5 commits
  echo "## 最近提交" >> "$REPORT_FILE"
  gh api "repos/ewanqian/$REPO/commits?per_page=5" --jq '
    .[] | 
    "- \(.commit.committer.date | fromdateiso8601 | strftime("%Y-%m-%d %H:%M:%S")): \(.commit.message | split("\n")[0]) (@\(.author.login // "unknown"))"
  ' >> "$REPORT_FILE" 2>/dev/null || echo "- 无法获取提交记录" >> "$REPORT_FILE"
  
  echo "" >> "$REPORT_FILE"
  
  # Open issues
  echo "## 未关闭 Issue" >> "$REPORT_FILE"
  gh issue list --repo "ewanqian/$REPO" --state open --limit 10 --json number,title,createdAt,author >> "$REPORT_FILE.tmp" 2>/dev/null
  jq -r '
    if length == 0 then "- 无未关闭 Issue" else
      .[] | "- #\(.number): \(.title) (创建于 \(.createdAt), @\(.author.login))"
    end
  ' "$REPORT_FILE.tmp" >> "$REPORT_FILE"
  
  echo "" >> "$REPORT_FILE"
  
  # Open PRs
  echo "## 未合并 PR" >> "$REPORT_FILE"
  gh pr list --repo "ewanqian/$REPO" --state open --limit 10 --json number,title,createdAt,author >> "$REPORT_FILE.tmp" 2>/dev/null
  jq -r '
    if length == 0 then "- 无未合并 PR" else
      .[] | "- #\(.number): \(.title) (创建于 \(.createdAt), @\(.author.login))"
    end
  ' "$REPORT_FILE.tmp" >> "$REPORT_FILE"
  
  rm -f "$REPORT_FILE.tmp"
  echo "Wrote report to $REPORT_FILE"
done

echo "All repos scanned successfully!"
