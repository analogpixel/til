# Bash Loop over comma

```bash
variable=abc,def,ghij
for i in ${variable//,/ }
do
    # call your procedure/other scripts here below
    echo "$i"
done
```
