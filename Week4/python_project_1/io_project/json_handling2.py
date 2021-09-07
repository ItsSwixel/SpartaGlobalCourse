import json

with open("trainee.json", "r") as f:
    trainee = json.load(f)

print(trainee)

for key, value in trainee.items():
    print(f"{key} = {value}")

trainee['year'] = [2020, 2021, 2022]
with open('trainee.json', 'w') as f:
    json.dump(trainee, f, indent=4)
