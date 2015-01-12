#!/usr/bin/python

import fileinput
import math

for line in fileinput.input():
    entropy = 0
    entries = map(float, line.strip().split())
    count = sum(entries)
    for entry in entries:
        entropy -= entry/count*math.log(entry/count,2)
    print entropy
