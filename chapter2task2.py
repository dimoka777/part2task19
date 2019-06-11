n = eval(input("Please enter quantity of students: "))
k = eval(input("Please enter quantity of apples: "))
result = k // n
left = k % n
if left == 1:
    apple = "apple"
else:
    apple = "apples"

print("Each student took", result, ".", left, apple, "left.")