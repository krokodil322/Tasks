
with open("goats.txt", encoding="utf-8") as torrent:
    #БЕРЁМ ВЕСЬ ФАЙЛ
	data = [item.strip() for item in torrent.readlines()]
	stop_word = data.index("GOATS")
	#СОЗДАЁМ СЧЁТЧИК КОЗЛИКОВ
	goats = {item: 0 for item in data[1:stop_word]}	
    #СЧИТАЕМ КОЗЛИКОВ
	for item in data[stop_word + 1:]:
		goats[item] += 1
	#СПРАШИВАЕМ ЖАКА ФРЕСКО 
	quan_goats = sum(map(int, goats.values()))	
	result = [key for key, value in goats.items() if (value / quan_goats) > 0.07]
	
with open("answer.txt", 'w', encoding="utf-8") as torrent:
    torrent.writelines([item + '\n' for item in sorted(result)])