# 이미 내용이 입력되어 있는 test.txt가 있다. 이 파일의 내용 중 'java'라는 문자열을 'python'으로 바꾸어 저장

with open("test.txt", 'r') as f:
    body = f.read()

newBody = body.replace('java', 'python')

with open("test.txt", 'w') as f:
    f.write(newBody)
    f.write('\n')