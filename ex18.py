# assigning list items to variables - number of variables must match list length
d, s, n = ['dave', 'scott', 'nick']
print s

# take in an unknown number of arguments and assign them to variables
def print_two(*args):
    print "Number of arguments submitted: ", len(args)
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
    print "arg1: %r" % arg1

def print_none():
    print "I got nothin'."

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
