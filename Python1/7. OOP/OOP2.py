
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __repr__(self):
#         return f" Point(X = {self.x} and Y = {self.y})"

# point1 = Point(10, 20)

# # print(point1.x, point1.y)

# print(point1)

# ----------------------------------------------

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __repr__(self):      # 开发时用
#         return f" Point(X = {self.x} and Y = {self.y})"
    
#     def __str__(self):       # def __str__(self): 会覆盖 def __repr__(self): --》 不会显示repr的
#         return f" Point object med (X = {self.x} and Y = {self.y})"

# point1 = Point(10, 20)

# # print(point1.x, point1.y)

# print(point1)

# ----------------------------------------------

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):    # def __eq__(self, other): 就是True（因为比较了内容）
#         return self.x == other.x and self.y == other.y
    

# point1 = Point(10, 20)
# point2 = Point(10, 20)

# print(point1 == point2)     
# # False 比较的是内存地址.如果加上 def __eq__(self, other): 就是True（因为比较了内容）

# ----------------------------------------------

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def swap_xy(self):
#         self.x, self.y = self.y, self.x       # swap 交换, 直接换 不需要中间值

# point1 = Point(10, 20)

# point1.swap_xy()
# print(point1.x, point1.y)

# ----------------------------------------------

# 继承 foradclass

# class A:
#     def __init__(self, value):
#         print(f'A.__init__ has value = {value}')
#         self.value = value

# class B(A):
#     def __init__(self, value):
#         print(f'B.__init__ has value = {value}')
#         super().__init__(value)             # super().__init__  不是 self  ?  
#         self.value += 10

# class C(A):
#     def __init__(self, value):
#         print(f'C.__init__ has value = {value}')
#         super().__init__(value)            
#         self.value *= 4

# class D(B, C):
#     def __init__(self, value):
#         print(f'D.__init__ has value  = {value}')
#         super().__init__(value)

# d = D(10)
# print(d.value)
# print(D.mro())   # methodlösningsordning  方法的解决顺序

# # <class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
# # 回溯执行修改 ：计算相反 A-C-B-D   10 * 4 + 10 = 50

# b = B(10)
# print(b.value)

# #  D()中间 B和C 换位置看看  class D(C, B): / 80；class D(B, C):50

# ------------------------------------

# 继承 foradclass

# from typing import Any

# class Animal:
#     def __init__(self, name):
#         self.name = name

# class Dog(Animal):
#     def __init__(self, name, breed):
#         # 调用父类的构造函数来初始化 name ， 再加一个属性 breed
#         super().__init__(name)
#         self.breed = breed

# # 创建 Dog 对象
# my_dog = Dog("Buddy", "Golden Retriever")

# print(my_dog.name)   # 输出: Buddy
# print(my_dog.breed)  # 输出: Golden Retriever

# ----------------------------------------------------

# class A:
#     def __init__(self, value):
#         print(f'A.__init__ has value = {value}')
#         self.value = value

# class B(A):
#     def __init__(self, value):
#         print(f'B.__init__ has value = {value}')
#         super().__init__(value)            
#         self.value += 10

# class C(A):
#     def __init__(self, value):
#         print(f'C.__init__ has value = {value}')
#         super().__init__(value)            
#         self.value *= 4

# class D(C, B):
#     def __init__(self, value):
#         print(f'D.__init__ has value  = {value}')
#         super().__init__(value)

# d = D(10)
# print(d.value)
# print(D.mro())   # methodlösningsordning
# # <class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
# # 计算相反 A-C-B-D

# # b = B(10)
# # print(b.value)


# ----------------------------------------------

# # Bas-klass (parent)  基类 父类

# class Animal:
#     def __init__(self):
#         print('Djur skapad.')

#     def WhoAmI(self):
#         print('Djur.')

#     def eat(self):
#         print('eat......nom nom...')

# # Avledd Klass (Derived klass)  子类
       
# class Dog(Animal):       # Dog ärver från Animal
#     def __init__(self):
#         print('hund skapad.')

#     def WhoAmI(self):
#         print('Hund.')

#     def bark(self):
#         print('Voff')

# d = Dog()
# d.WhoAmI()
# d.eat()
# d.bark()

# # ----------------------------------------------

# class Employee:
#     def __init__(self, first_name, last_name, salary):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.salary = salary

#     def __str__(self):
#         return f'{self.first_name} {self.last_name} tjänar {self.salary}'
    
# class Developer(Employee):
#     def __init__(self, first_name, last_name, salary, prog_lang):
#         super().__init__(first_name, last_name, salary)   # 在父类基础上添加了 prog_lang编程语言属性
#         self.prog_lang = prog_lang

#     def __str__(self):
#         return f'{super().__str__()} och favorit programmeringsspråk är {self.prog_lang}'   # 复制父类
        
# emp1 = Employee("Alice", "Ason", 45000)
# emp2 = Employee("Bob", "Bson", 42000)
# dev1 = Developer("Carl", "Cson", 50000, 'Python')

# print(emp1)
# print(emp2)
# print(dev1)

# ----------------------------------------------

# class Employee:
#     increase = 1.04   
#     def __init__(self, first_name, last_name, salary):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.salary = salary

#     def __str__(self):
#         return f'{self.first_name} {self.last_name} tjänar {self.salary}'
    
#     def increase_salary(self):
#         self.salary = int(self.salary * self.increase) 
#         # 使用 self.increase，则会根据具体的对象来选择 increase 值。
#         # 这意味着，如果子类（如 Developer）中定义了不同的 increase 值，它将使用子类中的值，而不是父类中的值。
#         # 如果用 Employee.increase 是类属性，所有字类都用这个值，字类中有另外的值也不会取，类属性值不会改变。

# class Developer(Employee):
#     increase = 1.10
#     def __init__(self, first_name, last_name, salary, prog_lang):
#         super().__init__(first_name, last_name, salary)
#         self.prog_lang = prog_lang

#     def __str__(self):
#         return f'{super().__str__()} och favorit programmeringsspråk är {self.prog_lang}'   # 复制父类
        
# emp1 = Employee("Alice", "Ason", 45000)
# emp2 = Employee("Bob", "Bson", 42000)
# dev1 = Developer("Carl", "Cson", 50000, 'Python')

# print(emp1)
# print(emp2)
# print(dev1)

# # Alla far Ioneökning

# emp1.increase_salary()    # 1.04   父类
# emp2.increase_salary()    # 1.04
# dev1.increase_salary()    # 1.10   子类按照子类自己的增长

# print(emp1)
# print(emp2)
# print(dev1)

# ----------------------------------------------

# Polymorfism 多态

# loop 循环

# class Animal:
#     def speak(self):
#         return "Ett Ljud"

# class Dog(Animal):
#     def speak(self):
#         return "Voff"
    
# class Cat(Animal):
#     def speak(self):
#         return "Mjau"
    
# dog = Dog()
# cat = Cat()

# animals = [dog, cat]

# for animal in animals:
#     print(animal.speak()) 

# ----------------------------------------------

# Duck - typing

class Bird:
    def make_sound(self):
        return 'Ett ljud'
    
class Duck(Bird):
    def make_sound(self):
        return 'kvack'
    
class Crow(Bird):
    def make_sound(self):
        return 'Kra'

def let_bird_make_sound(bird):
    return bird.make_sound()      

duck = Duck()
crow = Crow()

print(let_bird_make_sound(duck))
print(let_bird_make_sound(crow))

# 多态性：当一个基类的引用（如 bird）指向不同的子类对象（如 Duck 或 Crow），
# Python 会根据子类的实现来调用相应的方法。这就是多态的概念。
# 这正是多态的表现：虽然 bird 是一个 Bird 类型的引用，
# 但根据实际传入的对象（Duck 或 Crow），make_sound() 方法的具体实现不同。
























