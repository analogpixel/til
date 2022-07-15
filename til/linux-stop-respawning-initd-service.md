# Linux stop respawning initd service

If you have a serivce that restarts as soon as you kill it, it's probably
getting restarted by the init process.  You can stop the process by running:

```
initctl stop <servicename>
```

