# Ansible debugger

## Enable ENV
`ANSIBLE_ENABLE_TASK_DEBUGGER=True ansible-playbook -i hosts site.yml`

## Debug on task
```yaml
- name: Execute a command
  ansible.builtin.command: "false"
  debugger: on_failed
```

## Debug on play
```yaml
- name: My play
  hosts: all
  debugger: on_skipped
  tasks:
    - name: Execute a command
      ansible.builtin.command: "true"
      when: False
```

## Print command
https://docs.ansible.com/ansible/latest/user_guide/playbooks_debugger.html#print-command

## links
* https://docs.ansible.com/ansible/latest/user_guide/playbooks_debugger.html
