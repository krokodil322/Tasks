import random

lottery_ticket = set()
while len(lottery_ticket) != 7:
    lottery_ticket.add(random.randint(1, 49))
print(*sorted(lottery_ticket))

