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
        (id, start_x, start_y, width, height) = dict["id"], dict["start_x"], dict["start_y"], dict["width"], dict["height"]
        for x in range(start_x, start_x + width):
            for y in range(start_y, start_y + height):
                Claim.used_coords[x,y] += 1
                if Claim.used_coords[x,y] == 2:
                    Claim.reused_coords += 1

for string in fileinput.input():
    claims.append(Claim(dict(grok.match(string.rstrip()))))

print Claim.reused_coords
