# Flask Console Output in kubernetes with python

to get console output in kubernetes logs with flask:

```python
print('This is error output', file=sys.stderr)
```

