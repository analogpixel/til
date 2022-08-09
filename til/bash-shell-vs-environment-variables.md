# Bash shell vs. environment variables

shell variables set with:
```bash
x=5
```
don't persist when a new shell is started.

environmnet variables set with:
```bash
export x=5
```

do persist when a new shell is started.


```
root@linux ~# x=5                <= here variable is set without export command
root@linux ~# echo $x
5
root@linux ~# bash               <= subshell creation
root@linux ~# echo $x            <= subshell doesnt know $x variable value
root@linux ~# exit               <= exit from subshell
exit
root@linux ~# echo $x            <= parent shell still knows $x variable
5
root@linux ~# export x=5         <= specify $x variable value using export command
root@linux ~# echo $x            <= parent shell doesn't see any difference from the first declaration
5
root@linux ~# bash               <= create subshell again
root@linux ~# echo $x            <= now the subshell knows $x variable value
5
root@linux ~#
```

https://superuser.com/questions/821094/what-is-the-difference-between-set-env-declare-and-export-when-setting-a-varia
