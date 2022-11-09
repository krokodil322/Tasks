d = {
    'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch',
    'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*',
    'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je',
    'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya'
    }

with open("cyrillic.txt", encoding="utf-8") as torrent:
    data = "".join(torrent.readlines())
# print(data)

result, keys = str(), d.keys()
for word in data:
    for char in word:
        if char.lower() in keys and char.isupper():
            result += d[char.lower()].capitalize()
        elif char.lower() in keys and char.islower():
            result += d[char.lower()]
        else:
            result += char

with open("transliteration.txt", 'w', encoding="utf-8") as torrent:
    torrent.write(result)