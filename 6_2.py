# coding=utf-8
#!/usr/bin/python
number = 23
running = True
while running:
	guess = int(raw_input('Enter an integer : '))
	if guess == number:
		print 'Congratulations, you guessed it.'
		running = False # this causes the while loop to stop
	elif guess < number:
		print 'No, it is a little higher than that'
	else:
		print 'No, it is a little lower than that'
else:
	print 'The while loop is over.'

print 'Done'

# 我们把raw_input和if语句移到了while循环内，并且在while循环开始前把running变量设置为
# True。
# 当while循环条件变为False的时候，else块才被执行——这甚至也可能是在条件第一次被检验的
# 时候。
