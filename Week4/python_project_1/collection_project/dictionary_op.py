trainee = {'fname': 'Adam', 'lname': 'Smith', 'group': 'Eng-94', 'year': [2020, 2021]}
# or
trainee = dict(fname='Adam', lname='Smith', group='Eng-94', year=[2020, 2021])

print("fname:", trainee['fname'])
print("lname:", trainee['lname'])
print("group:", trainee['group'])
print("year:", trainee['year'][1])

trainee['fname'] = 'Mark'
print("fname:", trainee['fname'])

print("\nPrinting using a loop")
for i in trainee:
    print(i)

print("\nPrinting keys using a loop with .keys()")
for j in trainee.keys():
    print(j)

print("\nPrinting keys using a loop with .values()")
for k in trainee.values():
    print(k)

print("\nPrinting keys and values using a loop with .items()")
for key, value in trainee.items():
    print(key, ':', value)

print("\nPrinting keys and values using a loop - method 2")
for key in trainee:
    print(key, ':', trainee[key])
