# set up a formatter string that we can re-use to dump a bunch of info into
formatter = "%r %r %r %r"

# formatting ints, strings, and bools with the %r (raw) formatter
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)

# format formatting itself - it works!
print formatter % (formatter, formatter, formatter, formatter)

# multiline format statement
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
