weight = eval(input("Enter Your weight: "))
for i in range(15):
    weight_moon = weight * 0.165
    print("Your weight for the", i+1, "year is", weight_moon)
    weight += 1