#!/usr/bin/env python

import os
import glob

out = open("README.md", "w")

data  = { k: [] for k in   [f.name for f in os.scandir('.') if f.is_dir() and f.name != ".git"]   }

for d in data.keys():
    for f in glob.glob("{}/*.md".format(d)):
        first_line = open(f, "r").readlines()[0][1:].strip()
        data[d].append( [d,f,first_line ] ) 

out.write("# TOC\n")
for d in sorted(data.keys()):
    out.write("* [{}](#{}]\n".format(d,d))

out.write( "---\n" )

for d in sorted(data.keys()):
    out.write("### {}\n\n".format(d))
    for e in data[d]:
        out.write("- [{}]({})\n".format(e[0], e[1]) ) 
    out.write("\n\n")
