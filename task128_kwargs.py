# def info_kwargs(**kwargs) -> None:
#     kwargs = sorted(kwargs.items())
#     for pack in kwargs:
#         key, value = pack
#         print(key, value, sep=": ")
    

# info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')  


def comparator(numbers):
    return sum(numbers) / len(numbers)


numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]
print(min(numbers, key=comparator))
print(max(numbers, key=comparator))

# points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]

# def comparator(points) -> float:
#     return (points[0]**2 + points[1]**2)**0.5


# print(sorted(points, key=comparator))

numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]

def comparator(numbers) -> int:
    return min(numbers) + max(numbers)

print(sorted(numbers, key=comparator))