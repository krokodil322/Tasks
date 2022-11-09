import random

tickets = set()
while len(tickets) != 100:
	one_ticket = str()
	for _ in range(7):
		one_ticket += str(random.randint(1, 9))
	tickets.add(one_ticket)
for ticket in tickets:
	print(ticket)