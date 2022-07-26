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

```

## log to a file
`logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)`

## Adding date to the output logs
`logging.basicConfig(format='%(asctime)s %(message)s')`

https://docs.python.org/3/library/logging.html

