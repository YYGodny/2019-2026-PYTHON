def format_number(x):
	if len(str(x)) >= 4:
		f = []
		count = 0
		for index, item in enumerate(str(x)):
			if index == 0:
				f.append(item)
			else:
				if count % 3 == 0:
					f.append(',')
				f.append(item)
				count += 1
		g = ''.join(f)	
		return g
	else:
		return 'Trenger lengre tall!'
