
# def function_a():
#     print("Function A i test1.")
#     from test2 import function_b
#     function_b()

# function_a()





# Cirkulära beroenden (circular imports)
# 当两个或多个模块直接或间接相互导入时，就会发生循环导入（circular import），这可能会导致错误或导致程序崩溃
# a 和 b 相互 import 对方 会导致错误 


from test2 import function_b

def function_a():
    from test2 import function_b
    print("Function A i test1.")
    function_b()

# Sena imports (Lazy imports) 惰性导入
# En vanlig lösning för att undvika cirkulära beroenden är att använda sena imports, 
# där du importerar den nödvändiga funktionen inuti en funktion snarare än högst upp i modulen. 
# Detta försäkrar att importen endast sker när den faktiskt behövs, 
# vilket ofta kan kringgå cirkulära beroenden.





















