#! /usr/bin/env python
import sys

oldKey = None
hitSum = 0
hitMax = 0
MaxKey = None

for line in sys.stdin:
    data_mapped = line.strip().split('\t')
    if len(data_mapped) != 2:
        continue
    thisKey,thisValue = data_mapped

    if oldKey and thisKey != oldKey:
        print "{0}\t{1}".format(oldKey,hitSum)

        if hitSum > hitMax:
            hitMax = hitSum
            MaxKey = oldKey

        oldKey = thisKey
        hitSum = 0

    oldKey = thisKey
    hitSum += float(thisValue)
if oldKey != None:

    if hitSum > hitMax:
        hitMax = hitSum
        MaxKey = oldKey

    print "{0}\t{1}".format(oldKey,hitSum)
    print "The popular is {0}\t{1}".format(MaxKey,hitMax)