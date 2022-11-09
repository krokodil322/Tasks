def print_products(*args) -> None:
    counter = 1
    args = [name for name in args if (isinstance(name, str) is True) and name != '']
    if len(args) != 0:
        for name in args:
            print(f"{counter}) {name}")
            counter += 1
    else:
        print("Нет продуктов")

# print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
print_products([4], {}, 1, 2, {'Beegeek'}, '') 