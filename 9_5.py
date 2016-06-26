# coding=utf-8
shoplist = ['apple', 'mango', 'carrot', 'banana']

#Indexing or 'Subscription' operation
print 'Item[0] is', shoplist[0]
print 'Item[1] is', shoplist[1]
print 'Item[2] is', shoplist[2]
print 'Item[-1] is',shoplist[-1]
print 'Item[-2] is',shoplist[-2]
print 'Items except the last are',shoplist[:-1]

#Slicing operation
print 'Item 0 to 1 are', shoplist[0:2]
print 'All items are', shoplist[:]
print 'Item 1 to -1 are',shoplist[1:-1]
print 'Item -1 to -3 are',shoplist[-3:-1]

#Slicing on a string
name='python'
print 'characters 1 to 3 are',name[0:3]
print 'characters 2 to end are',name[2:]
print 'characters 1 to -1 are',name[0:-1]
print 'characters start to end are',name[:]
