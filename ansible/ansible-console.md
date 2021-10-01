# Ansible console a repl for ansible

you can run `ansible-console` like you would `ansible`: `ansible-console -i myinv.yml --limit onehost`  but then instead of a playbook/command running you are 
dropped into an interactive shell where you can run ansible commands like:

- `debug var=hostvars['myhost']`  : list out all the host variables for that host.

