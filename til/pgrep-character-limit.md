# Pgrep character Limit

`pgrep -fa needle`  will fail if `needle` is 4001 characters in.  Also pgrep
will truncate the output of what it finds to 4000 characters.

pgrep has a 4000 character file limit, and after that it just chops it off.  
Not so much fun when you are trying to look at a long java process name
that has a bunch of -D flags on it.

https://gitlab.com/procps-ng/procps/-/issues/86

---
#pgrep #linux #bug
