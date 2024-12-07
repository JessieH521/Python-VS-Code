
# # Uppgift 1

# # for

# for i in range(11):
#     print(i)

# # while

# number = 0

# while number <= 10:
#     print(number)
#     number += 1


# #---------------------------------------------------

# # Uppgift 2

# # for

# start = int(input("Mata in det första talet: "))
# end = int(input("Mata in det andra talet: "))

# for i in range(start +1, end):
#     print(i)


# while

# start = int(input("Mata in det första talet: "))
# end = int(input("Mata in det andra talet: "))

# i = start + 1
# while i < end:
#     print(i)
#     i += 1

# #---------------------------------------------------

# # Uppgift 3


# while True:
#     num1 = int(input("Mata in det första talet: "))
#     num2 = int(input("Mata in det andra talet: "))
#     print(num1+num2)
#     question = input("vill du fortsätta(j/n): ").lower()

#     if question == "n":
#         break

#---------------------------------------------------

# Uppgift 4

# sum = 0

# for i in range(4):
#     number = int(input("Mata in en siffra: "))
#     sum = sum + number

# print(f"Totala summan är: {sum}")

# #---------------------------------------------------

# # Uppgift 5

# num = int(input("Mata in ett tal: "))

# for i in range(1, num):
#     print(i)


# # Omvänt

# num = int(input("Mata in ett tal: "))

# for i in range(num -1, 0, -1):
#     print(i) 


# # Omvänt version 2

# num = int(input("Mata in ett tal: "))

# for i in range(1, num):
#     print(num - i)

#---------------------------------------------------

# Uppgift 6

# num = int(input("Mata in ett tal: "))

# for i in range(1, 11):
#     print(f"{i} * {num} = {i*num}")

#---------------------------------------------------

# Uppgift 7

# N = int(input("Mata in ett tal: "))

# for num in range(2, N + 1):
#     is_prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num)

#---------------------------------------------------

# Uppgift 8

# Inputsträngen som ska komprimeras
# s = "AAABBBCCDAA"
s= input("Mata in: ")

# Kontrollera om strängen är tom
if not s:
    komprimerad = ""
else:
    # Variabel för att lagra resultatet
    komprimerad = ""
    count = 1

    # Loop genom strängen
    for i in range(1, len(s)): 
        if s[i] == s[i - 1]: 
            count += 1
        else:
            komprimerad += str(count) + s[i - 1] 
            count = 1 

    # Lägg till det sista tecknet och dess räkning
    komprimerad += str(count) + s[-1] 

# Skriv ut resultatet
print(f"Original: {s}")
print(f"Komprimerad: {komprimerad}")