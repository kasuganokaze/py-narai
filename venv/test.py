for i in range(10):
    if i == 9:
        print("我是最后一个")
    else:
        print(i)

try:
    1/0
except ZeroDivisionError as e:
    print(11)
finally:
    print(111)