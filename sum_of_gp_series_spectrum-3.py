firnum = int(input('enter the first number of your g.p series'))
ratio = int(input('enter the ratio difference brtween each term'))
length = int(input('enter the length of the gp series'))
i = 0
j = 0
print('each numbers of thr gp series are: ')
while i < length:
	print(firnum)
	j = j + firnum
	firnum = firnum * ratio
	i = i + 1
print('The sum of the numbers of the gp series is: ', j)
