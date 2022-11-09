

def matrix(n:int=1, m:int=0, value:int=0) -> list:
	if m == 0:
		m = n  
	if n == 0:
		n = m

	return [[value for _ in range(m)] for _ in range(n)]

def show_matrix(matrix: list) -> None:
	for row in matrix:
		for column in row:
			print(str(column).ljust(2), end=" ")
		print()

show_matrix(matrix(n=3, value=9))