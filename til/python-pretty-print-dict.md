# Python pretty print a dict/hash

An easy way to pretty print something in python is to just
have the json (or yaml) module export it:

```python
import json 
print(json.dumps(blog_data, indent=2))
```
