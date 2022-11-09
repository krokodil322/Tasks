

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
	
print(chunked([char for char in input().split()], int(input())))

input()