

# 方式1:
# 当你在 main.py 中执行 from my_func import adder 时，Python 会首先执行 my_func.py 文件中的所有顶级代码。
# 这意味着 my_func.py 中的 print("Greetings from my_func.") 语句会被执行


def adder(a, b):
    return a + b

print("Greetings from my func.")     # 这条信息会在模块被导入时执行 


# 方式2:  if __name__ == "__main__":
# 只有作为自己 主程序执行时 Greetings from my func. 才会被执行。 其他文件中不会显示

# def adder(a, b):
#     return a + b

# if __name__ == "__main__":
#     print("Greetings from my func.")      # # 仅在直接运行该文件时打印

#--------

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








































