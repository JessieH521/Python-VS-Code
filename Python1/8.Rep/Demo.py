# Repetition

# # print(5+2)

# def adder(num1, num2):
#    return num1 + num2


# # Rör EJ

# print(adder(2,5)) 
# print(adder(7,9)) 

# print(2**5)

# ---------------------------------------

# x = "Hello"
# print(len(x))

# # Func

# def length(x):
#     return len(x)

# # # Rör EJ

# print(length('Hello'))


# print(x.upper())
# print(x.lower())
# print(x.split())    # --> ['Hello']
# print(x.split('e'))    # -->['H', 'llo']

# # x = "Hello world, this is Python"
# # print(x.split())
# # --> ['Hello', 'world,', 'this', 'is', 'Python']
# # 在这个例子中，split() 将字符串 x 按空格分割，并返回一个包含单词的列表。

# ---------------------------------------

# namn = "Alice"
# ålder = 30

# print("Namn", namn)
# print("ålder ", ålder )

# ålder = ålder + 1
# ålder += 1

# print("Uppdaterad ålder", ålder)

# ---------------------------------------

# # index
# # []

# a = "Hello world"

# print(a[0])    # --> string
# print(a[1])
# print(a[1:])
# print(a[:3])    # -->  Hel
# print(a[:])     # 全部
# print(a[-1])      #  最后一个字母
# print(a[::2])     # 每隔2个

# ---------------------------------------

# # string k  mutbal 有自己的位置 顺序 有序 无序
# # mutbal inmutbal 

# a = "hello world"  

# # a[0] = 'x'   # TypeError: 'str' object does not support item assignment 不支持项目分配

# a = a+ ' concatenate me'

# print(a)

# ---------------------------------------

# name = "Alice"
# age = 30
# print(f"My name is {name} and I am {age} years old.")

# ---------------------------------------

# if 1 < 2:
#     print("Yes!")
# else:
#     print("No!")

# ---------------------------------------

# def comparer(num1, num2):
#     if num1 < num2:
#         return "Yes!"
#     else:
#         return "No!"

# # Rör EJ

# print(comparer(1,2))  # ["Yes!"]
# print(comparer(4,3))   # ["No!"]

# ---------------------------------------

# if 1 == 2:
#     print('first')
# elif 3 == 3:
#     print('middle')
# else:
#     print('last')

# ---------------------------------------

# name = "Lisa"
# age = 35

# if age == 35 and name == "Lisa":
#     print("Kom in!")
# elif age == 35 or name == "Lisa":
#     print("Något av kraven uppfylls ej.")   # 有些要求没有得到满足。
# else:
#     print("Inga krav uppfulls.")    # 没有满足任何要求。

# ---------------------------------------------

# Loop

# for i in range(10):
#     print(i)

# for i in range(2, 10):
#     print(i)

# for i in range(2, 10, 2):     # 2-9 每2个取  2， 4， 6， 8
#     print(i)

# ---------------------------------------------
# lista

# lista = [1, True, None, "String", 2.56]

# for i in lista:
#     print(i)

# Func

# def lister(lista):
#     mylist = []
#     for i in lista:
#         mylist.append(i)
#     return mylist


# # Rör EJ
# print(lister([1, True, None, "String", 2.56]))

# ---------------------------------------------

# for i in range(5):
#     if i == 3:
#         break
#     print(i)
# else:
#     print("loopen avslutad")

# # 中间 break， else 不执行； for 都运行完也没break， else 正常执行


# for i in range(5):
#     if i == 6:
#         break
#     print(i)
# else:
#     print("loopen avslutad")

# ---------------------------------------------

# guess = input("Vilken ar den mest populara pizzatoppingen?\n")

# while guess != 'ost':
#     print("Fel! Det ar inte topping.")
#     guess = input("Vilken ar den mest populara pizzatoppingen?\n")

# print("ratt svar! Ost ar den mest  populara pizzatoppingen.")


# def glass_topping(guess):
#     while guess != 'ost':
#         return "Fel! Det ar inte topping."

#     return "ratt svar! Ost ar den mest  populara pizzatoppingen."


#  # Rör EJ
# test1 = glass_topping("skinka")
# print(test1)

# test2 = glass_topping("ost")
# print(test2)


# ---------------------------------------------

# my_lista = [0, 1, 2, "0", "Text", True]

# print(my_lista + ["new item"])
# print(my_lista)

# my_lista = my_lista + ["new item"]
# print(my_lista)

# print(my_lista * 2)

# lista = [1, 2, 3]

# lista.append('append me')
# lista.pop(0)   # 去掉第一个值 1
# print(lista)
# lista.remove('append me')
# print(lista)

# new_list = ["a", 'e', 'x', 'b', 'c']

# new_list.reverse()
# print(new_list)

# new_list.sort()
# print(new_list)


# ---------------------------------------------

# 字典 dictionary

# my_dictionary = {
#     1: "value one",
#     2: "value two",
#     3: "value three",
# }

# # print(my_dictionary[2])

# print(my_dictionary[3].upper())

# new_dict = {}

# new_dict['animal'] = 'cat'

# print(new_dict)

# Func

# def createDict(new_dictionary, animal, typeAnimal):
#     # new_dictionary = {}  不用写了 参数里已经加了。createDict({}, "animal", 'cat')
#     new_dictionary[animal] = typeAnimal
#     return new_dictionary

# # Rör EJ

# print(createDict({}, "animal", 'cat'))      # {'animal' : 'cat}

# dictionary = {
#     'key1': 1,
#     'key2': 2,
#     'key3': 3
#  }

# print(dictionary.keys())
# print(dictionary.values())
# print(dictionary.items())

# for key, value in dictionary.items():
#     print(f'{key}:{value}')

# ---------------------------------------------

# 



































