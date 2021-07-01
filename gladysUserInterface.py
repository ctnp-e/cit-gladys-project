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

	print("Need to add 3 tests")


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

	userQuit = False
	current_x = 0
	current_y = 0
	dest_x = 0
	dest_y = 0
	distance = compute.distance((current_x, current_y), (dest_x, dest_y))
	# loop until user types q
	while (not userQuit):

		# menu
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

		# quit
		if firstChar == 'q':
			userQuit = True

		# run some tests (this is part 1 of 2)
		elif firstChar == 't':
			runTests()

		# set current position
		elif firstChar == 'c':
			current_x = int(input("Enter current x: "))
			current_y = int(input("Enter current y: "))

		# set destination postition
		elif firstChar == 'd':
			dest_x = int(input("Enter destination x: "))
			dest_y = int(input("Enter destination y: "))

		# display destination
		elif firstChar == 'm':
			print("---------------")
			print(f" distance = {distance}")
			print("---------------")
			
		else:
			print("ERROR: " + firstChar + " is not a valid command")

	print("\n")
	print("Thank you for using the Gladys West Map App!")
	print("\n")
