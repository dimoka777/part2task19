a = eval(input("Enter a number: "))
b = eval(input("Enter a number: "))
c = eval(input("Enter a number: "))

first_room = (a // 2) + (a % 2)
second_room = (b // 2) + (a % 2)
third_room = (c // 2) + (c % 2)

result = first_room + second_room + third_room
print(result)
