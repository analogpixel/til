# Python Overriding __init__

if you have a class, and you want to override the init function but still
call the parents __init__ function you would do this:

```python
class FileInfo(dict):
    """store file metadata"""
    def __init__(self, filename=None):
        super(FileInfo, self).__init__()
        self["name"] = filename
```


## links
- https://stackoverflow.com/questions/753640/inheritance-and-overriding-init-in-python
