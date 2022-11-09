abscissas = [float(point) for point in input().split()]
ordinates = [float(point) for point in input().split()]
applicates = [float(point) for point in input().split()]
coords = zip(abscissas, ordinates, applicates)

result = all(map(lambda points: True if sum([pow(point, 2) for point in points]) <= 4 else False, coords))
print(result)