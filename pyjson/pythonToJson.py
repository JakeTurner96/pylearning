import json

pythonObject = {
    "Name": "Jake",
    "Age": 23,
    "Gender": "Male",
    "DoB": "16/08/1996",
    "Hobbies": ["Skateboarding", "Cycling", "Gaming"]
}

with open("json_data.json", "w")as writeFile:
    json.dump(pythonObject, writeFile)