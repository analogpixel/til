# Python dataclasses (c like struct)

if you want to create something like a C struct in python, you can use a dataclass. 

```python
from dataclasses import dataclass
import re

@dataclass
class Nodes:
    l: str
    r: str

n = Nodes("ZZZ","AAA")

n.l
n.r

```

