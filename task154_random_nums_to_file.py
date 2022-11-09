from random import randrange

with open("random.txt", "w", encoding="utf-8") as torrent:
	torrent.writelines([str(randrange(111, 778)) + "\n" for _ in range(25)])


