import json
import requests


with open('two1.json') as file:
    f = file.read()
    data1 = json.loads(f)
    server = data1["server"]
    port = int(data1["port"])
r = requests.get("{}: {}".format(server, port))
data = r.json()

lis = []
for i in range(len(data["first"])):
    s = 0
    for j in range(3):
        s += data["first"][i][j] * data["second"][i][j]
    lis.append(format(s, ".3f"))
print(*lis)
