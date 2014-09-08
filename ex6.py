# %d appears to format integers into a string
x = "There are %d types of people." % 10

# simple variables
binary = "binary"
do_not = "don't"

# basic string formatting, use parens for multiples
y = "Those who know %s and those who %s." % (binary, do_not) # 2 strings in a string
print x
print y

# printing out information about the string in addition to the string itself
print "I said: %r." % x # string in a string

# regular old string formatting
print "I also said: '%s'." % y # string in a string

# %r and %s perform about the same with booleans, it would seem
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print joke_evaluation % hilarious

# you can concat strings with the + operator
w = "This is the left side of..."
e = "a string with a right side."
print w + e
