import jmespath
persons = {
    "persons": [
        {"name": "erik", "age": 38},
        {"name": "john", "age": 45},
        {"name": "rob", "age": 14}
    ]
}


age=jmespath.search('persons[*].age', persons)

print(age)
