# Packer in a docker container

when getting this error:

`Error waiting for SSH: Error configuring bastion: SSH_AUTH_SOCK is not set`

when you try to run packer inside of a docker container, you can just run: `` eval `ssh-agent` `` before the packer
command, and it'll create to auth sock for you.


