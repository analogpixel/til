# Python Add or Update to a list in a dict

If you want to append to a list in a dict, but don't know if that key 
has a list in it already you can:

```python
mydict = {}
mydict.setdefault( 'key_name', [] ).append(post)
```

* If the `key_name` exists, then just append(post)
* If the `key_name` does **not** exist, then create the key `key_name` with the default value of `[]` and then append(post)

```
>> help('dict.setdefault')

Help on method_descriptor in dict:

dict.setdefault = setdefault(self, key, default=None, /)
    Insert key with a value of default if key is not in the dictionary.

    Return the value for key if key is in the dictionary, else default.
```
