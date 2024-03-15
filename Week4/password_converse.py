PASSWORD = '1234567'
password = str(input('Enter your password: '))

if password != PASSWORD:
    print('Access denied')
else:
    print('Access granted')