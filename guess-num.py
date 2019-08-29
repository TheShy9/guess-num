import random
r = random.randint(1,100)
while True:
	guess = input('请猜测数字的大小： ')
	guess = int(guess)
	if guess == r:
		print('终于猜对了')
		break
	else:
		x = guess - r
		if x > 0:
			print('比答案大')
		else:
			print('比答案小')
		