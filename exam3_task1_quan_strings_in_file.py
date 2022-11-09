with open("ledger.txt", encoding="utf-8") as torrent:
    print('$' + str(sum([int(item[1:].strip()) for item in torrent.readlines()])))
