FIRST_NUM = int(input("Please enter your first number: "))
SECOND_NUM = int(input("Please enter your second number: "))

print(FIRST_NUM, "+", SECOND_NUM, "=", (FIRST_NUM+SECOND_NUM))
print(FIRST_NUM, "-", SECOND_NUM, "=", (FIRST_NUM-SECOND_NUM))
print(FIRST_NUM, "*", SECOND_NUM, "=", (FIRST_NUM*SECOND_NUM))
print(FIRST_NUM, "/", SECOND_NUM, "=", (FIRST_NUM/SECOND_NUM))

f = open("results.txt", "w")
f.write(str(FIRST_NUM+SECOND_NUM) + "\n")
f.write(str(FIRST_NUM-SECOND_NUM) + "\n")
f.write(str(FIRST_NUM*SECOND_NUM) + "\n")
f.write(str(FIRST_NUM/SECOND_NUM) + "\n")
f.close()
