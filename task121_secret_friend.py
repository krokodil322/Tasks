import random

persons = dict()
for _ in range(int(input())):
	persons.setdefault(input(), None)

for key in persons.keys():
	while persons.get(key) is None:
		secret_friend = random.choice(list(persons.keys()))
		if (key != secret_friend) and (secret_friend not in list(persons.values())):
			persons[key] = secret_friend

for key, value in persons.items():
	print(key, value, sep=" - ")s