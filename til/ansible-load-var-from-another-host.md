# Ansible load a variable, dynamically, from another host

Sometimes in ansible you need a certain host to run a command:

```
---
- hosts: my_host_group[0] 
  tasks:
  - name: get the variable value
    whatever_module: arg=arg_a
    register: result

- hosts: all
  tasks:
  - debug: var="{{result}}"
```


but the variables created on host_a stay on host_a.  So when you 
have another block with a different set of hosts, they don't have
access to that variable.

So, what you need to do, is specify the host and get the variable from it:

```
myvar = "{{ hostvars[groups['my_host_group'][0]]['datacenter_is_active'] }}"
```

this will look in your defined groups for `my_host_group` and pull out the first entry
just like the host def above did.  you can then access the variables that you
had set on that host.
