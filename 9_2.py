# coding=utf-8
zoo=('dog','elephant','penguin')
numbers=len(zoo)
print 'This zoo has',numbers,'animals'

new_zoo=('monkey','dolphin',zoo)
print 'The new zoo has',len(new_zoo),'animals'
print 'All animals in new zoo are',new_zoo
print 'Animals brought from old zoo are',new_zoo[2]

print 'Last animal brought from old zoo is ',new_zoo[2][len(zoo)-1]