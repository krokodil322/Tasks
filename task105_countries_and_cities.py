

countries_and_city = dict()
for item in [[name for name in input().split()] for _ in range(int(input()))]:
	countries_and_city[item[0]] = item[1:]

for city in [city for _ in range(int(input())) for city in input().split()]:
	for key, values in countries_and_city.items():
		if city in values:
			print(key)



