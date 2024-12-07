# import pandas as pd

# uppgift 1

# for i in range(11):
#     print(i)

# count = 0
# while count <= 10:
#     print(count)
#     count += 1

# ------------------------------------
# uppgift 2  Talen emellan

# tal1 = int(input("Ange ett mindre heltal:"))
# tal2 = int(input("Ange ett större heltal:"))

# for i in range(tal1 + 1, tal2):
#     print(i)

# i = tal1 + 1
# while i < tal2:
#     print(i)
#     i += 1

# ------------------------------------

# uppgift 3

# tal1 = int(input("Ange ett heltal:"))
# tal2 = int(input("Ange ett heltal:"))
# amount = tal1 +tal1

# fråga = input("Vill du fortsätta(J/N)?")

# while fråga != "N":
#     tal1 = int(input("Ange ett heltal:"))
#     tal2 = int(input("Ange ett heltal:"))
#     amount = tal1 +tal1
#     print(f"Summan av de två talen är {amount}")
#     fråga = input("Vill du fortsätta(J/N)?")

# # 老师的

# answer = True

# while answer:
#     num1 = int(input("Ange ett heltal:"))
#     num2 = int(input("Ange ett heltal:"))
#     print(num1 + num2)
#     question = input("Vill du fortsätta(J/N)?").lower()

#     if question == "n":
#         break

# ------------------------------------

# uppgift 4

# sum = 0
# for i in range(10):
#     number = int(input(" mata in en siffra:"))
#     sum += number

# print(f"Totala summan av det du matat in är{sum}.")

# ------------------------------------

# uppgift 5

# tal = int(input("mata in ett tal:"))

# for i in range(1, tal):
#     print(i)

# Omvänt 反转

# num = int(input("mata in ett tal:"))

# 从 num - 1 开始、到 1 结束、以步长 -1 递减的整数序列

# for i in range(num - 1, 0, -1):
#     print(i)

# for i in range(1, num):
#     print(num - i)    


# num = 1
# while num < tal:
#     print(num)
#     num += 1

# ------------------------------------
# uppgift 6

# N = int(input("mata in ett tal:"))

# for i in range(1, 11):
#     multiplikations = N * i
#     print(f"{N} * {i} = {multiplikations}")
#     # print(f"{N} * {i} = {i * N}")


# count = 1
# while count < 11:
#     multiplikations = N * count
#     print(f"{N} * {count} = {multiplikations}")
#     count += 1

# ------------------------------------

# uppgift 7

# 方法 一

# 1.是素数：该函数判断一个数字是否为素数，通过检查它是否能被2到该数字的平方根之间的任何数整除。
# 2.打印素数：该函数遍历从2到 N的所有数字，检查它们是否为素数，并将素数添加到一个列表中。
# 3.程序要求用户输入一个 N 的值，并打印出所有小于等于该值的素数。
# 为什么没有 2 和 3？
            
# def is_primtal(tal):
#     if tal < 2:
#         return False
#     for i in range(2, int(tal ** 0.5) + 1):
#         if tal % i == 0:
#             return False
#         return True
    
# def print_primtal(N):
#     primtal_list = []
#     for tal in range(2, N+1):
#         if is_primtal(tal):
#             primtal_list.append(tal)
#     return primtal_list

# N = int(input("Ange ett tal N: "))
# primtal = print_primtal(N)
# print(f"Primtalen upp till {N} är: 2,3,{','.join(map(str, primtal))}")

# map(str, primtal) 会将 primtal 列表中的每一个数字都转换为字符串
# 如果 primtal 是 [2, 3, 5, 7]，则 map(str, primtal) 会生成 ['2', '3', '5', '7']   
# ', '.join(['2', '3', '5', '7']) 会生成 '2, 3, 5, 7' 这个字符串

# 方法二

N = int(input("Mata in ett tal:"))

for num in range(2, N + 1):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

# ------------------------------------
# uppgift 8

# 游程编码（Run-Length Encoding，RLE），该函数接收一个字符串 s 作为输入。
# 压缩的字符串 komprimerad_sträng
# 特殊处理：如果输入字符串为空，程序会返回一个空字符串。
#  if not s: return "".->如果字符串 s 是空的，程序将直接返回一个空字符串 ""，这意味着不进行任何压缩，因为空字符串不需要压缩。

def run_length_encoding(s):
    if not s:
        return ""
    
    komprimerad_sträng = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            komprimerad_sträng += str(count) + s[i - 1]
            count = 1

    # # Lägg till den sista tecken-gruppen
    # 当到达最后一个字符时，循环结束后，不会有“下一个字符”来触发保存操作。
    # 因此，必须在循环结束后，手动处理并添加最后一组字符及其计数。
    komprimerad_sträng += str(count) + s[-1]

    return komprimerad_sträng

# Exempel på användning
input_sträng = input("Ange en sträng: ")
komprimerad = run_length_encoding(input_sträng)
print(f"Den komprimerade sträng är: {komprimerad}")
print(f"Original: {input_sträng}")

