import json

Dict= {
    "people":[
        {
        "name":"govinda",
        "age":28,
        "height":5.6
        },
        {
            "name":"rohan",
            "age":29,
            "height":6
        },
        {
            "name":"alice",
            "age":30,
            "height":6.1
        },
    ]
}

json_string=json.dumps(Dict,indent=4)
with open("my_data.json",'w') as f:
    f.write(json_string)