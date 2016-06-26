# coding=utf-8
#!/usr/bin/python
while True:
	s = raw_input('Enter something : ')
	if s == 'quit':
		break
	if len(s) < 3:
		continue
	print 'Input is of sufficient length'
# Do other kinds of processing here...

# 使用continue语句忽略块中的剩余的语句
