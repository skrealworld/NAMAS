#!/usr/bin/perl

$last = "";
$thisone = "";
%done = {};
$file = $ARGV[0];
open FILE, $file or die;
while (<FILE>) {
    s/\s$//g;
    $temp = $_;

    $temp =~ s/\.//g;
    $temp =~ s/\,//g;
    $temp =~ s/\s//g;

    $thisone = $_;
    if ($last ne $thisone && !exists $done{$temp}) {
	print $thisone."\n";
    }
    $done{$temp} = 1;
    $last = $thisone;
}
close FILE;
