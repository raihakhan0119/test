from hashlib import *

user_input = ()

loginDict = {}

def makeHash(password):
	password = input("What would you like to use as your password? Please use only letters and numbers. ")
	hash = (sha256(password.encode('utf-8')).hexdigest())
	loginDict[password] = hash
	print
def login(loginDict):
	loginDict = input("What would you like to use as your username? You cannot use ANY spaces. ")
	
passwordGuess = password

def prompt():
	print("Do you already have an account with us? Answer yes or no ")
	if user_input == yes:
		def 