
# unicode strings: code points
s = " This is üŋíc0de"
print("an s object: ", s,
      "has type: ", type(s))

# utf-8 encoded s
encoded_s = s.encode('utf-8')
# and the result is bytes object
print("encoded s: ", encoded_s)
print("type of encoded s: ", type(encoded_s))
# it can be reverted:
print("decoded encoded s: ", encoded_s.decode('utf-8'))
# and let'd create a bytes object
bytes_obj = b"A bytes object"
print("created bytes object: ", bytes_obj)
print("type of byte object: ", type(bytes_obj))
