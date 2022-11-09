

# files_pc = { for _ in range(int(input())) for item in input().split()}

options_resp, files_pc = {"write": 'W', "read": 'R', "execute" :'X'}, dict()
for  _ in range(int(input())):
	input_data = input().split()
	files_pc.setdefault(input_data[0], input_data[1:])

responses, for_output = dict(), list()
for  _ in range(int(input())):
	input_data = input().split()
	for_output.append(input_data[1])
	responses.setdefault(input_data[1], []).append(input_data[0])

result = dict()
for key, value in responses.items():
	for val in value:
		if (files_pc.get(key) is not None) and (val in list(options_resp.keys())):
			if options_resp.get(val) in files_pc.get(key):
				# print(f"{val} {key} {files_pc.get(key)} OK")
				result.setdefault(key, []).append(options_resp.get(val))
			else:
				result.setdefault(key, []).append(False)


for file in for_output:
	index = 0
	for key, value in result.items():
		if file == key:
			if (result.get(key).pop(0) is not False):
				print("OK")
			else:
				print("Access denied")


# print(options_resp)
# print(files_pc)
# print(responses)
# print()
# print()
# print(result)
# print(for_output)