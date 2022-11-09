

def spell(*args: list) -> dict:
	result = dict() 
	for item in [{word[0]: len(word)} for word in [word.lower() for word in args]]:
		for key, value in item.items():
			if value > result.get(key, -1):
				result[key] = value		
	return result

mylist = ['россия', 'Австрия', 'австралия', 'РумыниЯ', 'Украина', 'КИТай', 'УЗБЕКИСТАН']
print(spell(*mylist))
words = ['fruit', 'football', 'February', 'forest', 'Family']
print(spell(*words))