# upend_num = []
# user_num = list(input())
# for item in user_num:
# 	upend_num.insert(0, item)
# if len(user_num) > 5:
# 	upend_num.insert(0, upend_num.pop(-1))
# while upend_num[0] == '0':
# 	upend_num.pop(0)
# print("".join(upend_num))
user_num = "25000"
# print(int(user_num[:-5] + user_num[-5:][::-1]))
print(int(user_num[:-5] + user_num[-1:-6:-1]))