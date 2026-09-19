#!/usr/bin/python3

import sys
import hashlib
from os import listdir

def gen_hash( file_name ):
    digest = ""
    with open(file_name,"rb") as fp:
        data = fp.read()
        disk_hash = hashlib.md5(data)
        digest = disk_hash.hexdigest()

    return digest

def create_hash_map( disk_map ):
    num_disks = 0
    for file_name in listdir("."):
        if not file_name.endswith(".adf"):
            continue

        if num_disks % 100 == 0:
            print( f"Disks examined: {num_disks}", flush=True )

        num_disks += 1
        disk_hash = gen_hash( file_name )
        
        if disk_hash in disk_map:
            disk_names = disk_map[ disk_hash ]
            disk_names.append( file_name )
        else:
            disk_map[ disk_hash ] = [ file_name ]

def main():
    disk_map = {}
    create_hash_map( disk_map )

    for disk_hash in disk_map:
        names = disk_map[ disk_hash ]
        if len( names ) > 1:
            for name in names:
                print( f"{disk_hash}\t{name}", flush=True )

main()
