# coding=utf-8
name = 'Swaroop'

if name.startswith('S'):
	print 'name is started with "S"'

if 'oo' in name:
	print 'name contains "oo"'

if name.find('ar') != -1:
	print 'name contains "ar"'

delimiter = '_*_'
shoplist = ['apple', 'pear', 'carrot', 'banana']
print delimiter.join(shoplist)