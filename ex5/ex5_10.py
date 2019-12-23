import os

# target directory : ../../

print(os.getcwd())

os.chdir('../../')

f = os.popen('ls')

print(f.read())


