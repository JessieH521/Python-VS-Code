
import arithmetic

import geometry

# testa arithmetic funktionerna

print(arithmetic.add(5, 6))
print(arithmetic.subtract(10, 5))

# testa geometry funktionerna

print(geometry.area_of_circle(5))
print(geometry.perimeter_of_circle(5))



# - Använd alias för att importera add från arithmetic.py 
# som summa och subtract som differens i din main-fil.

from arithmetic import add as ad
from arithmetic import subtract as sub

print(ad(7, 8))
print(sub(9, 5))

# --------------------------------------------

# 老师的代码

from arithmetic import add, subtract
from geometry import areaCircle, perimeterCircle


# Testa arithmetic-funktionerna

sum_result = add(5, 3)
difference_result = subtract(5, 3)


# Testa geometry-funktionerna

circle_perimeter = perimeterCircle(5)
circle_area= areaCircle(5)


print(f"Summa: {sum_result}")
print(f"Differens: {difference_result}")
print(f"Omkrets av cirkel: {circle_perimeter:.2f}")
print(f"Area av cirkel: {circle_area:.2f}")


# Extra Utmaning: 挑战

from arithmetic import add as summa, subtract as differens
from geometry import areaCircle, perimeterCircle


# Testa arithmetic-funktionerna

sum_result = summa(5, 3)
difference_result = differens(5, 3)


# Testa geometry-funktionerna

circle_perimeter = perimeterCircle(5)
circle_area= areaCircle(5)


print(f"Summa: {sum_result}")
print(f"Differens: {difference_result}")
print(f"Omkrets av cirkel: {circle_perimeter:.2f}")
print(f"Area av cirkel: {circle_area:.2f}")




