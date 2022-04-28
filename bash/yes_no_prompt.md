# Yes/No Prompt in Bash

```bash
read -p "Are you sure? " -n 1 -r
echo    # (optional) move to a new line
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    exit 1
fi
```

## Link
* https://www.shellhacks.com/yes-no-bash-script-prompt-confirmation/
