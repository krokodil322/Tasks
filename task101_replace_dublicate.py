chars_input = [char for char in input().split()]
counter_chars = dict()
for char in chars_input:
    counter_chars[char] = 0

index = 0
for char in chars_input:
	if counter_chars[char] >= 1:
		print(char + "_" + str(counter_chars[char]), end=" ")
	else:
		print(char, end=" ")

	counter_chars[char] = counter_chars.get(char) + 1
