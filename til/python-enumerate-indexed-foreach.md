# Python enumerate indexed foreach

If you have a list of values `['a','b','c']`  and you want to loop
over them and get their index values:

```python
l = ['a','b','c']
for index_value, x in enumerate(l):
  print(index_value,x)
```

outputs:
```
0 a
1 b
2 c
```
