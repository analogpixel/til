# Bash run actual command and not alias

if you have a command `foo` but you also have an alias of `foo`, and you
want to just run the `foo` command directly, you can:

`env foo`  

and that'll run the command not the alias.  This works because `env` doesn't know about
aliases, so it won't use them.


https://unix.stackexchange.com/questions/103467/what-is-env-command-doing
