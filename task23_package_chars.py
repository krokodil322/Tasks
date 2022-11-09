string = input().split()

package_char = [[] for cycle in range(len(string))]
index, before_char = 0, string[0]
for char in string:
	if before_char is char:
		package_char[index].append(char)
	else:
		before_char = char
		index += 1
		package_char[index].append(char)
	
package_char = [item for item in package_char if len(item) != 0]
print(package_char)
