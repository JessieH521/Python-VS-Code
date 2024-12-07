
# Cirkulära beroenden (circular imports)
# 当两个或多个模块直接或间接相互导入时，就会发生循环导入（circular import），这可能会导致错误或导致程序崩溃
# a 和 b 相互 import 对方 会导致错误 

# from test1 import function_a

# def function_b():
#     print("Function B i test2.")
#     function_a()




def function_b():
    print("Function B i test2.")
    from test1 import function_a
    function_a()


function_b()







