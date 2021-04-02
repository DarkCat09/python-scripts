import base64

passwdfile = open('passwords.txt', mode='wt', encoding='utf-8')

for i in range(23):
    login = input("Enter email: ")
    password = input("Enter password: ")
    passwd_base64 = base64.b64encode(password.encode('UTF-8')).decode('UTF-8')
    passwdfile.write(login + ':' + passwd_base64 + '\n')

passwdfile.close()
