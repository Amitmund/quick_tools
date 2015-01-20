#!/usr/bin/perl

# Usage: command [hostname1 hostname2 ...]

foreach my $arg (@ARGV){
	print "$arg\n";
	system("host $arg | egrep -o \"(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\"");
}
