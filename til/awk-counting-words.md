# Awk counting words

Awk has a nice array feature that looks like this:
```
if key in array:
  increment array value for key by 1
else:
  set array value for key to 1
```

so you don't have to worry about initializing the value, using that, you can then
do something like this to count words:

```awk
awk '{for(i=1;i<=NF;i++) a[$i]++} END {for(k in a) print k,a[k]}' testfile
```

- loop over every field
- for each field(word) increment that key in the array
- print out all the keys/values at the end
