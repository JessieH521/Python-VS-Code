# Dictionary {}

# 字典 可以在值里面写一个key 多个value 嵌套列表

# my_dictionary = {
#     1 : "value one",
#     2 : "value two",
#     3 : "value three",
#     4 : ["name_one", "name_two"]
# }

# # print(my_dictionary[4])      # 取第几位的值
# print(my_dictionary[4][0])     # 第4组第1个值 
# print(my_dictionary[4][0].upper())     # 第4组第1个值 大写

# ----------------------------------

# 字典可以更改 可以加

# my_dictionary = {
#     1 : "value one",
#     2 : "value two",
#     3 : "value three",
#     4 : ["name_one", "name_two"]
# }

# my_dictionary[1] = "updateed value one"

# print(my_dictionary)

# my_dictionary[4] += ['name_three']

# print(my_dictionary)

# ----------------------------------

# assignment

# new_dictionary = {}

# new_dictionary['animal'] = 'cat'
# new_dictionary['answer'] = 42

# print(new_dictionary)

# ----------------------------------

# nested_dictionary = {
#     "person1" : {
#         "name" : "Alice",
#         "age" : 30
#     },
#     "person2" : {
#         "name" : "Bob",
#         "age" : 25
#     }
# }

# print(nested_dictionary)

# ----------------------------------

# nested_dictionary = {
#     "person 1" : {
#         "name" : {
#             "first" : "Alice",
#             "last" : "Alisson"
#         },
#         "age" : 30
#     },
#     "person 2" : {
#         "name" : {
#             "first" : "Bob",
#             "last" : "Bobson"
#         },
#         "age" : 25
#     }
# }

# # print(nested_dictionary)
# print(nested_dictionary["person 2"]["name"]["last"])

# ----------------------------------

# Methods

# dictionary = {
#     "key 1" : 1,
#     "key 2" : 2,
#     "key 3" : 3
# }

# # print(dictionary.keys())     # key value 以列表形式展现
# # print(dictionary.values())
# print(dictionary.items())      # key - value - pair

# ----------------------------------

# Set 集合 {}

# x = set()

# x.add(1)

# print(x)

# ----------------------------------

# y = {1, 2, 3}

# y.add(4)
# print(y)

# y.add(3)      # 尽管加了一个3 但只显示1个3
# print(y)

# ----------------------------------

# set 可以去重

# my_list = [1, 2, 3, 1, 2, 3, 4, 5, 4, 6]

# print(set(my_list))

# ----------------------------------

# my_set = {"banan", "melon"}

# set.add()  向集合中只能添加单个元素。
# set.update() 向集合中添加多个元素（可以是任何可迭代对象，如列表、元组、集合等）。

# my_set.update(["kiwi", "citron"])

# # print(my_set)

# my_set.remove("banan")
# my_set.remove("apple")

# my_set.discard("melon")  
# my_set.discard("apple")

# print(my_set)

# set.discard() 是集合（set）中的一种方法，用于从集合中删除指定的元素。
# 如果该元素不存在，不会引发错误，这是它与 remove() 方法的区别。

# ----------------------------------

# for frukt in my_set:
#     print(frukt)

# print("apple" in my_set)
# print("melon" in my_set)

# my_set.clear()
# print(my_set)

# ----------------------------------

# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}

# # Union A ∪ B  A 并 B  

# print(A.union(B))
# print(A | B)

# ----------------------------------

# Snitt - "Intersection"  A 交 B  A ∩ B

# print(A.intersection(B))
# print(A & B)

# ----------------------------------

# Differens  Mängddifferens   A - B eller A \ B

# print(A.difference(B))
# print(A - B)
# # print(A \ B)

































































