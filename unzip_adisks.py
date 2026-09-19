#!/usr/bin/python3

from os import listdir, rename, system 
from os.path import isfile, join, splitext
import zipfile
import re
import sys
import filetype
from adisk_utils import normalize_name, normalize_files


def gunzip_file( file_name ):
    try:
        parts = splitext( file_name )
        ext = parts[ 1 ]
        system( f"yes | gunzip --suffix {ext} {file_name}" )
    except Exception as e:
        print( e, file=sys.stderr )
        print( f"Hit an error gunzipping file {file_name}" )


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

        if not isfile( f ):
            continue

        kind = filetype.guess( f )
        if not kind:
            continue

        if kind.extension == "gz":
            gunzip_file( f ) 
        if kind.extension == "zip":
            unzip_file( f )

    return

def rn_file( old_name, new_name ):
    try:
        rename( old_name, new_name )
    except Exception as e:
        print( e, file=sys.stderr )
        print( f"Hit an error renaming {old_name} to {new_name}", file=sys.stderr )
        
def uncompress_adz_files():
    for f in listdir("."):
        parts = splitext( f )
        fname = parts[ 0 ]
        fext  = parts[ 1 ]
        if fext.lower() == ".adz":
            gunzip_file( f )
            rn_file( fname, f"{fname}.adf" )
    
def main():
    normalize_files( ".zip" )
    normalize_files( ".gz"  )
    normalize_files( ".gzip" )
    uncompress_files()
    normalize_files( ".adz" )
    uncompress_adz_files()
    normalize_files( ".adf" )

main()

