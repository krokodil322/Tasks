nums = [set([int(item) for item in input().split()]) for _ in range(3)]
ratings = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
ratings = [ratings.difference(item) for item in nums]

nums = set(ratings[0])
for item in ratings:
	nums.intersection_update(item)

print(*nums)
