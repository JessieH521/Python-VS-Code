
# 方法 1
# from math import sqrt         # kvadratrot  / Square root
# print(sqrt(25))

# 方法 2   这个经常使用     # 在math下没有import 具体方法时，  调用时需要 加上 math.
# import math     
# print(math.sqrt(25))

# 方法 3
# from math import * 是一种导入 Python math 模块中所有函数和常量的方法。
# 使用这个语句后，你可以直接使用 math 模块中的所有函数和常量，而不需要在它们前面加上 math. 前缀。

# from math import *

# from math import sqrt as sq
 
# ---------------------------------------------------

# from math import sqrt 
# import math  

# def sqrt(x):
#     return "hej"

# print(sqrt(25))
# print(math.sqrt(25))

# ---------------------------------------------------

# from math import sqrt as sq

# print(sq(25))

# ---------------------------------------------------


# 我们有两个文件：
# my_func.py - 定义了 adder 函数。
# main.py - 导入并调用 adder 函数。

# 执行顺序
# 1. 导入模块：
# 当你在 main.py 中执行 from my_func import adder 时，Python 会首先执行 my_func.py 文件中的所有顶级代码。
# 这意味着 my_func.py 中的 print("Greetings from my_func.") 语句会被执行。
# 2. 调用函数：
# 然后，adder 函数被成功导入，接着在 main.py 中执行 print(adder(2, 3))，这会计算并打印 2 和 3 的和。

# 因此，运行 main.py 后的输出将是：
# Greetings from my func.
# 5

# 如何避免导入时打印问候语
# 如果你希望在导入 my_func 模块时不打印问候语，可以将 print 语句放入 if __name__ == "__main__": 块中。
# 这样，只有当 my_func.py 作为主程序运行时才会打印问候语：
# if __name__ == "__main__":后，你运行 main.py，输出将是：5

# 通过使用 if __name__ == "__main__":，你可以控制哪些代码在模块被导入时执行，避免不必要的打印。


# from my_func import adder

# print(adder(2, 3))


# ---------------------------------------------------

# 应该是在其他文档中吧 ?????

# import sys

# print(sys.path)

# import os

# sys.path.append(os.path.absp)





















































