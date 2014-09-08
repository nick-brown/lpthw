# commas prevent print from ending with a \n
print "How old are you?",
# raw_input() appears to take arguments from the command line and allow them
# into the script
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %s old, %s tall and %s heavy." % (age, height, weight)
