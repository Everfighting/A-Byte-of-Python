# coding=utf-8
#!/usr/bin/python
#ab is short for 'a'ddress'b'ook
ab={'Swaroop':'swaroopch@byteofpython.info',
    'Larry'  :'larry@wall.org',
    'Matsumoto':'matz@ruby-lang.org',
    'Spammer'  :'spammer@hotmail.com'
    }
print "Swaroop's address is %s" %ab['Swaroop']

# adding a key/value pair
ab['Guido']='guido@python.org'

#deleting a key/value pair
del ab['Spammer']

print '\n The number of address in this address book is %s' %len(ab)
for name,address in ab.items():
    print 'Contact %s at %s' %(name,address)

if 'Guido' in ab:
    print "\n Guido's address is %s" %ab['Guido']
