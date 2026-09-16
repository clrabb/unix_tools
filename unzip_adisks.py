#!/usr/bin/python3

from os import listdir, rename, system
from os.path import isfile, join
import zipfile
import re
import sys
import filetype



def normalize_name(file_name):
    lc_name = file_name.lower()
    no_spaces_name = re.sub( "[\s-]+", "_", lc_name )
    return no_spaces_name


def normalize_files( extension ):
    for f in listdir("."):
        f_lc = f.lower()
        if not f_lc.endswith( extension ):
            continue

        old_name = f
        normalized_name = normalize_name(old_name)
        rename( old_name, normalized_name )
        print( f"renamed {old_name} to {normalized_name}", file=sys.stderr )

    return

def unzip_files( extension ):
    for f in listdir("."):
        if not f.lower().endswith( extension ):
            continue

        print( f"unzipping {f}", file=sys.stderr )
        with zipfile.ZipFile( f ) as z_obj:
            z_obj.extractall( path="." )

    return

def uncompress_files( extension ):
    for f in listdir("."):
        if not f.lower().endswith( extension ):
            continue

        print( f"gunzipping {f}", file=sys.stderr )
        system( f"gunzip --suffix {extension} {f}" )

    return
    
    
def main():
    normalize_files( ".zip" )
    uncompress_files()


    unzip_files( ".zip" )
    uncompress_files( ".adz" )
    normalize_files( ".adf" )

main()

