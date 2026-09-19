#!/usr/bin/python3

import re 
from os import system, listdir, rename

def normalize_name(file_name):
    lc_name = file_name.lower()
    no_spaces_name = re.sub( "[\s-]+", "_", lc_name )
    no_brackets_name = re.sub( "[^A-Za-z0-9_\.]", "_", no_spaces_name )
    no_apos_name = re.sub( "\'", "", no_brackets_name )
    return no_apos_name

def normalize_files( extension ):
    for f in listdir("."):
        f_lc = f.lower()
        if not f_lc.endswith( extension ):
            continue

        old_name = f
        normalized_name = normalize_name(old_name)
        rename( old_name, normalized_name )
        print( f"renamed {old_name} to {normalized_name}" )

    return
