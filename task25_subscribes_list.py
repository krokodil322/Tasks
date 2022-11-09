
def chunked(user_input: list, size_chunk: int) -> list:
	index, counter, package_data = 0, size_chunk, [[]]
	for item in user_input:
		while True:
			if counter != 0:
				package_data[index].append(item)
				counter -= 1
				break
			else:
				package_data.append([])
				counter = size_chunk
				index += 1
	return package_data

# user_input = input().split()
print(f"Ввод: ('A', 'B', 'C', 'D'), Уровень: 1 {chunked(['A', 'B', 'C', 'D'], 1)}")
print(f"Ввод: ('A', 'B', 'C', 'D'), Уровень: 2 {chunked(['A', 'B', 'C', 'D'], 2)}")
print(f"Ввод: ('A', 'B', 'C', 'D'), Уровень: 3 {chunked(['A', 'B', 'C', 'D'], 3)}")
print(f"Ввод: ('A', 'B', 'C', 'D'), Уровень: 4 {chunked(['A', 'B', 'C', 'D'], 4)}")
