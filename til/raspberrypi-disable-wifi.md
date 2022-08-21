# Raspberry Pi Disable Wifi

To disable the internal wifi on the raspbery pi: 

- edit /boot/config.txt
- add the line `dtoverlay=disable-wifi`  

to disable bluetooth you can and the line `dtoverlay=disable-bt`

reboot for change to take effect.
