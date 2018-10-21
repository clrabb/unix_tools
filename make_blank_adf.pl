#!/usr/bin/perl
use strict;
use warnings;
use File::Copy;

my $TEMPLATE = "/Users/crabb/bin/unix_tools/empty.adf";

my $num = 0;
while ( 1 )
{
    print "How many empty disks?";
    $num = <STDIN>;
    chomp $num;
    last if $num =~ /^\d+$/; 
}

print "Number is $num\n";

for ( my $i = 0; $i < $num; ++$i )
{
    my $filename = "empty" .sprintf( "%04d", $i ) . ".adf";
    print "Making disk: $filename\n";
    copy( $TEMPLATE, "./$filename" ) or die "Cannot copy file $TEMPLATE to new file $filename: $!\n";
}






