
# l = [1,2,3]

# print(type(l))
# print(type([]))
# print(type(()))
# print(type({}))

# --------------------------------------

# class Sample():
#     pass

# x = Sample()

# print(type(x))      # <class '__main__.Sample'>

# --------------------------------------

# class Dog():
#     def __init__(self, breed):
#         self.breed = breed

# milo = Dog(breed = "Labrador")
# frank = Dog(breed = "Huskie")

# print(milo.breed)
# print(frank.breed)

# --------------------------------------

# class Dog():

#     # class object atributes
#     species = 'däggdjur'
#     def __init__(self, breed, name):
#         self.breed = breed
#         self.name = name

# frank = Dog("Huskie", "Frank")

# print(frank.breed)
# print(frank.name)
# print(frank.species) 

# -----------------------------------------

# class Circle():    
#     pi = 3.14 

#     # Cirkeln initieräs med en radie (ständard 1) 圆用半径初始化（默认1)
#     def __init__(self, radius=1):   # radius 半径 
#         self.radius = radius      

#     # Metod för att beräkna arean (tänk på self)
#     def area(self):
#         return self.radius * self.radius * Circle.pi

#     # Metod för att sätta radien
#     def setRadius(self, radius):
#         self.radius = radius

#     # Metod för att hämta radien
#     def getRadius(self):
#         return self.radius


# c = Circle()
# c.setRadius(2)
# print("Radien är :", c.getRadius())  # Notera att du behöver använda () för att kalla metoden
# print("Area är:", c.area())


# -----------------------------------------

# 私有属性  self._radius

# @property 和 @setter 的使用是在 Python 中实现属性封装（encapsulation）的常见方法，
# 目的是为了提供对类中私有属性的安全访问与修改。
# @property：将一个方法装饰成属性，使得我们可以通过访问属性的方式调用方法，而不需要显式调用它。
# 例如，我们可以用 obj.radius 而不是 obj.radius() 来获取一个属性的值。
# @radius.setter：允许我们定义一个属性的“setter”方法，
# 当通过 obj.radius = value 来修改属性时，这个方法会被自动调用，并执行特定的逻辑。

# 为什么使用 @property 和 @setter？
# 1. 属性封装：
# 在定义类时，某些属性可能不希望被直接修改或访问（通常这些属性会以 _ 开头，如 _radius），因为直接暴露这些属性可能会导致对象状态不一致或不可控。
# 通过 @property 和 @setter，你可以控制这些属性的读取和写入行为，确保对象处于有效状态。
# 2. 控制访问逻辑：
# 当你需要对属性的值进行验证、检查或进行其他额外操作时（如防止属性设置为负数），你可以在 @setter 中实现逻辑，而不是让用户直接修改内部属性。
# 3. 代码简洁与可读性：
# 使用 @property 可以让属性访问看起来像普通的属性访问，不需要调用方法，提升代码的简洁性与可读性。

# @property 用于创建只读属性或控制属性的访问方式。
# @setter 用于定义属性的修改行为，可以增加验证逻辑，确保属性的正确性。


# class Circle():    
#     pi = 3.14 

#     def __init__(self, radius=1):   # radius 半径 
#         # Vi änvander _radius som privat attribut 使用 _radius 作为私有属性，只能读不能改
#         self._radius = radius       

#     # Getter för radius， 
#     # @property 用于创建只读属性或控制属性的访问方式。
#     @property
#     def radius(self):
#         return self._radius

#     # Setter för radius，
#     # @setter 用于定义属性的修改行为，可以增加验证逻辑，确保属性的正确性。
#     @radius.setter
#     def radius(self, radius):
#         self._radius = radius

#     # Metod för att beräkna arean (tänk på self)
#     def area(self):
#         return self.radius * self.radius * Circle.pi

# c = Circle()
# c.radius = 2        # Här används settern 设置值为2 用的 @radius.setter
# print("Radien är :", c.radius)        # Här används gettern 读取 @property
# print("Area är:", c.area())


# -----------------------------------------

# class Person:
#     def __init__(self, name, email, age):
#         self.name = name
#         self.email = email
#         self.age = age

#     def __str__(self):
#         return f'{self.name} är {self.age} år gammal och har e-post {self.email}'

# p1 = Person("Alice", "alice@qq.com", 34)
# p2 = Person("Bob", "bob@qq.com", 37)

# print(p1)
# print(p2)

# p1.phone = '0723344556'

# print(p1.phone)
# print(p2.phone)  # kommer inte funka /Error

# # -----------------------------------------

# class Person:
#     def __init__(self, **kwagrs):    # 构造函数，使用 **kwargs 以字典形式接收任意数量的键值对
#         self.__dict__ = kwagrs       # 将传入的关键字参数字典直接赋值给对象的 __dict__ 属性

#     def __str__(self):
#         return f"{self.name} ar {self.age} ar gammal"

# p1 = Person(name = 'Alice', age = 23)
# p2 = Person(name = 'Bob', age = 45)

# print(p1)
# print(p2)

# # -----------------------------------------

# class Something:
#     def __init__(self, data:dict):    # data:dict 默认形式
#         self.__dict__ = data

#     def __str__(self):
#         str_rep = ''
#         for key, value in self.__dict__.items():
#             str_rep += f'{key} = {value}\n'
#         return str_rep

# data_dict1 = {
#     'a' : 10,
#     'b' : 20,
#     'name' : 'One'
# }

# data_dict2 = {
#     'c' : 15,
#     'd' : 25,
#     # 'name' : 'Two'    # 去掉看可不可以
# }

# s1 = Something(data_dict1)
# s2 = Something(data_dict2)

# print(s1)
# print(s2)

# # -----------------------------------------




























