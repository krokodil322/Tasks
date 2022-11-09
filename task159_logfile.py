from datetime import timedelta as td

def check_time(pack: list) -> bool:
	times = list(map(lambda item: list(map(int, item.split(':'))), pack[1:]))
	time1 = td(hours=times[0][0], minutes=times[0][1])
	time2 = td(hours=times[1][0], minutes=times[1][1])
	difference = str(time2 - time1).split(':')[0]
	if int(difference) >= 1:
		return True
	else:
		return False
	
with open("logfile.txt", encoding="utf-8") as torrent:
	data = [item.strip().split(', ') for item in torrent.readlines()]
	data = list(filter(lambda pack: check_time(pack), data))

with open("output.txt", 'w', encoding="utf-8") as torrent:
	torrent.writelines([item[0] + '\n' for item in data])