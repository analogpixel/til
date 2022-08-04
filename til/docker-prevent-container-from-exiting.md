# Docker prevent container from exiting 

if you don't want a docker container to exit you can do something 
like this in the Dockerfile:

```
FROM ubuntu:latest

ENTRYPOINT ["tail", "-f", "/dev/null"]
```
