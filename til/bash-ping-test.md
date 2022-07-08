# Bash ping test

Check if a host is up

```bash
if ping -c 1 ${host_name}.rally.prod &> /dev/null
then
  echo "${host_name} up ; continue"
else
  echo "Unable to ping ${host_name}.rally.prod"
  exit 1
fi
```

I did find that on macos, if you don't specify a FQDN, then something on .home will always respond to ping.

## simple oneline
````bash
ping -c 1 127.0.0.1 &> /dev/null && echo success || echo fail
````

## SSH check with ansible
check to make sure the host is up with ssh :
```bash
if ! "${bin_dir}/bin/ansible" -i "inventories/${site}.yml" "${host_name}" -e time=240 -c local -m wait_for -a 'host={{ ansible_ssh_host }} port=22 timeout=240' >/dev/null 2>&1; then
  printf "The host %s did not come back up after %d seconds\n" "${host_name}" "240"
  exit 1
else
  printf "SSH is up on %s, continuing...\n" "${host_name}"
fi
```

---
