# Macos find process listening on port

find out what processes is listening on a certain port:

`sudo lsof -i -P | grep LISTEN | grep :8080`

