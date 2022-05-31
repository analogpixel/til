# Curl resolve hostname to different IP

instead of updating your /etc/host file, just use `--resolve`
to have curl change the hostname to a new ip.

`curl --resolve hostname:443:new-ip https://hostname`

