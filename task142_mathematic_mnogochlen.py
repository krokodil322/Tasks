
An, x = list(reversed(list(map(int, input().split())))), int(input())
powers = range(0, len(An))
polynom = map(lambda a, pow_: a*(x)**pow_, An, powers)
print(sum(list(polynom)))
