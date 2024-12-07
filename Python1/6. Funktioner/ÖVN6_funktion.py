# uppgite 1

# def arrayCheck(num_list):
#     for i in range(len(num_list) - 2):
#         if num_list[i] == 1 and num_list[i +1] == 2 and num_list[i + 2] == 3:
#             return True
#     return False


# print(arrayCheck([1, 1, 2, 3, 1]))
# print(arrayCheck([1, 1, 2, 4, 1]))
# print(arrayCheck([1, 1, 2, 1, 2, 3]))

# 当函数找到 [1, 2, 3] 这样的序列时，会执行 return True，此时函数就会结束，并返回 True，不会再执行后面的循环或其他代码。
# 如果在循环中没有找到 [1, 2, 3] 这个序列，则循环结束后执行 return False，返回 False 表示序列不存在。

# ------------------------------------------

# # uppgite 2 

# def stringBits(string):
#     string = string[::2]
#     print(string)

# def stringBits(s):
#     return s[::2]      # return 结果输出必须要写 print（）

# stringBits('Hello')
# stringBits('Hi')
# stringBits('Heeololeo')


# ------------------------------------------

# uppgite 3

# def doubleChar(string):
#     new_string = ""
#     for i in range(0, len(string)):
#         a = string[i] * 2
#         new_string = new_string + a
#     print(new_string)    

# # 老师的
# def doubleChar(s):
#     result = ""
#     for char in s:
#         result = result + char * 2
#     return result


# print(doubleChar('The'))
# print(doubleChar('AAbb'))
# print(doubleChar('Hi-There')) 

# ------------------------------------------

# uppgite 4  count_evens Funktion

# def count_evens(numbers):
#     count = 0
#     for i in numbers:
#         if i % 2 == 0:
#             count += 1
#     return count

# print(count_evens([2, 1, 2, 3, 4]))
# print(count_evens([2, 2, 0]))
# print(count_evens([1, 3, 5]))

# ------------------------------------------

# uppgite 5


# str(number): 首先，number 被转换为字符串，这样你可以逐个字符（数字）进行处理。
# int(digit): 对于每个字符（数字），它被转换回整数。
# for digit in str(number): 遍历字符串中的每个字符，将其转换为整数并生成新的列表。
# random.shuffle(digits) 是 Python 中 random 模块的一部分，用于将一个列表中的元素随机打乱顺序。
# shuffle() 方法会直接修改原列表。

import random

def generate_Numbers():
    digits = list(range(10))
    random.shuffle(digits)
    return digits[:3]

def guessGame():
    numbers = generate_Numbers()

    while True:
        guess = int(input(" Gissa ett tresiffrigt nummer.Vad är din gissning? "))
        guess_list = [int(digit) for digit in str(guess)]

        if guess_list == numbers:
            print("Match!")
            break

        else:
            guess_set = set(guess_list)
            numbers_set = set(numbers)

            if len(guess_set & numbers_set) == 3:
                print("Close")
            elif len(guess_set & numbers_set) in [1, 2]:
                print("En eller två siffror är close")
            elif len(guess_set & numbers_set) == 0:
                print("Nope")

guessGame()


        











