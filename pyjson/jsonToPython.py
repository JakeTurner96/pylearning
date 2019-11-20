import json


jsonData = '{"Name":"Jake", "Age":23}'
print(type(jsonData))

pythonObject = json.loads(jsonData)
print(type(pythonObject))