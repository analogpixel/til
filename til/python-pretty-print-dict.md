# Python pretty print a dict/hash

An easy way to pretty print something in python is to just
have the json (or yaml) module export it:

```python
import json 
print(json.dumps(blog_data, indent=2))
```

you can also use the pretty print module:

```python
import pprint
pp = pprint.PrettyPrinter(depth=4)
pp.pprint( blog_data)
```
