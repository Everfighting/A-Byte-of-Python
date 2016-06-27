# coding=utf-8
#!/usr/bin/python
class Person:
	def __init__(self, name):
		self.name = name
	def sayHi(self):
		print 'Hello, my name is', self.name

p = Person('Swaroop')
p.sayHi()
# This short example can also be written as Person('Swaroop').sayHi()