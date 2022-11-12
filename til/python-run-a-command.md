# Python run a command and get the output

This is a closely guarded secret in the python community, most
people want you to type in lines upon lines of commands, or
break your command into a list first, and then setup pipes
and redirects, but really all you need to do is:

```python
import subprocess

output = subprocess.getoutput("ls -l")
```

Not as nice as Perl where you can just use backticks, but
I guess this is as nice as it's going to get with python for now.

