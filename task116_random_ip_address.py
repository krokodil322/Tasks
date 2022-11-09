import random
import string

def generate_ip() -> str:
	ip_address = str()
	for cycle in range(4):
		ip_address += str(random.randint(0, 255))
		if cycle != 3:
			ip_address += "."
	return ip_address

def generate_index() -> str:
	latveria_index = str()
	for cycle in range(1, 8):
		if cycle < 3 or cycle > 5:
			latveria_index += random.choice(string.ascii_uppercase)
		elif cycle > 2 or cycle < 6:
			if cycle != 4:
				latveria_index += str(random.randint(0, 99))
			else:
				latveria_index += '_'
	return latveria_index

print(generate_index())