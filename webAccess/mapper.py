#! /usr/bin/env python
import sys
import re

# def mapper():
parts = [ r'(?P<host>\S+)',
          r'(?P<client>\S+)',
          r'(?P<user>\S+)',
          r'\[(?P<time>.+)\]',
          r'"(?P<request>.+)"',
          r'(?P<status>[0-9]+)',
          r'(?P<size>\S+)',
]

pattern = re.compile(r'\s+'.join(parts)+r'\s*\Z')

for line in sys.stdin:
    m = pattern.match(line)
    if not m:
        continue
    host, ignore, user, date, request, status, size = m.groups()
    print "{0}\t{1}".format(request,1)

# test_txt = "10.223.157.186 - - [15/Jul/2009:15:50:36 -0700] \"GET /assets/img/dummy/secondary-news-4.jpg HTTP/1.1\" 200 5766"
#
# def main():
#     import StringIO
#     sys.stdin = StringIO.StringIO(test_txt)
#     mapper()
#     sys.stdin = sys.__stdin__
#
# main()