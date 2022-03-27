password = "a123456"
x = 3
while True :
	pdw = input("please input po:")
	if pdw == password :
		print('succed log in')
		break
	else:
		x = x - 1
		print('Wrong password!You have',x,'chance!')
		if x == 0:
			break
