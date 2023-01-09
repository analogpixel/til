# Javascript seconds since epoch

javascript returns epoch in miliseconds, so make sure
to convert to seconds (if that is what you're after):

`Math.round(Date.now() / 1000)`
