country = input('please input your country: ')
age = input('please input your age: ')
age = int(age)
if country == 'Taiwan':
	if age >= 18:
		print('you can have a driving licence')
	else:
		print('you cannot have a driving licence yet')
elif country == 'USA':
	if age >= 16:
		print('you can have a driving licence')
	else:
		print('you cannot have a driving licence yet')
else:
	print('you can only input Tawain and USA')