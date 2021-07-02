import io

"""
	Student: Ngoc Nguyen + a little bit of mary ivanov
	Module: gladysUserLogin
	Description: This module does user login
"""


# start of the codes by Ngoc Nguyen
def login():
	"""
		checks that the email address contains an @ symbol
	"""
	# Loop until user enters a valid email address
	isEmailValid = False
	while not isEmailValid:
		emailAddress = input('email: ')
		isEmailValid = '@' in emailAddress

	password = input('password: ') # any password works

	return emailAddress
# end of the codes by Ngoc Nguyen
#a little bit of combing by Mary Ivanov