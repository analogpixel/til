# Python Install jupyterhub

I'm not on ubuntu ( ubuntu runs horribly on the raspberry-pi ) so I can't run the super fun
`curl -L https://tljh.jupyter.org/bootstrap.py | sudo -E python3 - --admin <admin-user-name>`  so
instead I guess I'll have to do the manual install:

## Good ol' manual install
```sh
sudo bash
python3 -m venv /opt/jupyterhub/
/opt/jupyterhub/bin/python3 -m pip install wheel jupyterhub jupyterlab jupyterhub jupyterlab
apt install nodejs npm
npm install -g configurable-http-proxy
mkdir -p /opt/jupyterhub/etc/jupyterhub/
cd /opt/jupyterhub/etc/jupyterhub/
/opt/jupyterhub/bin/jupyterhub --generate-config
echo "c.Spawner.default_url = '/lab'" >> /opt/jupyterhub/etc/jupyterhub/jupyterhub_config.py
mkdir -p /opt/jupyterhub/etc/systemd
vi /opt/jupyterhub/etc/systemd/jupyterhub.service
```

```
[Unit]
Description=JupyterHub
After=syslog.target network.target

[Service]
User=root
Environment="PATH=/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/opt/jupyterhub/bin"
ExecStart=/opt/jupyterhub/bin/jupyterhub -f /opt/jupyterhub/etc/jupyterhub/jupyterhub_config.py

[Install]
WantedBy=multi-user.target
```

```
ln -s /opt/jupyterhub/etc/systemd/jupyterhub.service /etc/systemd/system/jupyterhub.service
systemctl daemon-reload
systemctl enable jupyterhub.service
systemctl start jupyterhub.service
```

## Links
- https://jupyterhub.readthedocs.io/en/1.2.0/installation-guide-hard.html
