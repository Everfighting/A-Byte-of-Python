# coding=utf-8
#!/usr/bin/python
#Run this program in command line like 'C:\Python27>python module.py 123 4 45'
import sys
print 'The command line arguments are:'
for i in sys.argv:
    print i
print '\n\nThe PYTHONPATH is',sys.path