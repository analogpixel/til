# Azure grow centos disk

How to resize a centos 7  disk in azure:

- stop the node
- resize the disk 
- start the node
- `rpm -i http://mirror.centos.org/centos/7/os/x86_64/Packages/cloud-utils-growpart-0.29-5.el7.noarch.rpm`
- `gdisk -l /dev/sda`  and get the partition you want to grow (in this case 1)
- `growpart /dev/sda 1`  yes a space
- `xfs_growfs /`

## links
- https://docs.microsoft.com/en-us/azure/virtual-machines/linux/resize-os-disk-gpt-partition
