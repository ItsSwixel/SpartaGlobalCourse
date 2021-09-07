import json

trainee = {'fname': 'Adam', 'lname': 'Smith', 'group': {'G1': 'Eng-94', 'G2': 'Cyber2'}, 'year': [2020, 2021]}

print(trainee)

with open('trainee.json', 'w') as f:
    json.dump(trainee, f, indent=4)
