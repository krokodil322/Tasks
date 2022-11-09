

def mathematic_operations(A: int, B: int) -> None:
	if B == 0:
		raise ZeroDivisionError
	#СУММА
	print(A + B)
	#РАЗНОСТЬ
	print(A - B)
	#ПРОИЗВЕДЕНИЕ
	print(A * B)
	#ЧАСТНОЕ
	print(A / B)
	#ЦЕЛАЯ ЧАСТЬ ОТ ДЕЛЕНИЯ
	print(A // B)
	#ОСТАТОК ОТ ДЕЛЕНИЯ(МОДУЛЬ)
	print(A % B)
	#ФОРМУЛА
	print( ( (A)**10 + (B)**10 )**0.5 )

mathematic_operations(454, 322)
input()

