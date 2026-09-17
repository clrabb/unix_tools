#!/usr/bin/python3

from os import listdir, rename, system, rename
from os.path import isfile, join, splitext
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
        print( f"renamed {old_name} to {normalized_name}" )

    return

def gunzip_file( file_name ):
    try:
        parts = splitext( file_name )
        ext = parts[ 1 ]
        system( f"gunzip --suffix {ext} {file_name}" )
    except Exception as e:
        print( e, file=sys.stderr )
        print( f"Hit an error gunzipping file {file_name}", file=sys.stderr )


def unzip_file( file_name ):
    try:
        print( f"Unzipping file {file_name}" )
        with zipfile.ZipFile( file_name ) as z_obj:
            z_obj.extractall( path="." )
    except Exception as e:
        print( e, file=sys.stderr )
        print( f"Hit an error unzipping file {file_name}", file=sys.stderr )



def uncompress_files():
    for f in listdir("."):
        kind = filetype.guess( f )
        if not kind:
            continue

        if kind.extension == "gz":
            gunzip_file( f ) 
        if kind.extension == "zip":
           unzip_file( f )

    return

def uncompress_adz_files():
    for f in listdir("."):
        parts = splitext( f )
        fname = parts[ 0 ]
        fext  = parts[ 1 ]
        if fext.lower() == ".adz":
            gunzip_file( f )
            rename( fname, f"{fname}.adf" )
    
    
def main():
    normalize_files( ".zip" )
    normalize_files( ".gz"  )
    normalize_files( ".gzip" )
    uncompress_files()
    normalize_files( ".adz" )
    uncompress_adz_files()
    normalize_files( ".adf" )



    normalize_files( ".adf" )

main()

