# Bash range expansion with xargs and ssh

for some reason xargs says it can work on a list of space separated values
but that is not the case for me on macos.  so convert the spaces to nulls, and 
have xargs work on that:

this will connect to each server serially and run the command `ls -l /home/server/etc`:

`echo server-app-{01..09} | tr ' ' '\0' | xargs -0 -I {} ssh {} ls -l /home/server/etc`


