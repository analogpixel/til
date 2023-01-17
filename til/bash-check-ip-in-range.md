# Bash check if ip is in subnet range

Simple script from SO to check if an ip is in a subnet range.

```bash
#!/bin/bash

v4dec() {
        for i; do
                echo $i | {
                        IFS=./
                        read a b c d e
                        test -z "$e" && e=32
                        echo -n "$((a<<24|b<<16|c<<8|d)) $((-1<<(32-e))) "
                }
        done
}

v4test() {
        v4dec $1 $2 | {
                read addr1 mask1 addr2 mask2
                if (( (addr1&mask2) == (addr2&mask2) && mask1 >= mask2 )); then
                        return 0
                else
                        return 1
                fi
        }
}

check_ip=$1


if v4test $check_ip $net ; then
  echo "Ok it's in the net"
fi
```
