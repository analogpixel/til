# Bash export yaml var file as environmental variables 

if you have a yaml file of variables that looks like this:

```yaml
---
var1: value1
var2: value2
```

you can then export them all to the shell like this:

```
export $(cat vars.yml | sed "s/: /=/" | grep -v "\-\-\-" | xargs -L 1)
```
