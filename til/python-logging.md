# Python logging

Pythons built in logging module

```python
import logging
logging.basicConfig(level=logging.DEBUG)

loggin.debug("message to print when in debug mode")
logging.info("hi")
logging.warning("warning!")
logging.error("oh no")
logging.fatal("really oh no")

logging.info("var1: %s  var2: %s" var1, var2)
```

## log to a file
`logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)`

## Adding date to the output logs
`logging.basicConfig(format='%(asctime)s %(message)s')`

## Set via Environment Variable
```python
LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO').upper()
logging.basicConfig(level=LOGLEVEL)
```

https://docs.python.org/3/library/logging.html

