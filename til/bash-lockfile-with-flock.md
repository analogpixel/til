# Bash Lock File with Flock

If you have a script that you only want one copy of running at a time, you can
use **flock** to create a lockfile to prevent multiple copies from running:

```bash
(
flock -x -w 10 200 || exit 1

echo "do stuff here"

) 200>/var/lock/.script_lock
```

If another instance of your script is running, this will wait 10 seconds, and then fail. 
The 200 is the file handle to use, and can be any high number.

If you are running something from a cronjob that says polls an external resource, this would be
good to prevent lots of processes piling up if the external service went away causing
your bash script to hang.   

You could also do something like this to timeout your bash script:
```bash
#!/bin/sh
( your_command ) & pid=$!
( sleep $TIMEOUT && kill -HUP $pid ) 2>/dev/null & watcher=$!
wait $pid 2>/dev/null && pkill -HUP -P $watcher
```
