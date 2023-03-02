# Ansible append to a fact


If you have a loop and you want to append data to a fact you can:

```
- set_fact:
        failed_roles: "{{ failed_roles|default([]) + [ item_my_role ] }}"
```
