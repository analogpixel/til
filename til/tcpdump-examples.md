# TCPDUMP examples


watch traffic for hosts, and dump out full packets:
`tcpdump -XXA host 10.14.3.191 or host 10.14.3.192 or host 10.14.3.193`

Don't convert port numbers to names: `-nn`
Don't convert ips to hostnames: `-n`

