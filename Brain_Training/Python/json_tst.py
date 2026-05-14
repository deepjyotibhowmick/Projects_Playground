book = {}
book["Deep"] = {
    "name": "Deep",
    "address": "Mahesh Colony",
    "Mob": 588103
}

book["Moni"] = {
    "name": "Moni",
    "address": "Kukrakhupi",
    "Mob": 143143
}

# print(book["Moni"])
# print(book["Moni"].values())

import json
s= json.dumps(book)
# print(s)
json_file= open("test_json.txt", "w")
json_file.write(s)
json_file.close()

print(book["Deep"]["Mob"])
json_r=open("test_json.txt", "r")

for reads in json_r:
    print(reads)

json_r.close()
