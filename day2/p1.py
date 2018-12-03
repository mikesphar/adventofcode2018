#!/usr/bin/env python

from collections import Counter
import fileinput

boxes = list()

class Box:
    twice = 0
    thrice = 0

    def __init__(self, id):
        self.id = id

        character_counts = Counter(id)

        if 2 in character_counts.values():
            Box.twice += 1

        if 3 in character_counts.values():
            Box.thrice += 1

for box_id in fileinput.input():
    boxes.append(Box(box_id))

print "Checksum: ", Box.twice * Box.thrice

