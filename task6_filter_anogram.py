

def filter_anagrams(word: str, anograms: list) -> list:
	return [item for item in anograms if sorted(list(word)) == sorted(list(item))]
				
print(filter_anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))

