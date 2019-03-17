# with open("/Users/kaze/project/py-narai/venv/class_test.py") as file_object:
#     contents = file_object.read()
#     print(contents)

file = open('/Users/kaze/project/py-narai/venv/class_test.py')
# for line in file:
#     print(line.rstrip())
for line in file.readlines():
    print(line.rstrip())

print('1234' in 'dskh1234dvj')