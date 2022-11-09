

def build_query_string(response: dict) -> str:
	response = {key: response.get(key) for key in sorted(list(response.keys()))}
	result, size = str(), len(response)
	for pair, ampersand in zip(response.items(), range(1, size + 1)):
		if ampersand < size:
			result += pair[0] + '=' + str(pair[1]) + '&'
		else:
			result += pair[0] + '=' + str(pair[1])
		
	return result



print(build_query_string(response = {'sport': 'hockey', 'game': 2, 'time': 17}))