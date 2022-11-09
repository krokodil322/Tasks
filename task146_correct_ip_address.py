import string

ip_address = [oktet for oktet in input().split('.')]
status = all(map(lambda oktet: True if oktet.isdigit() else False, ip_address))
print(all(map(lambda oktet: True if int(oktet) <= 255 and int(oktet) >= 0 else False, ip_address)) if status else False)

