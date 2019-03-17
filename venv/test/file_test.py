import json

# with open("/Users/kaze/project/py-narai/venv/class_test.py") as file_object:
#     contents = file_object.read()
#     print(contents)

# mode = r读w写a附加r+读写
file = open('/Users/kaze/project/py-narai/venv/test/class_test.py', mode='r')
# for line in file:
#     print(line.rstrip())

file = open('/Users/kaze/project/py-narai/venv/write.txt', mode='w')
file.write("Hello World\n")

file = open('/Users/kaze/project/py-narai/venv/write.txt', mode='a')
file.write("Hello World")

# file = open('/Users/kaze/project/py-narai/venv/username.txt', mode='w')
# json.dump('name', file)

file = open('/Users/kaze/project/py-narai/venv/username.txt', mode='r')
name = json.load(file)
print(name)
