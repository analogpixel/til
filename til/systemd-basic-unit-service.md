# Systemd basic unit service

* copy to `/etc/systemd/system` and then run `systemctl daemon-reload`

```
[Unit]
Description=Service Name
After=network.target

[Service]
Type=forking|simple
Environment=var=value
User=run_as_user
Group=run_as_group
Restart=always
RestartSec=5
StartLimitIntervalSec=0 # always restart

ExecStart= my command \
           multiline

[Install]
WantedBy=multi-user.target
```

## docs
* `man 5 systemd.unit`
* [service types](https://www.freedesktop.org/software/systemd/man/systemd.service.html#Type=)
