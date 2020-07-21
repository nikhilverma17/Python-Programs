import base64
string_b="This is Saif".encode('utf-8')
base64_bytes=base64.b64encode(string_b)
##print(base64_bytes)

##base64_decoded_bytes=base64.decodebytes(base64_bytes)

a=base64_bytes.decode('utf-8')

base64_decoded_bytes=base64.b64decode(a)

print(base64_decoded_bytes.decode())
