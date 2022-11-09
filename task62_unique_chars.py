
# words = [len(set(item.lower())) for _ in range(int(input())) for item in input().split()]

# print(sum([len(set(item.lower())) for _ in range(int(input())) for item in input().split()]))
print(len(set([item.lower() for _ in range(int(input())) for item in input()])))
