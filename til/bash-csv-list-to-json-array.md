# Bash Convert CSV list to JSON array

If you have a list of items like `a,b,c`  and you
want to convert them to a list format to be used
by JSON you can run:

```
echo "a,b,c" | tr ',' '\n' | jq -ncR '[inputs]'`
```

which will output `["a","b","c"]`
