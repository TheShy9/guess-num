import random
r = random.randint(1,100)
count = 0
while True:
	count += 1 #count = count + 1 的简写
	guess = input('请猜测数字的大小： ')
	guess = int(guess)
	if guess == r:
		print('终于猜对了')
		print('这是你猜的第', count, '次')
		break
	else:
		x = guess - r
		if x > 0:
			print('比答案大')
		else:
			print('比答案小')
	print('这是你猜的第', count, '次')
		