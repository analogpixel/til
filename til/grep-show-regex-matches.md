# Grep show regex matches

If you just want to show matching regex patterns in a file:

`grep -Eio "\w+"` : this would find every word(\w)  and print it out.
`grep -Eio "(?:[0-9]{1,3}\.){3}[0-9]{1,3}"` : find every IP address in a file

# options
- `E` : use extended grep (egrep)
- `i` : ignore case
- `o` : only print matching section
