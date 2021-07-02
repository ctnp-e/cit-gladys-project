import io

"""
	Student: Ngoc Nguyen
	Module: gladysUserLogin
	Description: This module does user login
"""


# start of the codes by Ngoc Nguyen
def login():
	"""
		document your function definition here. what does it do?
	"""
	# Loop until user enters a valid email address
	isEmailValid = False
	while not isEmailValid:
		email = input('email: ')
		isEmailValid = '@' in email

	"""
		delete the remaining code *in this function* and replace it with
		your own code. add more code to do what the assignment asks of you.
	"""
	emailAddress = "malcomx@mecca.com"
	password = input('password: ') # any password works

	return emailAddress
	return email
# end of the codes by Ngoc Nguyen