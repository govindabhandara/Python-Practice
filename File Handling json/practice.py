import json

with open('abc.json', 'rb') as file:
    for prefix, event, value in json.parse(file):
        print(f"prefix: {prefix}, event: {event}, value: {value}")