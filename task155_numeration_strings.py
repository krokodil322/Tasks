

with open("input.txt", encoding="utf-8") as take, open("output.txt", "w", encoding="utf-8") as put:
	put.writelines([f'{pack[0] + 1}) ' + pack[1] for pack in enumerate(take.readlines())])
