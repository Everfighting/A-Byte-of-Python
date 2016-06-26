# coding=utf-8
print 'Simple Assignment'
shoplist = ['apple','pear','banana','carrot']

#reference
mylist=shoplist
del shoplist[0]
print 'shoplist is',shoplist[:]
print 'mylist is',mylist[:]

mylist=shoplist[:]
del shoplist[0]
print 'shoplist is',shoplist[:]
print 'mylist is',mylist[:]

