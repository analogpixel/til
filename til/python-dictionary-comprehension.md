# Python Dictionary Comprehension

Python list comprehension looks like: `[x for x in [1,2,3]]`  and returns `[1,2,3]`

Python dictionary comprehension looks like: `{key: True for key in [1,2,3]}` and returns `{1: True, 2: True, 3: True}`

you could use that to check if one list is a subset of another list:
```python
# check if list a is a subset of list b
def a_subset_b(a,b):
    tmp = {z: True for z in b}
    return all( [ tmp.get(x, False) for x in a] )
```

More examples:
`{k:v for (k,v) in [ [1,2], [3,4] ]}`  returns: `{1: 2, 3: 4}`


