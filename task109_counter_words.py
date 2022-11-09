

words =  input().split()
counter_words = dict.fromkeys(words, 0)
print(*[counter_words.setdefault(word, counter_words.get(word) + 1) for word in words])

# print(*[counter_words.setdefault(word, counter_words.get(word) + 1) for word in words])
for word in words:
	counter_words[word] += 1
	print(counter_words[word], end=" ")