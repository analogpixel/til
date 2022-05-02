# SSH Debugging a conneciton

## open a debug connection
this will start another ssh server on the host with debugging turned
on.  From your client you can then connect to the host and 
see what is going on.

```sh
/usr/sbin/sshd -d -D -p 222 # on server
ssh -v -C -A -X -p 222 # on client
```
