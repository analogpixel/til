#!/usr/bin/env python

import os
import glob

out = open("README.md", "w")

out.write("""
How I quickly find stuff in this repo via the header:

`alias til='cat /path/to/til/.search | fzf -d "," --with-nth 1 | cat /path/to/til/$(awk -F, {"print \$2"})'`

 """)

search_file = []
groups = {}
for f in glob.glob("til/*.md"):
    first_line = open(f, "r").readlines()[0][1:].strip()
    category = first_line.split()[0].lower()
    groups.setdefault( category, [] ).append({"file": f, "title": first_line})
    search_file.append("{},{}".format(first_line, f))
    #data[d].append( [d,f,first_line ] ) 

for category in sorted(groups.keys()):
    out.write("## {}\n".format(category.capitalize() ) )
    for item in groups[category]:
        out.write("- [{}]({})\n".format(item['title'], item['file'] ))
out.write( "---\n" )

with open(".search", "w") as f:
    f.write( "\n".join(search_file) )

os.system("git add .; git commit -am 'toc'; git push")
