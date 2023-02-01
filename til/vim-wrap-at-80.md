# Vim wrap text at 80 characters

To wrap text at 80 characters for all files that end in wiki:

`au BufRead,BufNewFile *.wiki setlocal textwidth=80`

you can also select a block of text and type `gq` to format
existing blocks to the 80char limit.
