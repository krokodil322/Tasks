input_data = [int(item) for item in input().split()]
print( len(input_data) - len( set(input_data) ) )