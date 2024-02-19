#!/usr/bin/python3

import json
 
# Data to be written
dictionary = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}

print(dictionary)
print(type(dictionary))
# Serializing json (Serializing)
json_object = json.dumps(dictionary, indent=4)

print(json_object)
print(type(json_object))

# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)

dictionary = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 9.6,
    "phonenumber": "9976770500"
}

# we can just use dumps (Serializing)
with open("sample.json", "w") as outfile:
    json.dump(dictionary, outfile)


# read data from json file(Deserialization)
with open("sample.json", "r") as outfile:
    outfile = json.loads(json_object)
    print(outfile)
    print(type(outfile))