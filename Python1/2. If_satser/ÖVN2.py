
# uppgift 1
# number = int(input("Please enter a number:"))
# if number > 10:
#     print("number is  more than 10. större än ")
# else:
#     print("number is less than 10. mindre än")

# ---------------------------------------------

#  uppgift 2

# milk = int(input("how many packs of milk left?"))

# if milk < 10:
#     print("buy 30 packs of milk.")
# elif milk >=10 and milk <= 20:
#     print("buy 20 packs of milk.")
# else:
#     print("You do not have to order!")


# ------------------------------
# uppgift 3

# num1 = int(input("Please enter a number:,/Mata in tal 1"))
# num2 = int(input("please enter another number:,/ Mata in tal 2"))

# if num1 > num2:
#     largest = num1
# else:
#     largest = num2

# print(f"Det största talrt är:{largest}")

# --------------------

# uppgift 4

# num1 = input("Mata in tal 1:")
# num2 = input("Mata in tal 2:")
# num3 = input("Mata in tal 3:")

# if num1 > num2 and num1 > num3:
#     largest = num1
# elif num2 > num1 and num2 > num3:
#     largest = num2
# else:
#     largest = num3

# print(f"Det största talet är:{largest}")


# -----------------------------


# uppgift 5

# kategori = input("which category belongs you to: adult, pensioner or student?")

# if kategori == "pensioner" or kategori == "student":
#     print("Priset för resan är 20 kr")
# elif kategori == "adult":
#     print("Priset för resan är 30 kr")
# else:
#     print("Du har angett en felaktig kategori.")



# kategori = input("which category belongs you to: adult, pensioner or student?")

# if kategori == "pensioner" or kategori == "student":
#     pris = 20
#     print(f"Priset för resan är {pris} kr")
# elif kategori == "adult":
#     pris = 30
#     print(f"Priset för resan är {pris} kr")
# else:
#     print("Du har angett en felaktig kategori.")

# ----------------------------------

# uppgift 6

# birth_year = int(input("Please enter your year of birth?"))

# if 1980 <= birth_year < 1990:
#     print("Du är född på 1980-talet.")
# elif birth_year >= 1990 and birth_year < 2000:
#     print("Du är född på 1990-talet.")
# else:
#     print("Du är inte född på 1990 eller 1980-talen.")

# ------------------------

# uppgift 7

# land = input("Vilket land bor du i? ").lower()

# # if land == ("Sverige", "Danmark", "Norge"):
# if land in ["Sverige", "Danmark", "Norge"]:
#     print( "Du bor i Skandinavien." )
# else:
#     print(  "Du bor inte i Skandinavien." )

# ------------------------

# uppgift 8 

# money = int(input("Hur mycket pengar har du?"))
# rabbat = input("Har du rabbat? Om ja, ange Ja; annars anger du Nej. ")

# if 15 < money <= 25 and rabbat == 'Nej':
#     print("Du kan köpa en liten hamburgare. ")
# elif money > 15 and money <= 25 and rabbat == 'Ja':
#     print(" Du kan köpa en liten hamburgare och en pommes frites. ")
# elif money > 25 and money <= 50 and rabbat == 'Nej':
#     print("Du kan köpa en stor hamburgare.")
# elif money > 25 and money <= 50 and rabbat == 'Ja':
#     print("Du kan köpa en stor hamburgare och pommes frites. ")
# elif money <= 60 and money >= 50 and rabbat == ("Ja" or "Nej"):
#     print("Du kan köpa ett meal med dryck.")
# else:
#     print("Du skriver fel")

# -----------------------

# uppgift 9 

# 方法 1

# temp_Svedala = float(input("Mata in temperaturen i Svedala"))
# temp_Jukkasjärvi = float(input("Mata in temperaturen i Jukkasjärvi"))
# temp_Visby = float(input("Mata in temperaturen i Visby"))

# if temp_Svedala < temp_Jukkasjärvi and temp_Svedala < temp_Visby:
#     print("Det är kallast i Svedala")
# elif temp_Jukkasjärvi < temp_Svedala and temp_Jukkasjärvi < temp_Visby:
#     print("Det är kallast i Jukkasjärvi")
# else:
#     print("Det är kallast i Visby")

# if temp_Svedala > temp_Jukkasjärvi and temp_Svedala > temp_Visby:
#     print("Det är varmast i Svedala")
# elif temp_Jukkasjärvi > temp_Svedala and temp_Jukkasjärvi > temp_Visby:
#     print("Det är varmast i Jukkasjärvi")
# else:
#     print("Det är varmast i Visby")

# ave_temp = (temp_Svedala + temp_Jukkasjärvi + temp_Visby) / 3
# print(f"Medeltemperaturen är {ave_temp} grader.")

# 方法2 

# temp_Svedala = float(input("Mata in temperaturen i Svedala"))
# temp_Jukkasjärvi = float(input("Mata in temperaturen i Jukkasjärvi"))
# temp_Visby = float(input("Mata in temperaturen i Visby"))

# kallast_plats = min(temp_Svedala, temp_Jukkasjärvi, temp_Visby)
# varmast_plats = max(temp_Svedala, temp_Jukkasjärvi, temp_Visby)

# if kallast_plats == temp_Svedala:
#     print("Det är kallast i Svedala")
# elif kallast_plats == temp_Jukkasjärvi:
#     print("Det är kallast i Jukkasjärvi")
# else:
#     print("Det är kallast i Visby")

# if varmast_plats == temp_Svedala:
#     print("Det är varmast i Svedala")
# elif varmast_plats == temp_Jukkasjärvi:
#     print("Det är varmast i Jukkasjärvi")
# else:
#     print("Det är varmast i Visby")

# 方法 3

# if kallast_plats == temp_Svedala:
#     coldest_plats = 'Svedala'
# elif kallast_plats == temp_Jukkasjärvi:
#     coldest_plats = 'Jukkasjärvi'
# else:
#     coldest_plats = 'Visby'

# if varmast_plats == temp_Svedala:
#     varmast_location = 'Svedala'
# elif varmast_plats == temp_Jukkasjärvi:
#     varmast_location = 'Jukkasjärvi'
# else:
#     varmast_location = 'Visby'

# print(f"Det är kallast i {coldest_plats}")
# print(f"Det är varmast i {varmast_location}")

# ave_temp = (temp_Svedala + temp_Jukkasjärvi + temp_Visby) / 3
# print(f"Medeltemperaturen är {ave_temp} grader.")


# --------------------------------------------

# uppgift 10

# password = input("Snälla att mata in ett lösenord som är minst 8 tecken långt:")

# if len(password) >= 8:
#     print("Lösenordet är skapat.")
# else:
#     print("Lösenordet uppfyller inte krav.")

# -----------------------------------------

# uppgift 11

# Celsius_temperatur = float(input("Mata in en temperatur i Celsius:"))

# new_temp = input("vill du konvertera temperaturen till Fahrenheit eller Kelvin? \n Konvertera till Fahrenheit mata in Ja. \n Konvertera till Kelvin mata in Nej.")

# if new_temp == "Ja":
#     temp = Celsius_temperatur * 9/5 + 32
#     print(f"(Fahrenheit_temp is {temp}")
# elif new_temp == "Nej":
#     temp = Celsius_temperatur + 273.15
#     print(f"(Kelvin_temp is {temp}")
# else:
#     print("Ogiltigt val.")

# ------------------------------------

# uppgift 12

# tal1 = float(input("Mata in tal 1:"))
# tal2 = float(input("Mata in tal 2:"))

# operation = input("vilken operation vill du utföra \
#                   (\n a. addition \n b. subtraktion \n c. multiplikation \n d. division).")

# if operation == "a":
#     result = tal1 + tal2
#     print(f"The result is {result}")
# elif operation == "b":
#     result = tal1 - tal2
#     print(f"The result is {result}")
# elif operation == "c":
#     result = tal1 * tal2
#     print(f"The result is {result}")
# elif operation == "d":
#     if tal2 == 0:
#         print("Divisorn kan inte vara 0.")
#     else:
#         result = tal1 / tal2
#         print(f"The result is {result}")
# else:
#     print("Ogiltig operation.")

# ----------------------------------------

# uppgift 13

# original_pris = int(input(" mata in priset på en produkt:"))
# rabatt = int(input("mata in en rabattprocent (till exempel 10 för 10%)."))

# if rabatt > 50:
#     print("Rabatten är för hög, det nya priset kan inte beräknas.")
# else:
#     new_pris = original_pris * (1 - rabatt/100)
#     print(f"Det nya priset efter rabatten är {new_pris} kr")

# -----------------------------------------

# uppgift 14

# 方法 1 day.lower() 

# day = input("mata in en veckodag: (t.ex. 'måndag', 'tisdag')")
# tid = int(input("mata in tiden i 24-timmarsformat: (t.ex. 14 för kl. 14:00)"))

# if day.lower() in ('måndag', 'tisdag', 'onsdag', 'torsdag', 'fredag'):
#     if tid >=9 and tid<=18:
#         print("Butiken är öppen")
#     else:
#         print("Butiken är stängd")
# elif day.lower() == 'lördag':
#     if tid >= 10 and tid <= 14:
#         print("Butiken är öppen")
#     else:
#         print("Butiken är stängd")
# elif day.lower() == 'söndag':
#     print("Butiken är stängd")
# else:
#     print("Ogiltig inmatning")

# 方法 2 lower() 

day = input("mata in en veckodag: (t.ex. 'måndag', 'tisdag')").lower()
tid = int(input("mata in tiden i 24-timmarsformat: (t.ex. 14 för kl. 14:00)"))

if day in ['måndag', 'tisdag', 'onsdag', 'torsdag', 'fredag']:
    if 9 <= tid <= 18:
        print("Butiken är öppen")
    else:
        print("Butiken är stängd")
elif day == 'lördag':
    if tid >= 10 and tid <= 14:
        print("Butiken är öppen")
    else:
        print("Butiken är stängd")
elif day == 'söndag':
    print("Butiken är stängd")
else:
    print("Ogiltig inmatning")

# -----------------------------------------

# uppgift 15

# tal = int(input("Mata in ett heltal:"))

# if tal % 2 == 0:
#     print("Talet är jämnt.")
# else:
#     print("Talet är udda.")

# # %: Modulus 



















