def changer(list):
	a=[x for x in list if x % 2 == 0]
	return a
print changer([1, 4, 9, 16, 25, 36, 49, 64, 81, 100])