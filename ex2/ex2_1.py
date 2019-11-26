result = {'kor':80, 'eng':75, 'math':55}

sum = 0

for val in result.values():
    sum = sum + val


print('sum : ' + str(sum))
print('average : ' + str(sum / len(result.keys())))

