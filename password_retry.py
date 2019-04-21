password = 'a123456'
i = 3
while i > 0 :
	pwd = input('請輸入密碼')
	if pwd == password:
		print('密碼正確')
		break
	else :
		i = i-1
		if i > 0:
			print('密碼錯誤 還剩', i ,'次機會')
		else:
			print('沒機會了')
		 
		




	
