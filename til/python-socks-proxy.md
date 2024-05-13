# Python socks proxy support

If you want to add socks proxy support to your code:

```python
import socks
import socket
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "localhost", 1080)
socket.socket = socks.socksocket
```


