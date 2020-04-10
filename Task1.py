"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

TextsPh=list(zip(*texts))
CallsPh=list(zip(*calls))

TextsPh = TextsPh[0] + TextsPh[1]
CallsPh = CallsPh[0] + CallsPh[1]
PhNumbers = TextsPh + CallsPh
PhNumbers = list(dict.fromkeys(PhNumbers))
print("There are {} different telephone numbers in the records.".format(len(PhNumbers)))

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are 570 different telephone numbers in the records."
"""
