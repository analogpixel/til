# Python working with CSV files

```python
import csv

with open("filename.csv") as csvfile:
  csv_object = csv.reader(csvfile)
  junk  = csv_object.__next__()

  for item in csv_object:
    print( item[0] )
```

## Slurp a column into a list
```python
col_1 = [ x[1] for x in csv_object ] 
```
