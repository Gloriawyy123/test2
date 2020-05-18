import json


json_str = {}
js = {}
for i in range(8):
    json_str[i] = i+1

for i in range(7):
    js[i] = json_str
print(json_str)
with open('test.json', 'w') as j:
    json.dump(js, j)