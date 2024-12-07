# uppgift 1

# # Skapa en tom lista för att spara talen
# number_list = []

# # Fråga användaren om att mata in fyra tal
# for i in range(4):
#     num = int(input(f"mata in ett tal {i +1}:"))
#     number_list.append(num)

# Max_num = max(number_list)

# print(f"Det största talet är:{Max_num}")

# -----------------------------------------

# uppgift 2

# number_list = []

# for i in range(3):
#     num = int(input("mata in ett tal:"))
#     number_list.append(num)

# Min_num = min(number_list)
# Max_num = max(number_list)

# # 方法 1

# number_list.remove(Max_num)
# number_list.remove(Min_num)
# Medianen = number_list[0]

# # 方法 2

# for n in number_list:
#     if n != Max_num and n != Min_num:
#         Medianen = n
#         break

# # 方法 3 排序取中间

# sorted_num = sorted(number_list) 
# Medianen = sorted_num[1]

# print(f"Minsta talet: {Min_num}")
# print(f"Största talet: {Max_num}")
# print(f"Medianen: {Medianen}")

# -----------------------------------------

# uppgift 3  Gissa talet

# num_list = []

# for i in range(10):
#     num = int(input("mata in ett heltal mellan 1 och 100:"))
#     num_list.append(num)

# num_list = [12, 25, 37, 77, 89, 90, 91, 92, 93, 99]

# guess_num = int(input(" Gissa ett heltal mellan 1 och 100:"))

# if guess_num in num_list:
#     print(" Ha, vilken tur du har, du gissa rätt! Är en på 10 att det sker!")
# else:
#     print("Aj då, bättre lycka nästa gång!")

# -----------------------------------------

# # uppgift 4  Favoritdjuret  Set() 交集

# djur = {"katt", "hund", "häst", "ko", "får", "björn", "uggla", "orm"}
# print(djur)

# input_djur = set()

# for i in range(3):
#     m = input("Ange 1 djur som du gillar: ").lower()
#     input_djur.add(m)

# print(input_djur)

# count = len(djur & input_djur)

# print(f" Vi har {count} stycken gemensamma djur vi gillar!")


# KLURING

djur_input = ["katt", "hund", "häst", "ko", "får", "björn", "uggla", "orm"]

# 方法 1

# djur_str = input("Ange 3 djur som du gillar och separerade med kommatecken:").lower().split(",")
# djur_str = [djur.strip() for djur in  djur_str]
# # 假设用户输入 " Katt , Hund ,Lejon ", 那么 .strip() 将去除逗号，得到 ['katt', 'hund', 'lejon']

# # # 用嵌套循环来看两个列表里有多少重叠的元素，其实set（）& 更方便
# gemensamma = 0
# for a in djur_str:
#     if a in djur_input:
#         gemensamma += 1

# print(f"Ni har {gemensamma} gemensamma djur.")
# print(type(djur_str))       # list
# print(type(djur_input))     # set

# # # 方法2
# djur_input = {"katt", "hund", "häst", "ko", "får", "björn", "uggla", "orm"}

# djur_str = input("Ange 3 djur som du gillar och separerade med mellanslag:").lower()

# djur_set = set(djur_str.split())
# print(djur_set)

# count = len(djur_input & djur_set)
# count = len(djur_input.intersection(djur_set))    # 等于取两个集合的交集 djur_input & djur_set
# count = len(djur_input.union(djur_set))           # 等于取两个集合的并集

# print(f" Vi har {count} stycken gemensamma djur vi gillar!")

# -----------------------------------------

# uppgift 5

# def print_menu():
#     print("\nMeny:")
#     print("1. Add")
#     print("2. Remove")
#     print("3. Edit")
#     print("4. Print shopping list")
#     print("5. Insert")
#     print("6. Reversed")
#     print("7. Sorted")
#     print("8. Delete shopping list")
#     print("0. Exit")

# def add_item(shopping_list):
#     item = input("Ange ett item att lägga till:")
#     shopping_list.append(item)
#     print(f"{item} har lagt till.")

# def remove_item(shopping_list):
#     item = input("Ange ett item att ta bort:")
#     if item in shopping_list:
#         shopping_list.remove(item)
#         print(f"{item} har tagits bort.")
#     else:
#         print(f"{item} finns inte på listen.")

# def edit_item(shopping_list):
#     old_item = input("Ange ett item att ändra:")
#     if old_item in shopping_list:
#         new_item = input("Ange det nya itemet:")
#         index = shopping_list.index(old_item)
#         shopping_list[index] = new_item
#         print(f"{old_item} har ändrats till {new_item}")
#     else:
#         print(f"{old_item} finns inte på listen.")

# def print_shopping_list(shopping_list):
#     if shopping_list:
#         print("\nShoppinglista:")
#         for item in shopping_list:
#             print(f"- {item}")
#     else:
#         print("Shoppinglista är tom.")

# def insert_item(shopping_list):
#     item = input("Ange ett item att infoga:")
#     index = int(input("Ange positionen att infoga itemet på (0-indexerad):"))
#     if index >= 0 and index <= len(shopping_list):      # =len() 说明可以在列表末尾加值
#         shopping_list.insert(index, item)
#         print(f"{item} har infogats på position {index}")
#     else:
#         print("Ogiltig position.")
    
# def reverse_list(shopping_list):
#     shopping_list.reverse()
#     print("Shoppinglistan har vänds")

# def sort_list(shopping_list):
#     shopping_list.sort()
#     print("Shoppinglistan har sorterats")

# def delete_shopping_list():
#     return []

# def main():
#     shopping_list = []
#     while True:
#         print_menu()
#         choice = input("Välj ett alternativ: ")
        
#         if choice == "1":
#             add_item(shopping_list)
#         elif choice == "2":
#             remove_item(shopping_list)
#         elif choice == "3":
#             edit_item(shopping_list)
#         elif choice == "4":
#             print_shopping_list(shopping_list)
#         elif choice == "5":
#             insert_item(shopping_list)
#         elif choice == "6":
#             reverse_list(shopping_list)
#         elif choice == "7":
#             sort_list(shopping_list)
#         elif choice == "8":
#             shopping_list = delete_shopping_list()
#             print("Shoppinglistan har raderats.")
#         elif choice == "0":
#             print("Avslutar programmet")
#             break
#         else:
#             print("Ogiltigt val, försök igen.")


# if __name__ == "__main__":
#     main()

# ------------------------------------------------------

# uppgift 6

# 6. Dictionary

# Skriv en bankapplikation. Skriv först en meny med följande val:
# 1. Skapa konto
# 2. Ta bort konto
# 3. Lista alla kontonummer
# 4. Lista totalsaldo
# 5. Lista alla kontonummer och saldo


# account_dict = {}

# def print_menu():
#     print("\nMeny:")
#     print("1. Skapa konto.")
#     print("2. Ta bort konto.")
#     print("3. Lista alla kontonummer.")
#     print("4. Lista totalsaldo.")
#     print("5. Lista alla kontonummer och saldo.")
#     print("0. Avsluta.")

# def skapa_konto():

#     konto_number = int(input("Ange ett num att lägga till:"))
#     konto_saldo = float(input("Ange en pengar att lägga till:"))          

#     if konto_number in account_dict:
#         print("Kontot finns redan.")
#     else:
#         account_dict[konto_number] = konto_saldo
#         print(f"Konto {konto_number} har skapad som har pengar {konto_saldo}")
#         print(account_dict)

# def tabort_konto():
#     num = int(input("Ange ett konto_number att ta bort"))
#     if num in account_dict.keys():
#         account_dict.pop(num)
#         print(account_dict)
#         print(f"Konto {num} har tagits bort.")      
#     else:
#         print("Kontot finns inte.")

# def lista_alla_kontonummer():
#     if account_dict:
#         print("Alla kontonummer:")
#         for konto_number in account_dict:  
#         # 在 Python 中，当你对字典进行迭代时，默认迭代的是字典的键，
#         # 因此不需要显式调用 account_dict.keys()。
#             print(konto_number)
#     else:
#         print("Inga konton finns.")

# def lista_totalsaldo():
#     totalsaldo = sum(account_dict.values())
#     print(f"Totalsaldo är {totalsaldo} SEK")

# def lista_alla():
#     if account_dict:
#         print("Alla kontonummer och saldo:")
#         for kontonummer, saldo in account_dict.items():
#             print(f"Konto {kontonummer}: {saldo}SEK")
#     else:
#         print("Inga konton finns.")
    
# def main_menu():
    
#     print_menu()
#     while True:
#         choice = input("Välj ett alternativ: ")
#         if choice == "1":
#             skapa_konto()
#         elif choice == "2":
#             tabort_konto()
#         elif choice == "3":
#             lista_alla_kontonummer()
#         elif choice == "4":
#             lista_totalsaldo()
#         elif choice == "5":
#             lista_alla()
#         elif choice == "0":
#             print("Avsluta programmet.")
#             break
#         else:
#             print("Ogiltigt val, försök igen.")

#     print(account_dict)


# if __name__ == "__main__":
#     main_menu()














