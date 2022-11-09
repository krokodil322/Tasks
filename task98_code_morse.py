letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', 
		 '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', 
		 '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', 
		 '...--', '....-', '.....', '-....', '--...', '---..', '----.']
letters_morse = dict(zip(letters, morse))
print(*[letters_morse[char] for char in list(input().upper()) if char not in "' ',.+=?!-"])

