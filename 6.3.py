# coding=utf-8
#!/usr/bin/python
for i in range(1, 5):
	print i
else:
	print 'The for loop is over'

# range(1,5)给出序列[1, 2, 3, 4]
# 如果我们为range提供第三个数，那么它将成为步长。例如，range(1,5,2)给出[1,3]。
# else在for运行之后再执行的，除非遇到break.