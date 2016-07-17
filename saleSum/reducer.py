#! /usr/bin/env python
import sys

oldKey = None
saleSum = 0
saleMax = 0
totalNum = 0
totalValue = 0

for line in sys.stdin:
    data_mapped = line.strip().split('\t')
    if len(data_mapped) != 2:
        continue
    thiskey, thisValue = data_mapped

    if oldKey and oldKey != thiskey:
        print oldKey,'\t',saleSum,'\t',saleMax
        oldKey = thiskey
        totalValue += saleSum
        saleSum = 0
        saleMax = 0
    oldKey = thiskey
    saleSum = saleSum + float(thisValue)
    saleMax = max(saleMax,float(thisValue))
    totalNum +=1

if oldKey != None:
    print oldKey,'\t',saleSum,'\t',saleMax
    totalValue += saleSum
    print "The summary is:",totalNum,'\t',totalValue