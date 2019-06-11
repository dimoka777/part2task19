age = eval(input("Enter Your age: "))
if age % 2 == 0:
    for i in range(age):
        if i % 2 == 0:
            print(i, end = " ")
else:
    for i in range(age):
        if i % 2 == 1:
            print(i, end = " ")