

tribonachi, index_counter = [], 0
for cycle in range(int(input())):
	if len(tribonachi) < 3:
		tribonachi.append(1)
	else:
		sequence = sum(tribonachi[0+index_counter:len(tribonachi):1])
		tribonachi.append(sequence)
		index_counter += 1
print(*tribonachi)

