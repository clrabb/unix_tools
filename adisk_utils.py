#!/usr/bin/python3

import re 
from os import system, listdir, rename

def normalize_name(file_name):
    lc_name = file_name.lower()
    no_spaces_name = re.sub( "[\s-]+", "_", lc_name )
    only_letters_and_numbers = re.sub( "[^A-Za-z0-9_\.]", "_", no_spaces_name )
    dedup_underscores = re.sub( "_+","_", only_letters_and_numbers )
    normalized = re.sub( "\'", "", dedup_underscores )
    return normalized

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
