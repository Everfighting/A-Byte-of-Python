# coding=utf-8
#!/usr/bin/python
number = 23
guess = int(raw_input('Enter an integer : '))
if guess == number:
	print 'Congratulations, you guessed it.' # New block starts here
	print "(but you do not win any prizes!)" # New block ends here
elif guess < number:
	print 'No, it is a little higher than that' # Another block
	# You can do whatever you want in a block ...
else:
	print 'No, it is a little lower than that'
	# you must have guess > number to reach here
print 'Done'
# This last statement is always executed, after the if statement is executed

#内建的raw_input函数提供一个字符串，这个字符串被打印在屏幕上，然后等待用户的输
#入。
#注意if语句在结尾处包含一个冒号——我们通过它告诉Python下面跟着一个语句块。
#