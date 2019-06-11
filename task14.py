str = input("Enter a string: ")
position_first = str.find("f")
position_last = str.rfind("f")
if position_last == position_first:
    if position_first == -1 and position_last == -1:
        print()
    else:
        print(position_first)
else:
    print(position_first, position_last)