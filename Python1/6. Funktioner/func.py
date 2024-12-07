

# def any_name(parameter, parameter2):
#     """
#     Docstring, förklarar vad denna funktion gör.
#     """
#     print(parameter)

# --------------------------------------

# hello- funktion

# def hello():
#     print("hello")

# hello()

# --------------------------------------

# def giveMeHello():
#     return "Hello you!"

# res = giveMeHello()

# print(res)

# -----------------------------

# def giveMeHello():
#     return "Hello you!"

# print(giveMeHello())

# -----------------------------

# number1 = 3
# if number1 % 2 == 0:
#     print("even")
# else:
#     print("odd")

# number2 = 5
# if number2 % 2 == 0:
#     print("even")
# else:
#     print("odd")

# number3 = 20
# if number3 % 2 == 0:
#     print("even")
# else:
#     print("odd")

# odd:奇数   Even:偶数

# def evencheck(number):
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# # 得用 print 因为 是return 值不能直接显示 或者用一个变量接住这个值
# # 如果没有用 return， 可以直接 evencheck() 来显示结果
# print(evencheck(5))
# print(evencheck(10))
# print(evencheck(7))

# -------------------------------------

# def evencheck(number):
#     print(number % 2 == 0)

# evencheck(5)
# evencheck(10)
# evencheck(7)

# --> result: True / False

# ---------------------------------------

# # 原始值是 John， 给个新名字参数变成新名字，否则默认是 John

# def helloYou(name="John"):
#     return ("hello " + name)

# res = helloYou("Bob")
# print(res)

# res = helloYou()
# print(res)

# ---------------------------------------

# 2个参数

# def addEvenOnly(num1, num2):
#     if (num1 % 2 != 0) or (num2 % 2 != 0):
#         return False 
#     else:
#         return num1 + num2

# x = addEvenOnly(7, 8)
# y = addEvenOnly(0, 8)

# print(x)
# print(y)

# ---------------------------------------

# def func(a, b, c=10, d=11):
#     print(a, b, c, d)

# func(1, 2)
# func(1, 2, 3)
# func(1, 2, 3, 4)

# func(c="c", a="a", d="d", b="b")

# func(1, 2, d=4)

# ---------------------------------------

# x = 10       # Global variabel  全局变量

# def myFunc():
#     x = 5     # Lokal variabel  局部变量
#     print(x)

# myFunc()
# print(x)

# ---------------------------------------

# *args 可以接收任意数量的参数, 元组形式 输出 Tuple
# *args 用于传递任意数量的位置参数，以元组形式接收。
# **kwargs 用于传递任意数量的关键字参数，以字典形式接收。

# def func(*args):
#     print(args)

# func()
# func(1)
# func(1, 2)
# func(1, 2, 3)
# func(1, 2, 3, 4, 5, 6)

# ---------------------------------------

# **kwargs: keyword arguments.可以接收任意数量的参数(字典形式出现) **kwargs 输出的是字典

# def func2(a, b, **kwargs):
#     print(a, b)
#     print(kwargs)
#     print(a, b,kwargs)

# func2(1,2, c=14, d=19)

# ---------------------------------------


# def func2(a, b, **kwargs):
#     print(a, b,kwargs["c"], kwargs["d"])

# func2(1,2, c=14)

# ---------------------------------------

# def func2(a, b, **kwargs):
#     print(a, b)
#     if "c" in kwargs:
#         print(kwargs["c"])
#     elif "d" in kwargs:
#         print(kwargs["d"])

# func2(1,2, c=14)

# ---------------------------------------

# def func3(a, b, *args, name="John", **kwargs):
#     print(f"a = {a}")
#     print(f"b = {b}")
#     print(f"args = {args}")
#     print(f"name = {name}")
#     print(f"kwargs = {kwargs}")

# # func3(1, 2)

# func3(1, 2, 3, name = "Jie", age=34, email="abc@gmail.com")

# func3(1, 2, 3, name = "Jie", age=34, email="abc@gmail.com", phone="123")

