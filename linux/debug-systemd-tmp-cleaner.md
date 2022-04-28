# Debug systemd tmp cleaner

systemd is in charge of cleaning tmp files in various places,  if it isn't
working, this will show you why:

`env SYSTEMD_LOG_LEVEL=debug systemd-tmpfiles --clean`

