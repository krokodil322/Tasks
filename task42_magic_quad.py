size = int(input())
matrix = [[int(item) for item in input().split()] for _ in range(size)]
status, one_time = True, True
check_repeat_nums = [[matrix[r][c] for c in range(size)] for r in range(size)]
before_num = check_repeat_nums[0][0]
check_repeat_nums[0].pop(0)
for i in range(size):
	if before_num in check_repeat_nums[i] or (0 in check_repeat_nums[i]):
		status = False
		break
if status is True:
	row_sum = [sum(item) for item in matrix]
	column_sum = [sum([matrix[r][c] for r in range(size)]) for c in range(size)]
	main_diagonal_sum = sum([matrix[i][i] for i in range(size)])
	auxiliary_diagonal_sum = sum([matrix[i][size - i - 1] for i in range(size)])
	for r_sum, c_sum in zip(row_sum, column_sum):
		if r_sum != main_diagonal_sum or c_sum != main_diagonal_sum or main_diagonal_sum != auxiliary_diagonal_sum:
			status = False
			print("NO")
			break
	if status is True:
		print("YES")
else:
	print("NO")
