#!/usr/bin/env python

import os
import glob

out = open("README.md", "w")

groups = {}
for f in glob.glob("til/*.md"):
    first_line = open(f, "r").readlines()[0][1:].strip()
    category = first_line.split()[0].lower()
    groups.setdefault( category, [] ).append({"file": f, "title": first_line})
    #data[d].append( [d,f,first_line ] ) 

out.write("# TOC\n")
for category in sorted(groups.keys()):
    out.write("## {}\n".format(category.capitalize() ) )
    for item in groups[category]:
        out.write("- [{}]({})\n".format(item['title'], item['file'] ))
out.write( "---\n" )

quit()

for d in sorted(data.keys()):
    out.write("### {}\n\n".format(d))
    for e in sorted(data[d]):
        out.write("- [{}]({})\n".format(e[2], e[1]) ) 
    out.write("\n\n")
