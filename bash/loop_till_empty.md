# Loop till string is empty in bash

```bash
doc="this/is/the/string/to/chop"

while [-n "${doc}" ] ; do
  # strip off a / chunk at a timee
  doc=${doc%/*} 
  echo $doc
done
```
