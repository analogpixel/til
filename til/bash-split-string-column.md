# Bash split string by column separator 

split a string by a separator:

```bash
string='one_two_three'
IFS='_' read -r var_one var_two var_three  <<< "$con"
unset IFS
echo $var_one
```

