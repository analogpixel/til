# Python environment boolean variable

if you want to read in a value from the environment and make it a boolean you 
can do this:

```
IS_TEST = os.getenv('IS_TEST', "False").lower() in ['true', '1', 't']
```
