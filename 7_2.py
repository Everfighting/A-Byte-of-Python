# coding=utf-8
#!/usr/bin/python
def printMax(a, b):
	if a > b:
		print a, 'is maximum'
	else:
		print b, 'is maximum'

# directly give literal values
printMax(3, 4)

# give variables as arguments
x = 5
y = 7
printMax(x, y)