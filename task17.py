input_string = input("Enter a list element separated by space: ")
list = input_string.split()
list = [int(i) for i in list]
for i in list:
    j = 1
    if list[i] == j:
        j += 1
    else:
        print(j)
