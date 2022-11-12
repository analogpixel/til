# Python create a directory (create parents)

If you want to create a directory, and all the parent directories (mkdir -p)
all you need to do is:

```python
import pathlib

pathlib.Path("/this/is/the/path/to/create").mkdir(parents=True, exist_ok=True)
```


