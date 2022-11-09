
numbers = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 
		   5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
print(*[numbers[num_key] for num_key in [int(item) for item in input()]], end=" ")

