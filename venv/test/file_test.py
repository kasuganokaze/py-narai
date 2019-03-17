import json

# with open("/Users/kaze/project/py-narai/venv/class_test.py") as file_object:
#     contents = file_object.read()
#     print(contents)

# mode = r读w写a附加r+读写w+读写a+读写附加
with open('/Users/kaze/project/py-narai/venv/test/class_test.py', mode='r') as file:
    for line in file:
        print(line.rstrip())

with open('/Users/kaze/project/py-narai/venv/write.txt', mode='w') as file:
    file.write("Hello World\n")

with open('/Users/kaze/project/py-narai/venv/write.txt', mode='a') as file:
    file.write("Hello World")

# file = open('/Users/kaze/project/py-narai/venv/username.txt', mode='w')
# json.dump('name', file)

with open('/Users/kaze/project/py-narai/venv/username.txt', mode='r') as file:
    name = json.load(file)
    print(name)
