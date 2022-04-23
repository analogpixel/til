# Add or Update to a list in a dict

If you want to append to a list in a dict, but don't know if that key 
has a list in it arlready you can:

```python
mydict = {}
mydict.setdefault( 'key_name', [] ).append(post)
```

what this does is returns the dict value of the key 'key_name', but if
that key doesn't exist it return the default of `[]`, it then appends to that
list.
