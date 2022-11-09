
def index_of_body_weight(weight: float, growth: float) -> None:
	index = weight / (growth)**2

	if index >= 18.5 and index <= 25:
		print("Оптимальная масса")
	elif index < 18.5:
		print("Недостаточная масса")
	elif index > 25:
		print("Избыточная масса")

index_of_body_weight(input(), input())
