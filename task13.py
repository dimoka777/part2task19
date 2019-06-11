line = input("Enter a line: ")
split = line.split(" ")
split[0], split[1] = split[1], split[0]
str = ' '.join(split)
print(str)