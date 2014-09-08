from sys import argv


script, user_name = argv
# set the prompt here in pass it in rather than typing it anew each time
prompt = '> '

print "Hello %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like the food this evening, %s?" % user_name
likes = raw_input(prompt)

if likes not in ['no', 'false', 'yuck']:
    response = "Oh good, I'm so glad you like it!"
else:
    response = "I'm sorry, can I get you something else?"

print response
