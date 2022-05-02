# RPM Fix Corrupt database

```sh
rm -f /var/lib/rpm/__db.00* ; rpm --rebuilddb
db_verify /var/lib/rpm/Packages ; yum clean all
```
