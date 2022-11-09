import random

def task1() -> None:
	n = 10**6       # количество испытаний
	S, k = 16, int()
	for _ in range(n):
		x = random.uniform(-2.0, 2.0)
		y = random.uniform(-2.0, 2.0)
		if (y**2 <= 2 - 3*x) and (x**3 >= -y**4 - 2):
			k += 1
	print((k / n) * S)
	
	return None

def task2() -> None:
	S_quad, k, n, S_round = 4, int(), 10**6, int() 

	for _ in range(n):
		x = random.uniform(-1.0, 1.0)
		y = random.uniform(-1.0, 1.0)
		if y**2 <= 1 - x**2:
			k += 1

	print(((k / n) * S_quad))



	return None

task2()

