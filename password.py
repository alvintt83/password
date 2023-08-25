password = "a12346"
i = 3
while True:
	pwd = input('Please enter your password:')
	if pwd == "a123456":
		print("Login Successful")
		break
	else:
		i = i - 1
		print("Wrong password !", i, "more left")
		if i == 0:
			break

		
		