marks = [90, 25, 67, 45, 80]

for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("Number %d Student is Success" % (number+1))
