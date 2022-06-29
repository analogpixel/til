# RaspberyPi automount usb drives

I was having a hard time getting `mu-editor` to find my raspberry pi 2040 
running circuitpython on my Raspberry pi 4.  First problem, was I was using
the usbc cable that cable with some headphones, which supplied power, but not
data.  After fixing that problem (and throwing away the useless cable) I was
having issues with mu-editor finding the board.  The problem being that I was
running i3 and not the default window manager that comes with the PI; this
matters because the default wm that comes with the PI automounts usb drives
when they get plugged in, and i3 does not.

So, to setup automounting of usb drives when they get plugged in under i3 you do this:

- `sudo apt install udevil`
- edit `/etc/systemd/system/devmon.service`  and add this:

```
[Unit]
Description=Automounting usb drives.
After=network.target

[Service]
Type=simple
User=pi
Restart=on-abort
ExecStart=/usr/bin/devmon

[Install]
WantedBy=multi-user.target
```

- `sudo systemctl enable devmon.service`
- `sudo systemctl start devmon.service`

And now you have automounting device.  

A lot of places on the internet tell you to use `usbmount`, but it's not available for
`Debian GNU/Linux 11 (bullseye)`  (apt install doesn't find it; I guess it was 
removed from debian for bug related reasons)


## links
- https://raspberrypi.stackexchange.com/questions/100312/raspberry-4-usbmount-not-working
