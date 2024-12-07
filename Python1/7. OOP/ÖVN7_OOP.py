
# uppgift 1

# class Matratt:
#     def __init__(self, name, pris, type, kalo):
#         self.name = name
#         self.pris = pris
#         self.type = type
#         self.kalo = kalo

#     def __str__(self):
#         return f"Rätt:{self.name}, pris: {self.pris} kr, type: {self.type}, antal kalorier: {self.kalo} kcal."

# def main_menu():
#     # 1.skapa Matratt Objects 4个对象
#     ratt1 = Matratt("Vegetarisk Lasagne", 85, "Vegetarisk", 600)
#     ratt2 = Matratt("Köttbullar med Potatismos", 95, "Kött", 800)
#     ratt3 = Matratt("Falafel med Sallad", 80, "Vegansk", 500)
#     ratt4 = Matratt("Grillad Kyckling med ris", 110, "Kött", 750)

#     # 2.Object into List
#     menu_list = [ratt1, ratt2, ratt3, ratt4]

#     # 3.print dagens lunchmeny
#     print("\n Dagens lunchmeny:")
#     for ratt in menu_list:
#         print(ratt)

# if __name__ == "__main__":
#     main_menu()

# --------------------------------------------

# uppgift 2 

class Person:
    def __init__(self, födelsedatum, name=None, address=None, postnummer=None):
        # name=None, 出生日期是必须的，其他可以不写 得用None  
        self.födelsedatum = födelsedatum
        # Övriga attribut kan sättas senare
        self.name = name
        self.address = address
        self.postnummer = postnummer

    @property                 # 属性  get
    def name(self):
        return self._name
    
    @name.setter              # 方法 set
    def name(self, name):
        self._name = name

    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, address):
        self._address = address

    @property
    def postnummer(self):
        return self._postnummer
    
    @postnummer.setter
    def postnummer(self, postnummer):
        self._postnummer = postnummer

    # Method

    # 允许后续修改或更新名字：虽然在初始化时设置了 name，但是程序运行过程中，可能需要修改某个人的名字。
    # 如果没有类似 Namnge 这样的函数，就只能在初始化时设置，后续无法再修改。

    def Namnge(self, change_name):
        self.name = change_name       # name 是上面的原始名字，change_name  是新name

    def BytAdress(self, new_address, new_postnummer):
        self.address = new_address
        self.postnummer = new_postnummer
        
    def __str__(self):      # def visa_info(self): 老师定义了一个可以展示的方法， 没有用__str__
        return f"Name: {self.name}, Födelsedatum: {self.födelsedatum}, Address: {self.address}, {self.postnummer}"
    
def main():

    # Create two Person objects
    p1 = Person("1994-08-04", "Jie", postnummer= 15460)
    p2 = Person("1994-05-04", "Alex", "Dottningsgatan 1, Stockholm", 17650)

    print(p1)
    print(p2)

    # Set new names and addresses
    p1.Namnge("JC")
    p1.BytAdress("svevagen 56", "13455")
    p2.Namnge("Gustav")
    p2.BytAdress("Eklundvagen 26, Nacka", 10876)

    # Print out the details
    print("Person 1 Details:")
    print(p1)

    print("Person 2 Details:")
    print(p2)

    # Låt Erik flytta in hos Anna
    p2.BytAdress(p1.address, p1.postnummer)
    print(p2)
    
if __name__ == "__main__":
    main()


# 属性和方法

# 1. 调用方式：
# 属性直接通过对象点符号（.）访问或修改。
# 方法通过对象调用，并且通常会包含括号 () 来执行行为。
# 2.目的：
# 属性用于存储信息，例如对象的名字、年龄等。
# 方法用于操作或改变属性，例如计算、打印、或执行某个任务。



# 老师的代码

# # Definiera klassen Person
# class Person:
#     def __init__(self, fodelsedatum):
#         # Födelsedatum är obligatoriskt
#         self.fodelsedatum = fodelsedatum
#         # Övriga attribut kan sättas senare
#         self.namn = None
#         self.gatuadress = None
#         self.postnummer = None
#         self.postort = None

#     # Property för namn (Get)
#     @property
#     def namn(self):
#         return self._namn
    
#     # Setter för namn
#     @namn.setter
#     def namn(self, namn):
#         self._namn = namn
    
#     # Property för gatuadress
#     @property
#     def gatuadress(self):
#         return self._gatuadress
    
#     # Setter för gatuadress
#     @gatuadress.setter
#     def gatuadress(self, gatuadress):
#         self._gatuadress = gatuadress

#     # Property för postnummer
#     @property
#     def postnummer(self):
#         return self._postnummer
    
#     # Setter för postnummer
#     @postnummer.setter
#     def postnummer(self, postnummer):
#         self._postnummer = postnummer
    
#     # Property för postort (Get)
#     @property
#     def postort(self):
#         return self._postort
    
#     # Setter för postort
#     @postort.setter
#     def postort(self, postort):
#         self._postort = postort
    
#     # Metod för att byta namn
#     def namnge(self, nytt_namn):
#         self.namn = nytt_namn

#     # Metod för att byta adress
#     def byt_adress(self, ny_gatuadress, nytt_postnummer, ny_postort):
#         self.gatuadress = ny_gatuadress
#         self.postnummer = nytt_postnummer
#         self.postort = ny_postort

#     # Metod för att skriva ut information om personen
#     def visa_info(self):
#         return f"Person: {self.namn}, Födelsedatum: {self.fodelsedatum}, Adress: {self.gatuadress}, {self.postnummer}, {self.postort}"

# # Skapa två personer
# person1 = Person("1990-05-12")
# person2 = Person("1988-08-23")

# # Namnge personerna
# person1.namnge("Anna Andersson")
# person2.namnge("Erik Svensson")

# # Sätt adresser för båda
# person1.byt_adress("Storgatan 12", "12345", "Stockholm")
# person2.byt_adress("Lillgatan 5", "54321", "Göteborg")

# # Skriv ut information om båda personerna
# print(person1.visa_info())
# print(person2.visa_info())

# # Låt Erik flytta in hos Anna
# person2.byt_adress(person1.gatuadress, person1.postnummer, person1.postort)

# # Skriv ut information efter flytten
# print("\nEfter flytten:")
# print(person1.visa_info())
# print(person2.visa_info())














