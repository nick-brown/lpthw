from sys import argv

# script seems to be a protected term
script, first, second, third = argv

print argv

# arguments and raw_input both come into the program as a string and must be 
# converted to other types (such as int) if needed
print "The script is called:", script
print "First variable is:", first
print "Second variable is:", second
print "Third variable is:", third
