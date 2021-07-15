"""
	Student: Ngoc Nguyen 
	Module: gladysUserLogin
	Description: This module does user login
"""

# start of the codes by Ngoc Nguyen
def login():
	"""
		Logs user in
	"""
	# Loop until user enters a valid email address
	isEmailValid = False
	while not isEmailValid:
		emailAddress = input('email: ')
		isEmailValid = '@' in emailAddress
		if not isEmailValid:
			print("ERROR: Email is not valid:", emailAddress)

	password = input('password: ') # any password works

	return emailAddress
# end of the codes by Ngoc Nguyen
