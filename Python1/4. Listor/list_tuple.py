

# my_list = [0, 1, 2, "0", "Text", True]

# -------------------------------

# name = "Kalle"

# my_list = [1, 2, 3, name]
# print(my_list)

# -------------------------------

# my_list = [1, 2, 3, '0', "Text", True]
# print(my_list[5])

# -------------------------------

# my_list = [1, 2, 3, '0', "Text", True]
# print(my_list[1:])
# print(my_list[:3])     # Slicing
# print(my_list[:])
# print(my_list[-1])
# print(my_list[:-1])
# print(my_list[::2])    #隔一个一显示
# print(my_list[::-1])     # 倒序 Omvänt


# ----------------------------------

# Concatinate(Sammanfoga)  连接 合并

# my_list = [1, 2, 3, '0', "Text", True]

# print(my_list + ["New item"])

# my_list = my_list + ['new item']
# print(my_list)
# print(my_list * 2)

# ----------------------------------

# Metoder 方法

# list.pop() 是去掉最后一个值
# list.pop(序列)， list.pop(0) 是去掉第一个值

# list = [1, 2, 3]

# list.append('append me')
# # list.pop()      # 删掉最后一个
# list.pop(1)     # 删掉第二个
# print(list)

# popped_item = list.pop(0)   # 删除列表中的第一个元素 1，并将它赋值给变量 popped_item
# print(popped_item)    # 打印出删除的元素，也就是 1。

# list = [1, 2, 3]

# # print(list[10])

# list.append("append me")
# print(list)

# list.remove("append me")
# print(list)

new_list = ['a', 'e', 'x', 'b', 'c']

# new_list.reverse()
# print(new_list)

# new_list.sort()
# print(new_list)

new_list.sort(reverse=True)
print(new_list)


# ------------------------------------

# Tuples 元组 () parentheses

# my_tuple = (1, 2, 3)

# print(len(my_tuple))    # len() 有几个元素

# ------------------------------------

# my_tuple = (1, 2, 3, 'four')

# print(my_tuple)

# # index 

# print(my_tuple[2])

# ------------------------------------

# my_tuple = (1, 2, 3, 'four', 3)

# print(my_tuple.index('four'))   # 打印 four 所在的索引

# print(my_tuple.count(3))   # 看3出现几次


# ------------------------------------

# # Tuple 不能更改 x

# my_tuple = (1, 2, 3, 'four')

# my_tuple[0] = 5      
# my_tuple.append(4)

# print(my_tuple)

# ------------------------------------

# 想改变 tuple 先把它变成 1.列表； 2. tuple 里加 列表 然后填入数据

# my_tuple = (1, 2, 3, 'four')
# my_list = list(my_tuple)

# print(my_list)

# my_tuple = (1, 2, 3, 'four', [])
# my_tuple[-1].append("Kommer funka!")

# print(my_tuple)

# ------------------------------------

# my_tuple2 = (5,) 在 Python 中，当定义只有一个元素的元组时，
# 必须在该元素后面加一个逗号 ,，否则 Python 会把它识别为一个普通的值，而不是元组。

# my_tuple = (1, 2, 3, 'four')
# my_tuple2 = (5,)
# my_tuple3 = my_tuple + my_tuple2
# print(my_tuple3)










































