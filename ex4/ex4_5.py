# test.txt라는 파일에 "Life is too short" 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램
f1 = open("test.txt", 'w')
f1.write("Life is too short")

# Stream이 open 된 상태에서 다시 다른 Stream으로 접근하기 때문에
# Write를 수행한 Stream을 Close해야 함
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())