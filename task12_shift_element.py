user_nums = [num for num in input().split()]
user_nums.insert(0, user_nums.pop(-1))
print(" ".join(user_nums))