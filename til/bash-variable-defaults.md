# Bash variable defaults :- vs :=

How to set default values in bash:
- `:-` doesn't update empty var, `bar`, just `foo`  `foo=echo ${bar:=something}`
- `:=` will update empty var, `bar`,  and `foo` `foo=${bar:=something}`


```
foo=${bar:-something}

echo $foo # something
echo $bar # no assignement to bar, bar is still empty

foo=${bar:=something}

echo $foo # something
echo $bar # something too, as there's an assignement to bar
```

