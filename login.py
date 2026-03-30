login={}

while True:
    print("1/ Register")
    print("2/ Login")
    print("3/Exit")


    user=input("Enter your choice(or press exit to end program)")

   

    if user=="exit" or user== "3":
        print("Program Ended")
        break

    elif user=="1" or user=="Register":
        username=input("Enter username")
        password=input("Enter your password")
        confirm_password=input("Enter same password to confirm")
        if password==confirm_password:
            login[username]=password
            print("Register Successfully")
        else:
            print("Passwords Not Matched")

    
        

    elif user=="2" or user=="Login":
        name=input("Enter your username")
        lpassword=input("Enter your password")

        if name in login:
            if login[name]==lpassword:
                print("Login Succesfully")
            else:
                print("Wrong password")
        else:
            print("Account not found")

    else:
        print("Invalid Choice")


    