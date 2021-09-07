import json

with open("trainee.json", "r") as f:
    trainee = json.load(f)
    print(trainee)

for key, value in trainee.items():
    print(f"{key} = {value}")
    