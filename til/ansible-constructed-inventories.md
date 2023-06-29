# Ansible Constructed Inventories (dynamic)

How to create a dynamic inventory using jinja

## 1-hosts
```
a1_dev_01 vm_x=vm-1
a1_dev_02 vm_x=vm-2
a1_dev_03 vm_x=vm-3
a2_jump_01 vm_x=vm-0

[dev_postgres]
a1_dev_01
a1_dev_02

[dev_ldap]
a1_dev_02
a1_dev_03

[dev:children]
dev_postgres
dev_ldap

[dev:vars]
env=dev

[jumphost]
a2_jump_01

[all:vars]
vm_domain=my.internal.domain.com
```

## 2-constructed.yml

create a dynamic group with all hosts that start with a1, and also
update host names to be FQDN.

```
plugin: constructed
strict: true
compose:
  ansible_host: vm_x ~ '.' ~ vm_domain

groups:
  a1-dynamic-hosts: inventory_hostname.startswith('a1')
```

## View the inventory

`ansible-inventory -i 1-hosts -i 2-constructed.yml  --list --yaml`

## Notes

note that a lot of the documentation (almost all I found) just assumes you have
default inventories that you pull in for the constructed to work from.   so
make sure to include all the target inventories you need for the dynamic
inventories to work from. 

## links
- https://stackoverflow.com/questions/71353557/how-to-properly-build-an-ansible-inventory
- https://www.lutro.me/posts/complex-groups-in-ansible-using-the-constructed-inventory-plugin
