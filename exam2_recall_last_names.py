last_names1 = {item for item in input().split()}
last_names2 = {item for item in input().split()}
print(*sorted(last_names1.union(last_names2)))

print(*sorted({item for item in input().split()}.union({item for item in input().split()})))