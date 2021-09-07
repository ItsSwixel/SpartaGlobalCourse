trainee = ("Adam", "Smith", "Eng-94", 2021)
print(trainee)

print("\nThis is the tuple using a for loop")
for i in trainee:
    print(i)

i = 0

print("\nThis is the tuple using while")
while i < len(trainee):
    print(trainee[i])
    i += 1

print("\nThis is to extract the values")
fname = trainee[0]
lname = trainee[1]
group = trainee[2]
year = trainee[3]

print("First name:", fname)
print("Last name:", lname)
print("Group:", group)
print("Year:", year)

print("\nThis is to extract the values using a new method")
fname, lname, group, year = trainee

print("First name:", fname)
print("Last name:", lname)
print("Group:", group)
print("Year:", year)