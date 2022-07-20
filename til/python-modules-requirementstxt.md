# Python define modules to install

If you want to keep track of what modules your python program needs to run, you 
can store them in a text file and call that with pip.  Great for when you
are building docker images:

create the file `requirements.txt` and list out the modules you want to install:

```
modulename1==version
modulename2
```

then run `pip install -r requirements.txt` or as the fancy python people like to do `python -m pip install -r requirements.txt`
