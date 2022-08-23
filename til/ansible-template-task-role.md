# Ansible template task to run a role

Run a role, calling a specific task

```yaml
---
- hosts: zookeeper_server
  gather_facts: true
  become: true
  tasks:
    - ansible.builtin.include_role:
        name: zookeeper-role
        tasks_from: node_exporter_crons.yml

```
