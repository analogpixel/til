# Ansible adhoc command

run an adhoc command on machines in your inventory:

`ansible -i inventories/INV.yml HOSTGROUP --become -m command -a 'ls'`
