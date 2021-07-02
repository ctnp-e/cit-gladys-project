import io

"""
	Student: Gabriel Solomon
	Module: gladysUserLogin
	Description: This module does …
"""


def login():
	"""
		asks user for email and does not accept the email if it does not contain the @ symbol.
	"""

	emailAddress = " "
	while("@" not in emailAddress):
		emailAddress = input("Enter your email address: ")
	
	password = input("Type in your password: ")

	return emailAddress
