password = "a12346"
i = 3
while True:
	i = i - 1
	pwd = input('Please enter your password:')
	if pwd == "a123456":
		print("Login Successful")
		break
	else:
		print("Wrong password !")
		if i > 0:
			print(i, "more left")
		else:
			print("No more left")

		
		