#!/usr/bin/env python

from collections import Counter
import fileinput

boxes = list()
twice_count = 0
thrice_count = 0

class Box:
    def __init__(self, id):
        self.id = id
        self.twice = False
        self.thrice = False

        character_counts = Counter(id)

        if 2 in character_counts.values():
            self.twice = True

        if 3 in character_counts.values():
            self.thrice = True

for box_id in fileinput.input():
    boxes.append(Box(box_id))

for box in boxes:
    if box.twice:
        twice_count += 1
    if box.thrice:
        thrice_count += 1

print "Twice_count: ", twice_count
print "Thrice_count: ", thrice_count
print "Checksum: ", twice_count * thrice_count

