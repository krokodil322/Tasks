
print(len(set(("".join([item.lower() for item in input() if item not in [',', '.', ':', ';', '-', '?', '!']])).split())))