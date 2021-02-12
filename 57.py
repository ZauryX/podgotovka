import sys
import json

diction = {
    "even": {},
    "odd": {}
}
for line in sys.stdin:
    list = line.rstrip('\n').split("/")
    if int(list[1]) % 2 == 0:
        diction["even"][list[0]] = list[1]
    else:
        diction["odd"][list[0]] = list[1]
with open('one.json', 'w') as file:
    json.dump(diction, file)
