# Python Date and Time

## EPOC time
```python
import time
time.time()
```

## Now
Get now with a string format:
```python
from datetime import datetime
datetime.today().strftime("%m-%d-%Y")
```

## Sort by date
this converts a string to a date and then to epoc seconds, and then
sorts on that;  There is probably a better way to do this:
```
from datetime import datetime
sorted(ret, key=lambda x: int(datetime.strptime(x['post_date'], "%m-%d-%Y").strftime("%s")), reverse=True)
```

## Date Math

If you have a date and want to add to it, you can use a [timedelta](https://docs.python.org/3/library/datetime.html#timedelta-objects)  

```
import datetime

today = datetime.datetime.now().date()
tomorrow = today + datetime.timedelta(days=1)
```

you can also loop over days to a certain point:

```
while current_date <= datetime.datetime.now().date():
  current_date += datetime.timedelta(days=1)
```
