import sys


question = "Are you Sure ??"
default = "no"

valid = {"yes": True , "y": True, "ye" : True}
invalid = {"no" :False,"n":False}
prompt = " [y/N] "

while True:
	choice = raw_input(question + prompt )
	if choice in valid:
		break
	elif choice in invalid:
		sys.stdout.write("exiting from program \n")
		exit()
	else:
		sys.stdout.write("Please respond with 'yes' or 'no' " + 
                             "(or 'y' or 'n').\n")					

print "Going Ahead\n"


