"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
a={}
for i in calls:
    s,r,d,t=i
    if s not in a.keys():
        a[s]= int(t)
    else:
        a[s] += int(t)
    if r not in a.keys():
        a[r]= int(t)
    else:
        a[r] += int(t)

longest = max(a.values())

for i in a.keys():
    if a[i] == longest:
        ans = i

print("{} spent the longest time, {} seconds, on the phone during \
September 2016.".format(ans,longest))

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

