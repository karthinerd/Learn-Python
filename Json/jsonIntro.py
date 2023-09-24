# JSON - syntax for Storing and Exchanging Data & is text, written with JavaScript object notation

import json

# JSON to Python

json_data = '{"name":"karthi","age":"21","gender":"Male"}'

convert_python = json.loads(json_data)

#  result is a Python dictionary:

print(convert_python["name"])


# Python to JSON

dict_obj = {"name": "karthi", "age": 21, "gender": "Male", "adult": True}

convert_json = json.dumps(dict_obj)

print(convert_json)

# You can convert Python objects of the following types, into JSON strings:

# dict
# list
# tuple
# string
# int
# float
# True
# False
# None

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}],
}

# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4, separators=(". ", " = "), sort_keys=True))
