# Ansible omit/remove module parameter if variable is null

If you want ansible to completely remove a parameter in the module definition if a 
variable isn't set, you can use `default(omit)`  in the example below, if item.mode isn't set,
then the entire 'mode:....' line will be removed.

```
- name: Touch files with an optional mode
  ansible.builtin.file:
    dest: "{{ item.path }}"
    state: touch
    mode: "{{ item.mode | default(omit) }}"
  loop:
    - path: /tmp/foo
    - path: /tmp/bar
    - path: /tmp/baz
      mode: "0444"
```

https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_filters.html#making-variables-optional
