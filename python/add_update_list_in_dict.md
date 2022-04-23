# Add or Update to a list in a dict

If you want to append to a list in a dict, but don't know if that key 
has a list in it arlready you can:

```python
mydict = {}
post_group.setdefault( mydict['key_with_list'], [] ).append(post)
```

what this does is returns the dict value of the key 'key_with_list', but if
that key doesn't exist it return the default of `[]`, it then appends to that
list.
