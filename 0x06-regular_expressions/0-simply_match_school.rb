#!/usr/bin/env ruby
# ruby script that scans '/School/' pattern in an argument
pattern = /School/
puts ARGV[0].scan(pattern).join