import io

import gladysCompute as compute
import gladysSatellite as satellite
import gladysUserLogin as userLogin

"""
	Student: Ngoc Nguyen
	Module: gladysUserInterface
	Description: This module does Gladys West Map App
"""

#start of the code by Ngoc Nguyen
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


def get_number(prompt):
	is_in_range = False # num is from 0 to 99 inclusive
	while not is_in_range:
		try:
			number = int(input(prompt))
		except:
			continue
		is_in_range = number >= 0 and number <= 99
	return number

def runApp(userName):
	"""
		runs the app
	"""

	userQuit = False
	current_x = -1
	current_y = -1
	dest_x = -1
	dest_y = -1
	distance = compute.distance((current_x, current_y), (dest_x, dest_y))
	# loop until user types q
	while (not userQuit):
		distance = compute.distance((current_x, current_y), (dest_x, dest_y))
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
			current_x = get_number("Enter current x: ")
			current_y = get_number("Enter current y: ")

		# set destination postition
		elif firstChar == 'd':
			dest_x = get_number("Enter destination x: ")
			dest_y = get_number("Enter destination y: ")

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
# end of the code by Ngoc Nguyen