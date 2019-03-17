from random import randint


def describe_user(name='default', age=18):
    print(name)
    print(age)


describe_user(name='haha')


def test(*names):
    for name in names:
        print(name)


test(1, 2, 3)


def test2(**names):
    for k, v in names.items():
        print(str(k) + str(v))


test2(name='4', age='18', add='shenzhen')

num = 0
while num != 6:
    num = randint(1, 6)
    print(num)
