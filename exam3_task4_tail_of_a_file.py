with open("text.txt", encoding="utf-8") as torrent:
	print(*reversed([item.strip() for item in torrent.readlines()[-1:-11:-1]]), sep='\n')