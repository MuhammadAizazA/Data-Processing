import json
def json_read():
    json_string = '{"name": "erik", "age": 38, "married": true}'
    person = json.loads(json_string)
    print(person['name'], 'is', person['age'], 'years old')
    print(person)

def write_json(data):
    with open("data/new_json_file.json","a") as f:
        json.dump(data,f)

if __name__=='__main__':
    json_read()
    with open("data/sample_json.json") as f:
        data=json.load(f)
        dict_data=dict(data)
        write_json(data)
        for index,key in enumerate(dict_data):
            for x in range(len(dict_data[key])):
                print(f"{index} {dict_data[key][x]}")
    