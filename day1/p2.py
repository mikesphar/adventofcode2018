#!/usr/bin/env python

import fileinput

frequency = 0
frequencies = {frequency}
foundit = False

while foundit == False:
    for change in fileinput.input():
        frequency += int(change)
        if frequency in frequencies:
            foundit = True
            print "Found it! ", frequency
            break
        else:
            frequencies.add(frequency)

