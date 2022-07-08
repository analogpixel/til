# Rclone mount cloud drives

Rclone is a command-line program to manage files on cloud storage. It is a feature-rich alternative to cloud vendors' web storage interfaces. Over 40 cloud storage products support rclone including S3 object stores, business & consumer file storage services, as well as standard transfer protocols.

So if you wanted to mount your pcloud drive on a raspberry pi that doesn't support the pcloud client, you can run
`rclone setup` then:

```sh
fusermount -uz pcloud
rclone mount --vfs-cache-mode=full  --daemon pcloud:/ pcloud
```

the `fusermount` command was to unmount the drive, as it didn't appreciate my ctrl-c to stop the initial one.
