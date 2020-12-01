# importing the module
import json


# reading the data from the file
f = open('file1.txt')
data = f.read()
data = data.replace("\'", "\"")


# reconstructing the data as a dictionary
js = json.loads(data)
f.close()


account = dict()
ask = None
ex = None
check = True
name = None
count = 0
while ask != 'q':
    ask = input("Are u a registered user(y/n)Enter q to quit and d to delete an account: ")
    if ask == 'n':
        username = input("Enter a username: ")
        while check == True:
            for key,value in js.items():
                if username == key:
                    username = input("Choose another username because this one is already taken: ")
                else:
                    check = False

        password = input("Enter password: ")
        password = input("Enter password again: ")
        account = {username: password}
        js.update(account)
        #f.write(str(js))
        print("Account made successfully")
    elif ask == 'y':
        username = input("Enter username: ")
        password = input("Enter password: ")
        for key,value in js.items():
            if username == key and password == value:
                print('Logged in successfully')
                count = count+1

        if count == 0:
            print("Account doesn't exist. Make one")

    elif ask == 'd':
        username = input("Enter username: ")
        password = input("Enter password: ")
        ex = input("You sure you want to delete the account(y/n): ")
        if ex == 'y':
            for key,value in js.items():
                if username == key and password == value:
                    js.pop(username)
                    print("Account successfully deleted")

f = open("file1.txt", "w")

f.write(str(js))