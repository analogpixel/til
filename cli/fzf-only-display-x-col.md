# Only display certain columns in fzf

* `-d` set the separator to look at
* `--with-nth`  sets the columns you want to show up in the fzf list

```bash
find til -name "*.md" -exec printf "{}:" \; -exec head -n 1 {} \;  | fzf -d ":" --with-nth 2 | cat $(awk -F: {"print \$1"})'
```

After you select an item, fzf will return the entire line, not just the displayed part. 
