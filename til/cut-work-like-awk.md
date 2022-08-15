# Cut space delimiter work like AWK

Awk is better than cut in every way except for column ranges.  So 
if you want the same sort of delimiter syntax that awk has you
can do this:  `tr -s ' ' | cut -d' ' -f1-4`   this will convert multiple
space down to 1 space, and then use space as a delimiter in cut.

---
#cut #awk #linux
