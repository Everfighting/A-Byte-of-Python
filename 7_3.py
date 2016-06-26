# coding=utf-8
#!/usr/bin/python
def func(x):
	print 'x is', x

x = 2
print 'Changed local x to', x

x = 50
func(x)
print 'x is still', x