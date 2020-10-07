def add(x, y):
	return x + y

lists = [[1, 2, 3], [4, 5], [6, 7, 8]]
combinedlist=reduce(add,lists)

print(combinedlist)  
