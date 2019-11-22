import json

pythonObject = {
    "Name": "Jake",
    "Age": 23,
    "Gender": "Male",
    "DoB": "16/08/1996",
    "Hobbies": ["Skateboarding", "Cycling", "Gaming"]
}

string = json.dumps(pythonObject)

print(string)