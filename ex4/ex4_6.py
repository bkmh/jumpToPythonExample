# 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성
# 단, 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.
user_input = input("Input Your Contents:")

with open("test.txt", 'a') as f:
    f.write(user_input)
    f.write('\n')
