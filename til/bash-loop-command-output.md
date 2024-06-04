# Bash loop over command output

if you want to run a command, and loop over it line by line:

```
while IFS= read -r line; do
    open $line
  done < <(awk -f ${LGT_DIR}/.bin/extract_open.awk ${LGT_DIR}/$topic/README.md)
```


