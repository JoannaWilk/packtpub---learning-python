# 4 ways to make a string

str1 = 'String built with single quotes.'
str2 = "String built with double quotes."
str3 = '''String built with triple quotes,
so it can span multiple lines.'''
str4 = """String built with triple double-quotes
so it can span multiple lines."""

# without print it's displayed with /n
# str4
print(str4)

# indexing and slicing strings
text = "The trouble is you think you have time."
print("Whole string: ", text)
print("string[0]: ", text[0])
print("string[5]: ", text[5])
print("string[:4]: ", text[:4])
print("string[4:]: ", text[4:])
print("string[2:14]: ", text[2:14])
print("string[2:14:3]: ", text[2:14:3])
print("quick way of making a copy - string[:]: ", text[:])

print("reversed - string[::-1]: ", text[::-1])
