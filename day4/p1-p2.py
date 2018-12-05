#!/usr/bin/env python

import fileinput
from datetime import datetime
from collections import defaultdict

## Input data
# [1518-05-05 00:04] Guard #1889 begins shift
# [1518-05-05 00:20] falls asleep
# [1518-05-05 00:26] wakes up

# All times are 00:00 - 00:59 each day

# Date format:
## datetime_object = datetime.strptime('[1518-05-05 00:26]', '[%Y-%m-%d %H:%M]')

# Important fields:
## $1 + $2 = timestamp
## $4 = [ guard.id | asleep | up ]

# events:
## #<integer> : new guard on shift, awake
## asleep:  current guard asleep
## up: current guard awake

# Output:
# Find the guard with the most minutes asleep
# What minute does the guard spend asleep the most?

class Guard:
    def __init__(self, id):
        self.id = id
        self.asleep_minutes_total = 0
        self.asleep_minutes = defaultdict(int)
        self.sleeping = False
        self.sleepstart = None

    def asleep(self, timestamp):
        if self.sleeping == False:
            self.sleeping = True
            self.sleepstart = timestamp

    def awake(self, timestamp):
        if self.sleeping == True:
            self.sleeping = False
            self.sleep_minutes = int((timestamp - self.sleepstart).total_seconds() / 60)
            self.asleep_minutes_total += self.sleep_minutes
            for minute in range(self.sleepstart.minute, self.sleepstart.minute + self.sleep_minutes):
                self.asleep_minutes[minute % 60] += 1

    def sleepiest_minute(self):
        max_sleep_count = 0
        max_sleep_minute = None

        for minute in self.asleep_minutes:
            if self.asleep_minutes[minute] > max_sleep_count:
                max_sleep_minute = minute
                max_sleep_count = self.asleep_minutes[minute]

        return max_sleep_minute, max_sleep_count


events = {}
guards = {}

for input_string in fileinput.input():
    string_split = input_string.split()
    timestamp = datetime.strptime(string_split[0] + ' ' + string_split[1], '[%Y-%m-%d %H:%M]')
    event = string_split[3]
    events[timestamp] = event

id = None
for timestamp in sorted(events):
    #print timestamp, ":", events[timestamp]
    if events[timestamp] == "asleep":
        guards[id].asleep(timestamp)
    elif events[timestamp] == "up":
        guards[id].awake(timestamp)
    else:
        id = events[timestamp].replace('#', '')
        if id not in guards:
            guards[id] = Guard(id)
        else:
            guards[id].awake(timestamp)


max_sleep = 0
sleepiest_guard = None
for id in guards:
    print "Guard ", guards[id].id, " slept for ", guards[id].asleep_minutes_total, " minutes"
    if guards[id].asleep_minutes_total > max_sleep:
        sleepiest_guard = id
        max_sleep = guards[id].asleep_minutes_total

(sleepiest_minute, sleep_minute_count) = guards[sleepiest_guard].sleepiest_minute()

# Part 1 find the guard who slept the longest and the minute they slept the most
print "Sleepiest guard was ", sleepiest_guard, " who slept for ", max_sleep, " minutes"
print "Sleepyhead guard slept ", sleep_minute_count, " times at minute ", sleepiest_minute
print "Part1 answer is ", int(sleepiest_guard) * sleepiest_minute

# Find guard with the most sleeps on the same minute
max_sleep_count = 0
most_sleepiest_minute = None
most_sleepiest_guard = None
for id in guards:
    (sleepiest_minute, sleep_minute_count) = guards[id].sleepiest_minute()
    if sleep_minute_count > max_sleep_count:
        most_sleepiest_minute = sleepiest_minute
        most_sleepiest_guard = id
        max_sleep_count = sleep_minute_count

print "Guard ", id, " slept ", max_sleep_count, " times on minute ", most_sleepiest_minute
print "Part2 answer is ", int(most_sleepiest_guard) * most_sleepiest_minute


