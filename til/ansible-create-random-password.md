# Ansible create a random password

the `lookup('ansible.builtin.password')` function will return a random password.  If you give it 
a file name, it will write the password to the controller:

```yaml
- name: create random but idempotent password
  ansible.builtin.set_fact:
    password: "{{ lookup('ansible.builtin.password', '/dev/null', seed=inventory_hostname) }}"

```

- If the file already exists, no data will be written to it. If the file has contents, those contents will be read in as the password. Empty files cause the password to return as an empty string.

## Links
- https://docs.ansible.com/ansible/latest/collections/ansible/builtin/password_lookup.html

