#!/usr/bin/python3

import sys
import hashlib
from os import listdir

def gen_hashes():
    for f in listdir("."):
        if not f.endswith(".adf"):
            continue

        with open(f,"rb") as fp:
            data = fp.read()
            disk_hash = hashlib.md5(data)
            digest = disk_hash.hexdigest()
            print( f"{digest}\t{f}" )

    return

def main():
    gen_hashes()

main()
