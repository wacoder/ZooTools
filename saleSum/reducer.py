#! /usr/bin/env python
import sys

oldKey = None
saleSum = 0
saleMax = 0

for line in sys.stdin:
    data_mapped = line.strip().split('\t')
    if len(data_mapped) != 2:
        continue
    thiskey, thisValue = data_mapped

    if oldKey and oldKey != thiskey:
        print oldKey,'\t',saleSum,'\t',saleMax
        oldKey = thiskey
        saleSum = 0
        saleMax = 0
    oldKey = thiskey
    saleSum = saleSum + float(thisValue)
    saleMax = max(saleMax,thisValue)

if oldKey != None:
    print oldKey,'\t',saleSum,'\t',saleMax