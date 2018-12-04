#!/usr/bin/env python

import fileinput
import json
from pygrok import Grok
from collections import defaultdict

pattern = '#%{WORD:id} @ %{NUMBER:start_x:int},%{NUMBER:start_y:int}: %{NUMBER:width:int}x%{NUMBER:height:int}'

grok = Grok(pattern)

claims = []

class Claim:
    used_coords = defaultdict(int)
    reused_coords = 0

    def __init__(self, dict):
        (self.id, self.start_x, self.start_y, self.width, self.height) = dict["id"], dict["start_x"], dict["start_y"], dict["width"], dict["height"]
        for x in range(self.start_x, self.start_x + self.width):
            for y in range(self.start_y, self.start_y + self.height):
                Claim.used_coords[x,y] += 1
                if Claim.used_coords[x,y] == 2:
                    Claim.reused_coords += 1

for string in fileinput.input():
    claims.append(Claim(dict(grok.match(string.rstrip()))))

print "Number of overlapping coords: ", Claim.reused_coords

for claim in claims:
    overlapping = False
    for x in range(claim.start_x, claim.start_x + claim.width):
        if overlapping == True:
            break
        for y in range(claim.start_y, claim.start_y + claim.height):
            if Claim.used_coords[x,y] > 1:
                overlapping = True
                break
    if overlapping == False:
        print "Non-overlapping claim: ", claim.id
        break


