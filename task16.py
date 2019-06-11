input_string = input("Enter a list element separated by space: ")
list = input_string.split()
list = [int(i) for i in list]
for num in list:

    # checking condition
    if num % 2 == 0:
        print(num, end=" ")

