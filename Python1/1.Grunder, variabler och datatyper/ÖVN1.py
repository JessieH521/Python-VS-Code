from datetime import datetime


# Uppgift 1

# print('Hello')

# --------------------------------------------------------------

# Uppgift 2

# print("2021")
# print(2021)
# print("2021-12-24")
# print(2021-12-24)     # 减法 Subtraktion

# --------------------------------------------------------------


# Uppgift 3


# first_name = input("Please enter your firstname:")

# # print('Frist_Name:', first_name)

# second_name = input('Please enter your second name:')

# # print('Second_Name:', second_name)

# print('Name:', second_name, first_name)

# print('My name is: {b} {a}'.format(a=first_name, b=second_name))


# Challenge
# print(f'My name is: {second_name} {first_name}')
# print(f"Namnet i omvändordning är: {lastname} {name}")


# --------------------------------------------------------------

# Uppgift 4

# chatbot

# name = "RobotenJ"
# hobby = "piano"

# user_name = input('Please enter your name?')
# user_year = input('Please enter your year of birth?')
# user_hobby = input('Please enter your hobby?')

# calculate age

# age = datetime.now().year - int(user_year)        # from datetime import datetime
# print(age)

# print('Hej, jag heter {} och du heter {}. Din hobby är att {} och min hobby är att {}. \
#       Eftersom du är född {}, så är du {} år gammal.'\
#       .format(name, user_name, user_hobby, hobby, user_year, age))

# eller använda f""
# print(f"hello, my name is {name}, your name is {user_name}.")
# print(f"Your hobby is {user_hobby} and my hobby is {hobby}.")
# print(f"Since you were born in {user_year}, you are {age} years old.")

# # Challenge 1

# # upper()
# print('Hej, jag heter {} och du heter {}. Din hobby är att {} och min hobby är att {}. \
#       Eftersom du är född {}, så är du {} år gammal.'\
#       .format(name.upper(), user_name.upper(), user_hobby, hobby, user_year, age))

# # Challenge 2

# result = (hobby == user_hobby)
# print(result)

# if hobby == user_hobby:
#     print("We have the same hobby!")
# else:
#     print("We have different hobbies!")
#     print("tråkigt")  

# --------------------------------------------------------------

# Uppgift 5

# a = float(input('Please enter a number:'))
# b = float(input('Please enter another number:'))
# c = float(input('Please enter last number:'))

# sum = a + b + c
# ave = sum / 3
# print(f"The sum of the numbers is: {sum}")
# print(f"The average of the numbers is: {ave}")

# # challenge 挑战 - 小数

# decimal_number = float(input("Enter a decimal number: "))
# rounded_number = round(decimal_number)
# print(f"The nearest integer is : {rounded_number}")


# Python的round()函数与数学的四舍五入的区别， 其他值四舍五入，5有些不同
# 整数部分为偶  小数为0.5 向下取整　　0也是偶数
# 整数部分为奇  小数为0.5 向上取整

# print(round(0.5))    # 1     0
# print(round(2.5))    # 3     2
# print(round(5.5))    # 6     6

# 用 round 有问题，自己写函数

# # behöver absolut inte kunna just nu

# def custom_round(n):
#     if n % 1 >= 0.5:
#         return int(n) + 1
#     else:
#         return int(n)


# print(custom_round(0.5))
# print(custom_round(2.5))
# print(custom_round(5.5))


# --------------------------------------------------------------

# Uppgift 6

# str = input("Please enter your favorit food:")

# a
# print(len(str))
# print(f"The lengths of the string is: {len(str)}")

# b
# print(str[0], str[-1])
# print(f"The first letter is: {str[0]}")
# print(f"The last letter is: {str[-1]}")

# c
# print(str[::-1])
# print(f"The string in reverse is: {str[::-1]}")


# d

# str = "Hello world."
# # for a in str:
# #     print(a)
# #     print( )

# print("\n".join(str))       # 可以把字符串一行一行分开输出

# -------------------------------------

# .join() 是 Python 中字符串类的一个方法，常用于将可迭代对象（如列表、元组）中的元素连接成一个字符串。
# separator.join(iterable)  
# separator：你想要用来分隔每个元素的字符串。
# iterable：可以是任何可迭代对象，如列表、元组、字符串等，其每个元素都会被拼接到一起，并由 separator 分隔。

# letters = ['H', 'e', 'l', 'l', 'o']
# result = ''.join(letters)  # 使用空字符串作为分隔符
# print(result)  # 输出：Hello

# words = ['apple', 'banana', 'cherry']
# result = ', '.join(words)  # 使用逗号和空格作为分隔符
# print(result)  # 输出：apple, banana, cherry

# lines = ['First line', 'Second line', 'Third line']
# result = '\n'.join(lines)  # 使用换行符作为分隔符
# print(result)     
# First line  
# Second line
# Third line

# .join() 方法的 iterable 中的元素必须是字符串类型，否则会报错。
# 比如，如果你传入了数字，需要先将其转换为字符串。
# numbers = [1, 2, 3]
# result = ', '.join(map(str, numbers))  # 使用 map 将数字转换为字符串
# print(result)  # 输出：1, 2, 3

# ----------------------------------------------

# # e 切片
# print(f"Every second character is {str[::2]}")


# --------------------------------------------------------------

# Uppgift 7 Utmaningen 挑战


# 我自己写的

# True = 1, False = 0

# flower = None
# eat_lunch = True

# print(flower)
# print(eat_lunch)

# eat_dinner = eat_lunch + 5
# print(eat_dinner)

# result = (flower == 0)
# print(result)

# 老师写的

# # skapa en variabel med  värdet None

# var1 = None

# # skapa en variabel med ett Booleskt värde
# var2 = True

# # skriv ut värdena pa bada variabelerna
# print("Värdet av var1 ar:", var1)
# print("Värdet av var2 ar:", var2)

# # Addera var2 (Boolean) med 5
# resultat = var2 + 5
# print("Resultatet av var2 +5 ar:", resultat)

# # Konvertera det Booleska värdet till ett heltal 将布尔值转换为整数
# konverterat_var2 = int(var2)
# print(konverterat_var2)

# # Jämfor om var1(None) är lika med 0
# jämforelse = var1 == 0
# print("Är var1(None) lika med 0?", jämforelse)



# --------------------------------------------------------------







