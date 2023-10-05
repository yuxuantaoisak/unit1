def registration(uname, upass):

    with open('users.csv', mode='r') as f:
        data = f.readlines()
        unamelist = [line.strip().split(',')[0] for line in data]
        upasslist = [line.strip().split(',')[1] for line in data]

        if uname in unamelist and upass not in upasslist:
            print("Username already exists. Please choose another one.")
        elif uname in unamelist and upass in upasslist:
            print("The account already exists. Please go to login page.")
        else:
            with open('users.csv', mode='a') as f:
                line = f"{uname},{upass}\n"
                f.writelines(line)
            print("Registration successful.")


while True:
    print("Welcome to the program")
    print("1. Register")
    print("2. Already a user? Log in")
    choice = input("Please enter your choice: ")
    if choice == '1':
        username = input("Please create a username: ")
        password = input("Please create a password: ")
        registration(username, password)
        break
    elif choice == '2':
        break
    else:
        print("Invalid choice. Please retry.")
