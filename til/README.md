
How I quickly find stuff in this repo via the header:

`alias til='cat /path/to/til/.search | fzf -d "," --with-nth 1 | cat /path/to/til/$(awk -F, {"print \$2"})'`

 ---
