
# # uppgift 1  Fordon 车辆

# class Fordon:
#     def __init__(self, märke, modell, year):
#         self.märke = märke
#         self.modell = modell
#         self.year = year

#     def start(self):
#         return f'{self.märke} {self.modell} från {self.year} har startat.'

#     def stop(self):
#         return f'{self.märke} {self.modell} från {self.year} har stannat.'

#     def tanka(self):   # 加油
#         return f'{self.märke} {self.modell}  tankas.'

# # Cykelklass, som ärver från Fordon        
# class Bil(Fordon):
#     def __init__(self, märke, modell, year, antal_door):
#         super().__init__(märke, modell, year)
#         self.antal_door = antal_door
 
#     def tuta(self):     # 叫
#         return f'{self.märke} {self.modell} tutar.'

# class Cykel(Fordon):
#     def __init__(self, märke, modell, year, num_gears):
#         super().__init__(märke, modell, year)
#         self.num_gears = num_gears

#     def ringklockan(self):
#         return f'{self.märke} {self.modell} ringer i ringklockan.'

# # Motorcykelklass, som ärver från Fordon
# class Motorcykel(Fordon):
#     def __init__(self, märke, modell, year, type_motor):
#         super().__init__(märke, modell, year)
#         self.type_motor = type_motor

#     def start(self):
#         return f'{self.märke} {self.modell} {self.type_motor} från {self.year} har startat.'

#     def stop(self):
#         return f'{self.märke} {self.modell} {self.type_motor} från {self.year} har stannat.'  
    
#     def typeMotor(self):
#         return f'{self.märke} {self.modell} {self.type_motor} med {self.type_motor}cc motor varvar motorn.'

#     def fuel_up(self):
#         print('{self.märke} {self.modell} tankas.')


# bil = Bil("Toyota", "Corolla", 2020, 4)
# cykel = Cykel("Crescent", "Sting", 2022, 2)
# motorcykel = Motorcykel("Harley-Davidson", "Street", 2019, 750)

# # bil
# print(bil.start())
# print(bil.tuta())
# print(bil.stop())

# # cykel
# print(cykel.start())
# print(cykel.ringklockan())
# print(cykel.stop())

# # motorcykel
# print(motorcykel.start())
# print(motorcykel.typeMotor())
# print(motorcykel.stop())

# -----------------------------------------

# uppgift 2  Polymorfism 多态

import math

class Shapes:
    
    def area(self):
        return 'Olika grafik har olika sätt att beräkna area.'

    def perimeter(self):
        return 'Olika former har olika metoder för att beräkna omkrets.'
        

class Cirkel(Shapes):
    def __init__(self, radie):
        self.radie = radie

    def area(self):
        area = self.radie ** 2 * math.pi
        return f"Area of the cirkel is {area}"
    
    def perimeter(self):
        perimeter = self.radie * 2 * math.pi
        return f"Perimeter of the cirkel is {perimeter}"

class Rektangel(Shapes):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        return f"Area of the Rektangel is {area}"
    
    def perimeter(self):
        perimeter = self.length * 2 + self.width * 2
        return f"Perimeter of the Rektangel is {perimeter}"
        
class Triangel(Shapes):
    def __init__(self, side1, side2, bottom, height):
        self.side1 = side1
        self.side2 = side2
        self.bottom = bottom
        self.height = height

    def area(self):
        area = (self.bottom * self.height) / 2
        return f"Area of the Triangel is {area}"
    
    def perimeter(self):
        perimeter = self.side1 + self.side2 + self.bottom
        return f"Perimeter of the Triangel is {perimeter}"


cirkel = Cirkel(10)
rektangel = Rektangel(10, 20)
triangel = Triangel(10, 10, 10, 10)


form = [cirkel, rektangel, triangel]

for shape in Shapes:
    print(f"Form: {shape.__class__.__name__}")
    print(f"area: {shape.area()}")
    print(f"perimeter: {shape.perimeter()}")



# # 另一种方法
# for shape in Shapes:
#         print(f"Form: {shape.__class__.__name__}")    # 取类的名称
#         print(f"Area: {shape.area():.2f}")            # 取面积 小数点后2位
#         print(f"Omkrets: {shape.perimeter():.2f}")
#         print("-" * 30)


































