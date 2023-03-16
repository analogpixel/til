# Ansible append to a fact


If you have a loop and you want to append data to a fact you can:

```
- set_fact:
        failed_roles: "{{ failed_roles|default([]) + [ item_my_role ] }}"
```

```
    - name: Get a list of all job objects
      no_log: true
      kubernetes.core.k8s_info:
        api_version: v1
        kind: Job
      register: service_list

    - set_fact: 
        jobs: "{{ jobs + [ 'name=' + item.metadata.name + ' namespace=' + item.metadata.namespace ] }}"
      loop: "{{ service_list | json_query('resources[*]') }}"
      no_log: true
      vars:
        jobs: []

    - debug:
        var=jobs
```
