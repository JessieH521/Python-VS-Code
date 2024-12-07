# # uppgift 16

# order = input("vad vill du ha? hamburgare, korv med bröd, pizza, kebbab/falafel, grill och vegetariskt \n")

# def hamburgare():
#     hamburgare = input("Hej, det finns 3 hamburgare att väljamellan: \
#                     \n a.Vanlig burgare - 25kr \n b.Ostburgare - 39 kr \
#                         \n c.dubbelburgare - 55 kr \n")
#     if hamburgare == "Vanlig burgare":
#         hamburgare_price = 25
#     elif hamburgare == "Ostburgare":
#         hamburgare_price = 39
#     elif hamburgare == "dubbelburgare":
#         hamburgare_price = 55
#     print("The price of {} is {}".format(hamburgare, hamburgare_price))

#     gurka = input("Ska du välja med gurka? Ja eller Nej")
#     if gurka == "Ja":
#         print("gurka")
#     else:
#         print("No gurka")

#     ketchup = input("Ska du välja med ketchup? Ja eller Nej ")
#     if ketchup == "Ja":
#         print("ketchup")
#     else:
#         print("No ketchup")

#     senap = input("Ska du välja med senap? Ja eller Nej")
#     if senap == "Ja":
#         print("senap")
#     else:
#         print("No senap")

#     vegetariskt = input("önkar du vegetariskt mat? Ja eller Nej")
#     if vegetariskt == "Ja":
#         print("vegetariskt")
#     else:
#         print()


# def grill():
#     grill = input("Det finns lövbiff,kycklingspett,schnitzel,chicken nuggets \
#                 och grillad kyckling till priset av 130,110,120,95 och 115 respektive").lower()

#     if grill == "lövbiff":
#         sas = input("välja bearnaisesas,vitlöksas eller vitlökssmör \
#                     —Det gar ocksa att fã en exktra lövbit till priset av 50 kr")
#         if sas in ["bearnaisesas", "vitlöksas", "vitlökssmör"]:
#             grill_price = 130 + 50
#         else:
#             grill_price = 130

#     elif grill == "kycklingspett":
#         grill_price = 110

#     elif grill == "schnitzeln":
#         grill_price = 120
#         sas = input("vill du ha remouladsas eller majonäs? ")
#         if sas == "remouladsas":
#             print("remouladsas")
#         else:
#             print("majonäs")

#     elif grill == "chicken nuggets":
#         sas = input("Till chicken nuggets ingar det en dipp. \
#                     Du far välja mellan sweet and sour,BBQ, taco,vitlök eller Szechuan.")
#         print(sas)
#         extra_sas = input("Det är möjligt att fa ett flertal extra dipp-saser \
#                         till priset av 5 kr , vill du ha? Mata in dipp namn ellr Nej")
#         if extra_sas in ["sweet and sour", "BBQ", "taco", "vitlök", "Szechuan"]:
#             print(extra_sas)
#             grill_price = 95 + 5 
#         else:
#             grill_price = 95

#     elif grill == "grillad kyckling":
#         grill_price = 115

#     print(f"You ordered {grill} and price is {grill_price}.")

# # vill du ha någon anant?

# if order == "hamburgare":
#     hamburgare()

# if order == "grill":
#     grill()
    


# # total_price = hamburgare_price + korv_price + pizza_price + falafel_price + grill_price + vegetariskt_price
# # print(total_price)

# # ------------------------------------------

# # uppgift 17 Badhuset

# huvudmeny = input("Hej, välkommen till huvudmenyn. \
#                   Om du vill börja ett nytt köp vänligen tryck på Ja, annas tryck på Avsluta.")
# if huvudmeny == "Ja":
#     medlem = input("Vilken typ av badare är det? \n barn: 50kr \n vuxen: 100kr \n pensionär: 70kr \n student: 70kr")
#     if medlem == "barn":
#         print("Ett barn till priset av 50kr")
#     elif medlem == "vuxen":
#         print("En vuxen person till priset av 100kr")
#     elif medlem == "pensionär":
#         print("En pensionär till priset av 70kr")
#     elif medlem == "student":
#         num <= 9999 and num >= 1000
#         if student_id in ['A'+ str(num), 'D', 'E']:
#             print("Z 等于 A 或 D 或 E")
        

# else:
#     print( "Avsluta")


# # ------------------------------------------

# # uppgift 18 Andersson's frukt och grönt system för kund

# print("Hej, välkommen till Andersson's frukt och grönts huvudmeny!")
# print("Vindruvor 20kr klase  Vitlök 25kr st \
#       Vattenmelon 70kr st Mandarin 23kr/kg \
#       Citron 6 kr st \
#       Banan 28kr/kg \    
#       Annanas 45 kr st \
#     Mango 30 kr st  \ 
#     Apple  32kr/kg\
#     Kiwi 7kr st
#     Tomat 26kr/kg
#     Kokosnöt 60kr st
#     Avokado 3 för 30 kr eller 13 kr st Äggplanta 20kr st
#     Potatis  13kr/kg
#     Chilipeppar  199kr/kg Paprika  59kr/kg
#     Broccoli")



# ---------------------------------------------------------

# LabbHamburgare

# huvud menu
def print_menu():
    print("Välkommen till Snabbmatskedjan!\n")
    print("Meny:")
    print("1. Hamburgare")
    print("2. Korv med bröd")
    print("3. Pizza")
    print("4. Kebab/falafel")
    print("5. Grill")
    print("6. Vegetariskt")
    print("0. Avsluta och skriv ut kvitto\n")

# 1.Hamburgare
def hamburgare(totalpris):
    print("\nHamburgare:")
    print("1. Vanlig burgare - 25 kr")
    print("2. Ostburgare - 39 kr")
    print("3. Dubbelburgare - 55 kr")

    burgarval = int(input("Välj hamburgare (1-3): "))
    if burgarval == 1:
        totalpris += 25
        print("Vanlig burgare - 25 kr")
    elif burgarval == 2:
        totalpris += 39
        print("Ostburgare - 39 kr")
    elif burgarval == 3:
        totalpris += 55
        print("Dubbelburgare - 55 kr")

    vego_burgare = input("Vill du ha vegofärs? (ja/nej): ").lower()
    if vego_burgare == "ja":
        print("Vegoburgare vald.")
    gurka = input("Vill du ha gurka? (ja/nej):").lower()
    if gurka == "ja":
        print("Gurka tillagd.")
    ketchup_senap = input("Vill du ha ketchup/senap? (ja/nej):").lower()
    if ketchup_senap == "ja":
        print("Tetchup/Senap tillagd")
    
    # Fråga om användaren vill beställa fler burgare
    # fler_burgare = input("Vill du lägga till fler burgare? (ja/nej):").lower()
    # if fler_burgare != "ja":
    #     break

# 2.Korv med bröd
def korv_bröd(totaopris):
    print("\nKorv med bröd:")
    print("En varmkorv - 20 kr")
    totaopris += 20
    
    ketchup = input("Vill du ha ketchup? (ja/nej): ")
    if ketchup == "ja":
        print("ketchup tillagd")
    senap = input("Vill du ha senap? (ja/nej): ")
    if senap == "ja":
        print("senap tillagt")

    # Rostad lök med möjlighet att lägga till fler portioner
    rostad_lök = input("vill du ha Rostad lök? pris är 5 kr. (ja/nej):").lower()
    while rostad_lök == "ja":
        print("Rostad lök tillagt")
        totaopris += 5
        rostad_lök = input("Vill du ha mer rostad lök? (+5 kr) (ja/nej): ").lower()


    räksallad = input("vill du ha Räksallad? pris är 15 kr. (ja/nej):").lower()
    while räksallad == "ja":
        print("Räksallad tillagt")
        totaopris += 15
        räksallad = input("Vill du ha mer räksallad? (+15 kr) (ja/nej): ").lower()

# 3.Pizza
def pizza(totalpris):
    print("\nPizza:")
    print("1. Margherita - 100 kr")
    print("2. Vesuvio - 110 kr")
    print("3. Funghi - 110 kr")
    print("4. Kebab pizza - 125 kr")
    print("5. Salami - 135 kr")

    pizzaval = int(input("Välj pizza (1-5): "))

    if pizzaval == 1:
        pizza_pris = 100
    elif pizzaval == 2:
        pizza_pris = 110
    elif pizzaval == 3:
        pizza_pris = 110
    elif pizzaval == 4:
        pizza_pris = 125
    elif pizzaval == 5:
        pizza_pris = 135

    lunchtid = input("Är det lunchtid? (ja/nej): ").lower()

    if lunchtid == "ja":
        if pizzaval == 1:
            pizza_pris = 80
        elif pizzaval == 2:
            pizza_pris = 90
        elif pizzaval == 3:
            pizza_pris = 90
        elif pizzaval == 4:
            pizza_pris = 110
        elif pizzaval == 5:
            pizza_pris = 115

    totalpris += pizza_pris

    # Kebab pizza
    if pizzaval == 4:
        vit_sas = input("Vill du ha vit sås? (ja/nej): ").lower()
        if vit_sas == "ja":
            print("Vit sås tillagd.")
        rod_sas = input("Vill du ha röd sås? (ja/nej): ").lower()
        if rod_sas == "ja":
            print("Röd sås tillagd.")

    # Lägg till extra ingredienser
    while True:
        print("\nExtra ingredienser (+10 kr per val):")
        print("1. Jalapeno")
        print("2. Extra ost")
        print("3. Bacon")
        print("4. Oliver")
        print("5. Kebab eller extra skinka (+25 kr)")

        extra_val = int(input("Välj en extra ingrediens (1-5), eller 0 för att avsluta: "))

        if extra_val == 1:
            totalpris += 10
            print("Jalapeno tillagd.")
        elif extra_val == 2:
            totalpris += 10
            print("Extra ost tillagd.")
        elif extra_val == 3:
            totalpris += 10
            print("Bacon tillagd.")
        elif extra_val == 4:
            totalpris += 10
            print("Oliver tillagd.")
        elif extra_val == 5:
            totalpris += 25
            print("Kebab eller extra skinka tillagd.")
        elif extra_val == 0:
            break   # Avsluta loopen om användaren inte vill lägga till fler ingredienser
        else:
            print("Ogiltigt val, vänligen försök igen.")

    # Visa totalpris för den specifika pizzabeställningen
    print(f"\nDin totala summa för pizzan är {totalpris} kr.\n")    

# 4.Kebab/falafel
def kebab_falafel(totalpris):
    print("\nKebab/falafel:")
    print("En kebab/falafel - 95 kr")
    totaopris += 95

    ris = input("Vill du ha ris istället för pommes frites? (ja/nej): ").lower()
    if ris == "ja":
        print("Ris tillagd.")

    ta_bort_lok = input("Vill du ta bort löken? (ja/nej): ").lower()
    if ta_bort_lok == "ja":
        print("Lök borttagen.")

    rod_sas = input("Vill du ha röd sås? (ja/nej): ").lower()
    if rod_sas == "ja":
        print("Röd sås tillagd.")

    vit_sas = input("Vill du ha vit sås? (ja/nej): ").lower()
    if vit_sas == "ja":
        print("Vit sås tillagd.")

# 5.Grill
def grill(totalpris):
    print("\nGrill:")
    print("1. Lövbiff - 130 kr")
    print("2. Kycklingspett - 110 kr")
    print("3. Schnitzel - 120 kr")
    print("4. Chicken nuggets - 95 kr")
    print("5. Grillad kyckling - 115 kr")

    grillval = int(input("Välj grillalternativ (1-5): "))

    if grillval == 1:
        grill_pris = 130
    elif grillval == 2:
        grill_pris = 110
    elif grillval == 3:
        grill_pris = 120
    elif grillval == 4:
        grill_pris = 95
    elif grillval == 5:
        grill_pris = 115

    totalpris += grill_pris

    if grillval == 1:    # Lövbiff
        print("Välj sås:")
        print("1. Bearnaisesås")
        print("2. Vitlökssås")
        print("3. Vitlökssmör")

        sasval = int(input("Välj sås (1-3): "))
        print("Sås tillagd.")

        extra_lovbit = input("Vill du ha en extra lövbit (+50 kr)? (ja/nej): ").lower()
        if extra_lovbit == "ja":
            totalpris += 50

    elif grillval == 3:  # Schnitzel
        print("Välj sås:")
        print("1. Remouladsås")
        print("2. Majonäs")
        sasval = int(input("Välj sås (1-2): "))
        print("Sås tillagd.")

    elif grillval == 4:  # Chicken nuggets
        print("Välj dipp:")
        print("1. Sweet and sour")
        print("2. BBQ")
        print("3. Taco")
        print("4. Vitlök")
        print("5. Szechuan")
        dippval = int(input("Välj dipp (1-5): "))
        print("Dipp tillagd.")

        extra_dipp = input("Vill du ha extra dipp (+5 kr)? (ja/nej): ").lower()
        if extra_dipp == "ja":
            print("Välj dipp:")
            print("1. Sweet and sour")
            print("2. BBQ")
            print("3. Taco")
            print("4. Vitlök")
            print("5. Szechuan")
            dippval = int(input("Välj dipp (1-5): "))
            print("Dipp tillagd.")
            totalpris += 5

# 6.Vegetariskt
def vegetariskt(totalpris):
    print("\nVegetariskt:")
    print("1. Vegoburgare - 39 kr")
    print("2. Falafel - 45 kr")
    print("3. Vegansk pizza - 100 kr")

    vegoval = int(input("Välj vegetariskt alternativ (1-3): "))

    if vegoval == 1:
        vego_pris = 39
    elif vegoval == 2:
        vego_pris = 45
    elif vegoval == 3:
        vego_pris = 100

    totalpris += vego_pris

# Tänk på utanför huvudloopen för att samla alla köp
#Menyn körs om och om igen tills användaren säger annat

def main():
    totalpris = 0
    while True:
        print_menu()
        val = int(input("\nVälj ett alternativ från menyn (1-6): "))
        
        if val == 1:
            while True:
                hamburgare(totalpris)
                fler_burgare = input("Vill du lägga till fler burgare? (ja/nej):").lower()
                if fler_burgare != "ja":
                    break
        elif val == 2:
            korv_bröd(totalpris)
        elif val == 3:
            pizza(totalpris)
            fler_pizzor = input("Vill du beställa en till pizza? (ja/nej): ").lower()
            if fler_pizzor != "ja":
                break
        elif val == 4:
            kebab_falafel(totalpris)
            fler_kebab = input("Vill du beställa en till kebab? (ja/nej): ").lower()
            if fler_kebab != "ja":
                break
        elif val == 5:
            grill(totalpris)
            fler_grill = input("Vill du beställa en till grillrätt? (ja/nej): ").lower()
            if fler_grill != "ja":
                break
        elif val == 6:
            vegetariskt(totalpris)
            fler_vego = input("Vill du beställa en till vegorätt? (ja/nej): ").lower()
            if fler_vego != "ja":
                break
        else:
            print("Ogiltigt val, vänligen försök igen.")

        # Fråga om användaren vill fortsätta
        fortsätta = input("Vill du beställa något annat? (ja/nej): ").lower()
        if fortsätta != "ja":
            print("Tack för ditt köp!")
            break

    # Visa totalpris
    print(f"\nDin totala summa är {totalpris} kr.\n")



# 问老师关于  1.打印总价格 应该在循环里面还是外面. 在里面外面都可以。














