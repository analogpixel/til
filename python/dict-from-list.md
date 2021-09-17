# Converting a list to a dict

if you just use `data = dict.fromkeys(['a','b'],[])` both entries will point to the same list.  to get
python to point to different lists you need to use dicitonary comprehension  `data = {k: [] for k in range(2)}`

