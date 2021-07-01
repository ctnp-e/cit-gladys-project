"""
	Student: Ngoc Nguyen
	Module: gladysUserLogin
	Description: This module does user login
"""

# start of the codes by Ngoc Nguyen
def login():
	# Loop until user enters a valid email address
	isEmailValid = False
	while not isEmailValid:
		email = input('email: ')
		isEmailValid = '@' in email

	password = input('password: ') # any password works

	return email
# end of the codes by Ngoc Nguyen