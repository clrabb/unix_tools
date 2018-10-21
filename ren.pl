#!/usr/bin/perl
use strict;
use warnings;

opendir( DIR, "." ) or die "Cannot open directory: $!\n";
my @files = readdir( DIR );
foreach my $file ( @files )
{
    my $lower = lc( $file );
    if ( $lower ne $file )
    {
        print "Renaming $file to $lower\n";
        rename $file, $lower;
    }
}

closedir DIR;
