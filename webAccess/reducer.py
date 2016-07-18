#! /usr/bin/env python
import sys

oldKey = None
hitSum = 0

for line in sys.stdin:
    data_mapped = line.strip().split('\t')
    if len(data_mapped) != 2:
        continue
    thisKey,thisValue = data_mapped
    if oldKey and thisKey != oldKey:
        print "{0}\t{1}".format(oldKey,hitSum)
        oldKey = thisKey
        hitSum = 0
    oldKey = thisKey
    hitSum += float(thisValue)
if oldKey != None:
    print "{0}\t{1}".format(oldKey,hitSum)