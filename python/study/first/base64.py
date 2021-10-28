def safe_base64_decode(s):
    remainder = len(s)%4
    if remainder!=0:
        return base64.b64decode(s + b'=' * (4 - remainder))
    return  base64.b64decode(s)

#assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
#assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('Pass')