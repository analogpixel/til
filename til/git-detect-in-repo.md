# Git Detect if you are in git repo

```bash
  if  git rev-parse --git-dir > /dev/null 2>&1; then
    echo "ok"
  else
    echo "Must be run from git repo"
    exit 1
  fi
```
