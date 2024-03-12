# Ansible backup files

If you are using ansible and want to backup a file before a template or copy, some modules
provide a `backup` option.  `backup: true` on a template will create a backup.  If you
register that task (for example `register: test`) you can then use `test.backup_file` to get
the name of the backup

*note* if the file doesn't change, then a backup won't be made, also, `test.backup_file` won't exist.

## Sample file

```yaml
- hosts: all 
  become: yes
  gather_facts: no
  tasks:

  - name: Create a file with inline content
    ansible.builtin.copy:
      backup: true
      dest: "/tmp/test_file_001"
      content: |
        # This is a configuration file
        Test file 001 aaa
    register: back_file

  - name: debug
    debug: 
      msg: "{{ back_file }}"

```

## links
- https://docs.ansible.com/ansible/latest/collections/ansible/builtin/template_module.html#parameter-backup
