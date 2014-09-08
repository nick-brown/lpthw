from sys import argv

script, filename = argv

# load the file contents into a variable
txt = open(filename)

print "Here's your file %r:" % filename
# print the info out with the read method
print txt.read()

# we can do the same thing using a prompt rather than a command line argument
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
