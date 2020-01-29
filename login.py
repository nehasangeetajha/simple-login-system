data = {'shrey': 'shrey1', 'sang': 'sang1'}

def loginpage():
    username_list = list(data.keys())
    password_list = list(data.values())
    
    def createacc():
        def createusername():
            username = input('Username: ')
            if username in username_list:
                print('Username already taken, choose another username')
                return createusername()
            else:
                return username
            
        def createpassword():
            password = input('Password (must be atleast 8 characters) : ')
            #string_utf = string.encode()
            if len(password)<8:
                print('Password too short')
                return createpassword()
            else:
                return password
            
        username = createusername()
        password = createpassword()

        data.update({username:password})
        

        print('Your Account has been created, please login using same username and password')

        return loginpage()

    
    def loginacc():
        def inputusername():
            username = input('Username: ')
            if username in username_list:
                return username
            else:
                print('Username not found')
                return loginpage()
        
        username = inputusername()
        password = input('Password: ')
        if password == password_list[username_list.index(username)]:
            print('Access Granted')
        else:
            print('Wrong password')

        return loginpage()


    def delacc():
        def delusername():
            username = input("Enter the Account's Username that you want to delete: ")
            if username in username_list:
                return username
            else:
                print('Account name not found')
                return loginpage()
            
        username = delusername()
        password = input('Input Password for identity verfication: ')
        if password == password_list[username_list.index(username)]:
            data.pop(username)
            print('Account Deleted')
            
        else:
            print('Password not verified, Password wrong')

        return loginpage()
            
        

    print('Existing Users ' + str(username_list))
    response = input('If you want to\nLogin, press 1\nCreate New Account, press 2\nDelete Existing Account, press 3\n: ')
    if response == 1:
        loginacc()
    elif response ==  2:
        createacc()
    elif response == 3:
        delacc()
    else:
        print('Invalid input, please input valid number')
        loginpage()


loginpage()







    


    