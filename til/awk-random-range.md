# Awk random number in range

If you want a random number within in a range in bash/awk/shell script:

```bash
function ran_range() {
  awk -v t=$2 -v b=$1 'BEGIN{ srand(); printf "%d\n", rand()*(t-b)+b  }'
}
```

This bash function takes 2 arguments, the low and high value of the range you want
a random number in.  These values are passed into awk via the `-v` flag which allows
you to pass shell variables in as awk variables.

We then get a random value between 0-1, multiply it by (high-low) and then add the low value 
to it.



