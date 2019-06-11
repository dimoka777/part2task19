hours = eval(input("Please enter hour: "))
minutes = eval(input("Please enter minute: "))
seconds = eval(input("Please enter second: "))

hours2 = eval(input("Please enter hour: "))
minutes2 = eval(input("Please enter minute: "))
seconds2 = eval(input("Please enter second: "))

if seconds > seconds2:
    seconds2 = seconds2 + 60
    minutes2 = minutes2 - 1
total_seconds = seconds2 - seconds
if minutes > minutes2:
    minutes2 = minutes2 + 60
    hours2 = hours2 - 1
total_minutes = minutes2 - minutes
if hours > hours2:
    hours2 = hours2 + 24
total_hours = hours2 - hours

result = (total_hours * 60 * 60) + (total_minutes * 60) + total_seconds
print(result)
