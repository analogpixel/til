# Bash range expansion with xargs and ssh

this will connect to each server serially and run the command `ls -l /home/server/etc`:

`echo server-app-{01..09} | tr ' ' '\0' | xargs -0 -I {} ssh {} ls -l /home/server/etc`

you can also use -n1 on macos to parse a list of space seperated values:

`echo server-app-{01..9} | xargs -n1 -I {} ssh {} ls -l /home/server/etc
