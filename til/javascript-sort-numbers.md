# Javascript sort numbers

by default javascript will sort your list as strings, so
make you need to do this:

```
[1,2,3,10,11,12].sort((a, b) => a - b)

(a, z) => a - z // ascending, like "a to z"
(a, z) => z - a // descending, like "z to a"
```

