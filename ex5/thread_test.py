import time

def long_task():
    for i in range(5):
        time.sleep(1)
        print('working:%s\n' % i)

print("START")
print(time.ctime())

for i in range(5):
    long_task()

print("End")
print(time.ctime())
