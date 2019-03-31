for i in range(3):
    if i == 2:
        print("我是最后一个")
    elif i == 1:
        print("我是倒数第二个")
    else:
        print(i)

try:
    1 / 0
except ZeroDivisionError as e:
    print(11)
    pass
else:
    print("没有抛异常")
finally:
    print(111)

# 字符串
name = 'ada lovelace'
name.title()
name.upper()
name.lower()
name.lstrip()
name.rstrip()

# 列表
array = ['1', '2', '3']
array.append('3')
array.insert(0, '4')
array.remove('4')
del array[0]
last = array.pop()
array.sort()
array.sort(reverse=True)
newArray = sorted(array)
len(newArray)
# 访问最后一个元素
print(newArray[-1])

numbers = list(range(10))
min(numbers)
max(numbers)
sum(numbers)
squares = [value ** 2 for value in range(1, 11)]
print(squares[0:3])
print(squares[-3:])
newSquares = squares[:]
print(newSquares)

# 元组
dimensions = (0, 1, 3)
print(0 not in dimensions)

# loads()：将json数据转化成dict数据
# dumps()：将dict数据转化成json数据
# load()：读取json文件数据，转成dict数据
# dump()：将dict数据转化成json数据后写入json文件
# 字典
dictionary = {
    'name': 'haha',
    'age': 18,
    'other': 'dhjh'
}
dictionary.keys()
dictionary.values()
print(dictionary.__contains__("age"))
for key, value in dictionary.items():
    print(key + str(value))
del dictionary['other']

print(int('18'))

print('1234' in 'dskh1234dvj')

