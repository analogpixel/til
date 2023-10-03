# SSH socks proxy server

login to remote host `pi-` as `pi` and start a socks proxy on port `9090`.  Then just configure your browser to point to `localhost:9090` for socks proxy and all traffic will go through the other host:

`ssh -N -D 9090 pi@pi-1`
