# Ansible Run Task From Role

If you want to run a specific task from an ansible role (change the entrypoint from main) then you can
use `tasks_from` in the `include_role` section:

```yaml
  # invoke role's default "entrypoint" (main.yml)
  roles:
    - my_role

  tasks:
    # include the role, but tasks from other.yml
    - include_role:
        name: my_role
        tasks_from: other.yml
```
[src](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/include_role_module.html)

you can also just run the task directly with:

```yaml
  tasks:
    - include_tasks: path/to/my_role/tasks/other.yml
```
