# Python custom sort comparator

If you need a custom function to compare to values in a sort:

```python
from functools import cmp_to_key

zz = [1,2,3]

def sort_function(l,r):

    if compare(l,r):
        return -1
    else:
        return 1
  
s = sorted(zz, key=cmp_to_key(sort_function))
```
- return a negative value (< 0) when the left item should be sorted before the right item
- return a positive value (> 0) when the left item should be sorted after the right item
- return 0 when both the left and the right item have the same weight and should be ordered "equally" without precedence

