
# DNK, RNK = ['A', 'C', 'G', 'T'], ['U', 'G', 'C', 'A']
# print("".join([RNK[DNK.index(char)] for char in list(input())]))

print( "".join([dict(zip(['A', 'C', 'G', 'T'], ['U', 'G', 'C', 'A']))[char] for char in input()]))
