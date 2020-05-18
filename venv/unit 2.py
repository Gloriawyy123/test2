import json
# numbers = [1]
filename = 'jsontest.json'
with open(filename) as f_obj:
    a = json.load(f_obj)
print(a)
