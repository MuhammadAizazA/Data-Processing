import json
def json_read():
    json_string = '{"name": "erik", "age": 38, "married": true}'
    person = json.loads(json_string)
    print(person['name'], 'is', person['age'], 'years old')
    print(person)

    
if __name__=='__main__':
    json_read()