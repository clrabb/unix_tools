#!/usr/bin/python3

import sys

lines = {}

for cnt, ln in enumerate( sys.stdin ):
    line = ln.strip()

    if line in lines:
        cnt = lines[ line ]
        cnt += 1
        lines[ line ] = cnt
    else:
        lines[ line ] = 1


for line in lines:
    cnt = lines[ line ]
    print( f"{cnt}\t{line}" )
