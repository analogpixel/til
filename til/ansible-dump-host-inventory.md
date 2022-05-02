# Ansible Dump out all the host inventory

`debug msg="{{ hostvars[inventory_hostname].ansible_ssh_host }}"`
