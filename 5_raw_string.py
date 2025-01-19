# Python Raw Strings Ignore Escape Character Sequences.
# Raw string starts with r and R followed by "" or ''
# The main difference between a raw string and a simple string lies in how backslashes are interpreted.

# in simple string backslashes have special meaning. 
simple_string = "This is a simple string\nWith a new line"
print(simple_string)

# In a raw string, backslashes are treated as literal characters. 
raw_string = r"This is a raw string\nWith a literal backslash"
print(raw_string)