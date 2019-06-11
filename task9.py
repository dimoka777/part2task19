counter = 0
for x in range(10):
  number = eval(input("Enter a number: "))
  counter = counter + number
print(counter)

number1 = []
for x in range(10):
    digit = eval(input("Enter a number: "))
    number1.insert(x,digit)
print(sum(number1))
