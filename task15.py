n = eval(input("Enter a number: "))
result = []
for i in range(n + 1):
    j = 1
    while j * j <= i:
        if j * j == i:
            result.append(i)
        j = j + 1
    i = i + 1

str = ' '.join(str(e) for e in result)
print(str)