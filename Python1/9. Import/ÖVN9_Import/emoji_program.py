
import emoji

print(emoji.emojize("Good morgon! Happy day!!"))

print(emoji.emojize("Good morgon! Happy day!:thumbs_up:"))

print(emoji.emojize("I love U:pizza::star-struck:"))


print(emoji.emojize("Good morgon! Happy day!:yellow_heart:"))

print("Bra jobbat!" + emoji.emojize(':broken_heart:'))


# ----------------------------------

# import emoji

# # 例如，获取 "👍" 的文本代码
# print(emoji.demojize("👍"))


# 老师的

message = emoji.emojize("Bra jobbat!:thumbs_down:, :sunglasses:, :rocket:")

good_m =emoji.emojize("Supper Bra!:thumbs_up:")

# print(message)
# print(good_m)

# svar = False

# if svar:
#     print(good_m)
# else:
#     print(message)


svar = input(" skriver something:")

if svar == "Bra":
    print(good_m)
else:
    print(message)
