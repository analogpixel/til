# Python Assignment in Expression (assign variable in if condition) The walrus operator :=

To use the results of of your conditional you can use the `:=` operator 

```python
if x := re.match('(.*)', s):
  print("match is:", x)
```

before you would have to do something like:
```python
x = re.match('(.*)', s)
if x:
  print(x)
```

https://peps.python.org/pep-0572/
