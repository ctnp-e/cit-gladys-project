import io

import gladysCompute as compute
import gladysSatellite as satellite
import gladysUserLogin as userLogin

"""
	Student: Ngoc Nguyen, Ethan Cao
	Module: gladysUserInterface
	Description: This module does Gladys West Map App
"""


def runTests():
	"""
		tests some module functions
	"""

	print("running a few tests")

	average = compute.gpsAverage(4, 5)
	print("average = ", average)

	# delete the remaining code *in this function* and replace it with
	# your code. add more code to do what the assignment asks you to do.
	# add 3 more tests of different functions in different modules
	print("hello!")


def start():
	"""
		logs the user in, and runs the app
	"""

	userName = userLogin.login()

	runApp(userName)


def runApp(userName):
	"""
		runs the app
	"""

	# loop until user types q
	userQuit = False
	current_x = 1
	current_y = 1
	dest_x = 2
	dest_y = 2
	distance = compute.distance((current_x, current_y), (dest_x, dest_y))
	while (not userQuit):

		# menu
		"""
			here student needs to print their own menu. or, to do better, 
			create a function to print your menu and simply call it here.
		"""
		print("-- Welcome to the Gladys West Map App --")
		print("email = ", userName)
		print(f"Current position    : x = {current_x}, y = {current_y}")
		print(f"Destination position: x = {dest_x}, y = {dest_y}")
		print(f"Distance            : {distance}")
		print()
		print("Type t to run tests or q to quit")
		print(" [c] to set current position")
		print(" [d] to set destination position")
		print(" [m] to map - which tell the distance")
		print(" [t] to run moduel test")
		print(" [q] to quit")
		print()

		# get first character of input
		userInput = input("Enter a command:")
		lowerInput = userInput.lower()
		firstChar = lowerInput[0:1]

		# menu choices, use a switch-like if-elif control structure

		"""
			here students need to change and add to this code to
			handle their menu options
		"""
		# quit
		if firstChar == 'q':
			userQuit = True

		# run some tests (this is part 1 of 2)
		elif firstChar == 't':
			runTests()

		elif firstChar == 'c':
			current_x = int(input("Enter current x: "))
			current_y = int(input("Enter current y: "))

		else:
			print("ERROR: " + firstChar + " is not a valid command")

	print("\n")
	print("Thank you for using the Gladys West Map App!")
	print("\n")
