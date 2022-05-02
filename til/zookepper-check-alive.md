# Zookeeper Check if alive

to check if zookeeper is running and you can connect to it from your host you can run:

`echo "ruok" | nc zookeeper-host 2181`

and you should get back `imok` in response.
