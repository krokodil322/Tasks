

user_word = input() + ' запретил букву'
ALPHABET = [chr(i) for i in range(1072, 1104)]

for letter in ALPHABET:
    if letter in user_word:
        print(user_word, letter)
        user_word = user_word.replace(letter, '').replace('  ', ' ').strip()
	
	


# print(result)
		
		
		
