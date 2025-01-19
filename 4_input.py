# with input() - we can read keyboard input in Python.

#----------------------------
# simple usecase
#----------------------------
input("Enter your age: ") # input processes all inputs as string literals

#----------------------------
# reading multiple entries from user.
#----------------------------

details = input("Enter your First Name, Last Name and your Age spearaterd by comma: ")

user_detail = [each_detial.strip() for each_detial in details.split(",")]
print(user_detail)

#----------------------------
# We can also secure sensitive information, so it won't be visible to screen whatever we type
# for this we will import getpass module
#----------------------------
import getpass
my_mail = getpass.getpass("Enter email addres: ")
print(my_mail)

#----------------------------
# sometimes we need to get the correct inputs, so to validate the input we may apply many if conditions.
# so we can overcome this issue with - PyInputPlus library, in case of wrong input it will prompt us again
# to give the correct input.
# Install it: python -m pip install pyinputplus
#----------------------------
import pyinputplus as pyip

age = pyip.inputInt(prompt="Enter age: ", min=0, max=100)
print(age)