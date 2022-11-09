
# myset1 = {int(item) for item in input()}
# print(myset1)

items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
items = {int(item) for item in items}
print(items)

words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 
		'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']
print(*sorted({list(word)[0].lower() for word in words}))

sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when 
		   I was three, and, save for a pocket of warmth in the darkest past, nothing of her 
		   subsists within the hollows and dells of memory, over which, if you can still stand 
		   my style (I am writing under observation), the sun of my infancy had set: surely, 
		   you all know those redolent remnants of day suspended, with the midges, about some 
		   hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, 
		   in the summer dusk; a furry warmth, golden midges.'''
# if char != ['(', ',', '.', ':', ';', ')']
unique_words = {word.lower() for word in "".join([char for char in sentence if char not in ['(', ',', '.', ':', ';', ')']]).split()}
print(*sorted(unique_words))

print(*sorted({word.lower() for word in  "".join([char for char in sentence if char not in ['(', ',', '.', ':', ';', ')']]).split() if len(word) < 4}))

files = ['python.png', 'qwerty.py', 'Python.PNg', 'apple.pnG', 'zebra.PNG',  
		 'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git', 'ZeBrA.PnG']

print(*sorted({name.lower() for name in [name for name in files if "".join( list(name)[-1:-5:-1]).lower() == "gnp."]}))

print({1, 2, 3, 4, 5, frozenset({6, 8, 9, 10})})