# Python pretty print a dict/hash

An easy way to pretty print something in python is to just
have the json (or yaml) module export it:

```python
import json 
print(json.dumps(blog_data, indent=2))
```

you can also use the [pretty print module](https://docs.python.org/3.8/library/pprint.html):

```python
import pprint
pprint.pprint( blog_data)
```
