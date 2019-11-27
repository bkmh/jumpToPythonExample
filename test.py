marks = [90, 25, 67, 45, 80]

number = 0

for mark in marks:
    number = number + 1

    if mark >= 60:
        print("Number %d Student is Success" %number)
    else:
        print("Number %d Student is fail" %number)
