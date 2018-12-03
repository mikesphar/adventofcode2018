#!/usr/bin/env python

import fileinput

ids = []
found = False

def remove_char_at_index(string, index):
    return string[:index] + string[index+1:]


def find_one_match(string, strings):
    for compare_string in strings:
        if string == compare_string:
            next
        else:
            count = 0
            diff_index = None

            for char_index, (a, b) in enumerate(zip(string, compare_string)):
                if a != b:
                    count += 1
                    diff_index = char_index
                if count > 1:
                    break

            if count == 1:
                return True, diff_index

    return False, None


for id in fileinput.input():
    ids.append(id.rstrip())

for id in ids:
    result, index = find_one_match(id, ids)

    if result:
        print "Found it! ", remove_char_at_index(id, index)
        break

