# Justfile a basic example

basic justfile:

```yaml
default:
  just --list

alias mc := my_command

my_command opt1="" opt2="":
  #!/usr/bin/env bash
  echo $opt1

```


