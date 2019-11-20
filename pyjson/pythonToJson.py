import json

pythonObject = {
    "Name": "Jake",
    "Age": 23
}
print(type(pythonObject))

jsonData = json.dumps(pythonObject)
print(type(jsonData))
