# Bash cycle through arguments

## This way allows you to start from wherever you are in the stack

```bash
while test $# -gt 0
do
    echo "$1"
    shift
done
```

## This way just loops through all the arguments in the stack

```bash
for var in "$@"
do
    echo "$var"
done
```

