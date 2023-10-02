# Crypto Wallet

# Criteria A: Planning

## Problem definition

Tseten Lama, the client, is a local trader who is interested in the emerging market of cryptocurrencies. He has started to buy and sell electronic currencies, however at the moment he is tracking all his transactions using a ledger in a spreadsheet which is starting to become burdensome and too disorganized. It is also difficult for Tseten Lama to find past transactions or important statistics about the currency. Tseten Lama is in need of a digital ledger that helps him track the amount of the cryptocurrency, the transactions, along with useful statistics.

There is no existing product that meets the needs of Tseten, so he needs someone to develop a product that is specifically made for the purposes listed above for him to make his life easier. 

The developer, Yuxuan Tao, agrees to develop a product that satisfies these needs and fulfills the requirements, allowing the client to organize and keep track of his spendings and the statistics about the currency of his choice. 

Apart from these requirements, Tseten Lama is open to explore a cryptocurrency selected by the developer.

## Proposed solution

Design statement: I will design and make an **electronic ledger** for a client who is **Tseten Lama**. The **electronic ledger** will be **a software that helps the client to withdraw and transfer money and track spendings** and is constructed using the software **PyCharm**. It will take **four weeks** to make and will be evaluated according to the criteria **A, B, and C**.

Introduction to the cryptocurrency:
Monero (XMR) is a privacy-focused cryptocurrency that was created in 2014. It is designed to provide enhanced privacy and anonymity for its users compared to other cryptocurrencies like Bitcoin. Monero achieves this privacy through various cryptographic techniques, including Stealth Addresses, Ring Signature, and Ring CT. This ensures that the sender, the receiver and the amount of transaction are all hidden by default. 


“What Is Monero (XMR)?” Getmonero.Org, The Monero Project, www.getmonero.org/get-started/what-is-monero/. Accessed 1 Oct. 2023. 


### Design Statement(rationale):

The product will be developed on the software PyCharm, which is a Python IDE with a range of essential tools that allow developers to customize and add the desired functions. It has numerous plug-ins and shortcuts that help with the developer’s productivity. This chosen software will effectively help the developer to achieve the goals that the client set and shorten the time needed compare to other tools. 
Some main features of the product include: deposit and withdrawal, balance checking, currency conversion, and address book. With these functions, the product allows the client to transfer and withdraw his currencies online, and the record is automatically saved. The client can also check the transaction history at ease, without the need to manually record transactions. Additionally, the built-in currency converter allows the client to convert the cryptocurrency to major currencies, making it easy when trading. The address book makes it impossible to make mistakes when transferring money to certain addresses. These functions in the product solve the client’s problem perfectly, as it manages all the records and has all the necessary functionalities that the client needs. 


## Success criteria

1.The electronic ledger is a text-based software (Runs in the Terminal).

2.The electronic ledger display the basic description of the cyrptocurrency selected.

3.The electronic ledger allows to enter, withdraw and record transactions.

4.The electronic ledger shows the past transaction records (deposit, withdrawal, etc) in tables or graphs. 

5.The electronic ledger shows the real time conversion rates from the cryptocurrency to other major currencies in the world (yen, usd, eur). 

6.The electronic ledger has an address book to make it more convenient  send money and reduce errors when typing in address manually (edit and delete).


# Criteria B: Design

## System diagram

![Screenshot 2023-09-14 at 0 19 00](https://github.com/yuxuantaoisak/unit1/assets/144768397/745f50a4-b2d7-4703-aa6d-165cba6dd46c)

**Fig. 1** This is the system diagram. 



## Flow diagrams

<img width="1034" alt="Screenshot 2023-10-02 at 8 36 54" src="https://github.com/yuxuantaoisak/unit1/assets/144768397/6f3285e8-3c25-4a1f-b8f2-8bf78c6ecc20">
**Fig. 2** This is the basic procedure for login. 



<img width="1117" alt="Screenshot 2023-10-02 at 8 47 42" src="https://github.com/yuxuantaoisak/unit1/assets/144768397/b5a58e5d-23dd-48fc-b7d4-4ab0ed16fe58">
**Fig. 3** This is the flow diagram for my login system. 


## Record of tasks

| Task No | Planned Action            | Planned Outcome                                                                                           | Time estimate | Target completion date | Criterion |
|---------|---------------------------|-----------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Finish proposed solution  | An explanation of why the product is being developed                                                      | 10min         | Sep 14                 | A         |
| 2       | Create a login system     | A flow diagram and the code for login                                                                     | 30min         | Sep 14                 | B, C      |
| 3       | Create success criteria   | To have a list of criteria that can used to evaluate the final product                                    | 20min         | Sep 19                 | A         |
| 5       | Create an ATM machine     | A flow diagram and code for an ATM machine system                                                         | 40min         | Sep 20                 | B, C      |
| 4       | Create system diagram     | To have a clear idea of the hardware and software requirements for the  proposed solution                 | 10min         | Sep 24                 | B         |
| 6       | Create a test plan        | Have the code tested to see if it aligns with the success criteria and  has the described functionalities | 30min         | Sep 29                 | B         |
| 7       | Create citation for codes | A complete citation on sources used throughout the development of the product                             | 20min         | Sep 29                 | C         |                                                                                                

## Test Plan

The test plan gives an idea of how the program will be tested as well as an overview of the program. It includes the test type, user input and the expected output, which are all important in testing. This table will also indicate if a specific part of the code has passed the test or no.  

| Test No | Test Type                                                                | User input               | Expected output                                                                                                           | Passed the test (Y/N) | Related success criteria                                                                                                                                    |
|---------|--------------------------------------------------------------------------|--------------------------|---------------------------------------------------------------------------------------------------------------------------|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1       | Upon starting the program,  the menu should pop up.                      | -                        | 1. Deposit 2. Withdraw 3. Balance 4. Graph 5. Conversion rates 6. Address book 7. Learn more Enter an option(1-7):        | Y                     | -                                                                                                                                                           |
| 2       | Check if the system gives feedback if the user enters incorrect value    | Anything  else than  1-7 | Enter an option(1-7):                                                                                                     | Y                     | -                                                                                                                                                           |
| 3       | Check if the deposit function is working.                                | '1'                      | Enter amount to deposit:                                                                                                  | Y                     | 3.The electronic ledger allows to  enter, withdraw and record transactions.                                                                                 |
| 4       | Check if user can deposit  money successfully                            | the amount to deposit    | Saved                                                                                                                     | Y                     | 3.The electronic ledger allows to  enter, withdraw and record transactions.                                                                                 |
| 5       | Check if the withdraw  function is working.                              | '2'                      | Enter amount to withdraw:                                                                                                 | Y                     | 3.The electronic ledger allows to  enter, withdraw and record transactions.                                                                                 |
| 6       | Check if user can withdraw  money successfully                           | the amount to withdraw   | Please don't forget the receipt.                                                                                          | Y                     | 3.The electronic ledger allows to  enter, withdraw and record transactions.                                                                                 |
| 7       | Ckeck if the balance function is working                                 | '3'                      | Your balance is ¥(balance)                                                                                                | Y                     | 3.The electronic ledger allows to  enter, withdraw and record transactions.                                                                                 |
| 8       | Check if the graph function is working                                   | '4'                      | Deposits   ▦*deposits(deposits) Withdraws  ▦*withdraws(withdraws) Total transactions: (len(data))                         | Y                     | 4.The electronic ledger shows the past transaction records (deposition, withdrawal, etc)  in tables or graphs.                                              |
| 9       | Check if the conversion rates function is working                        | '5'                      | Please choose what currency you want to convert to:  USD, EUR or JPY:                                                     | Y                     | 5.The electronic ledger shows the real time  conversion rates from the cryptocurrency to other  major currencies in the world (yen, usd, eur).              |
| 10      | Check if the output for each currency is correct                         | currency type            | Please check the conversion rate  right now on  https://www.google.com/finance/quote/XMR-(currency type)  and enter here: | Y                     | 5.The electronic ledger shows the real time  conversion rates from the cryptocurrency to other  major currencies in the world (yen, usd, eur).              |
| 11      | Check if the calculation is correct                                      | the amount of currency   | (amount) XMR is (amount_2) (Currency_type)                                                                                | Y                     | 5.The electronic ledger shows the real time  conversion rates from the cryptocurrency to other  major currencies in the world (yen, usd, eur).              |
| 12      | Check if the address book submenu pops up correctly                      | '6'                      | 1. Check addresses 2. Add address 3. Delete address Enter an option(1-3):                                                 | Y                     | 6.The electronic ledger has an address book to  make it more convenient to send money and reduce  errors when typing in address manually (edit and delete). |
| 13      | Check if the addresses  can bedisplayed correctly                        | '1'                      | all the addresses in address_book.csv                                                                                     | Y                     | 6.The electronic ledger has an address book to  make it more convenient to send money and reduce  errors when typing in address manually (edit and delete). |
| 14      | Check if address can  be added                                           | '2'                      | Please enter the address: Please enter the description:                                                                   | Y                     | 6.The electronic ledger has an address book to  make it more convenient to send money and reduce  errors when typing in address manually (edit and delete). |
| 15      | Check if address can  be deleted                                         | '3'                      | Please enter the number of the line you want to delete:                                                                   | Y                     | 6.The electronic ledger has an address book to  make it more convenient to send money and reduce  errors when typing in address manually (edit and delete). |
| 16      | Check if the system gives  feedback if the user enters incorrect values  | >row                     | Invalid input. Please enter a valid number.                                                                               | Y                     | 6.The electronic ledger has an address book to  make it more convenient to send money and reduce  errors when typing in address manually (edit and delete). |
| 17      | Check if the system  prints the introduction  to the currency  correctly | '7'                      | monero_intro.csv                                                                                                          | Y                     | 2.The electronic ledger display the basic description  of the cyrptocurrency selected.                                                                      |


# Criteria C: Development

## Login system

My client requires a system to protect the private data. I thought about using a login system to accomplish this requirement using a if condition and the open command to work with a csv file. 

A you can see in the flow diagram in **Fig 3**, in th first line I am defining a function called try_login, this function has two inputs of type string, and the output is a boolean representing True if the
user logins correctly or false otherwise. This is saved in the variable logged_in. Then in line two, I used the open function to open the csv file named 'users.csv' and used readlines function to access all the usernames and passwords. After that, I initialized the logged_in function as False and used a for loop to define 'uname' 
and 'upass' in the file. If username and password are identical as in the users.csv file, the logged_in function becomes True, and it's the end of the program. 

I defined a variable called 'attempts' with the initial value of 3, meaning that there are 3 chances for the user to enter password. When username or password are incorrect, the user will be given the chance, and the 'attempt' variable will be reduced. 

If the password is still incorrect after 3 trials, the user will not be authorized into the program. Otherwise, they can enter the program.



```.py
def try_login(name:str,password:str):
    with open("project/users.csv", mode='r') as f:
        data=f.readlines()
    logged_in=False
    for line in data:
        uname=line.split(",")[0]
        upass=line.split(",")[1].strip()

        if uname==name and upass==password:
            logged_in=True
            break
    return logged_in

attempts=3
name=input("Please enter your username: ")
password=input("Please enter your password: ")
result=try_login(name=name,password=password)

while result==False and attempts>0:
    name=input("[Error] Please enter your username: ")
    password=input("Please enter your password: ")
    result=try_login(name=name,password=password)
    attempts-=1

if result==False:
    print("You are not authorized. Exiting")
    exit(1)  #finish the program

else:
    print("Welcome")


```

## My lib

In this library, I defined three functions which are banner maker, print menu, and validate_int_user. The banner maker was made for the welcome page of the ATM machine, and the same goes with menu function. 
The validate_int_user function validates the user input to menu, making sure that the user enters a digit as an option in the menu by using the isdigit() function. Otherwise, the user will receive feedback and be asked to reenter an option.

```.py
def banner_maker(msg: str, space: int, symbol: str) -> str:
    # predefine variables we will need
    width = len(msg) + 2 * space + 2
    height = 5
    banner = ""
    end_code = "\033[00m"
    green = "\33[0;92m"
    # border-line
    border_line = f"{symbol}" * width
    # middle-line
    middle_line = f"{symbol}" + " " * (width - 2) + f"{symbol}"
    # msg_line
    spaces = " " * space
    msg_line = f"{symbol}{spaces}{green}{msg}{end_code}{spaces}{symbol}"
    banner = f"{border_line}\n{middle_line}\n{msg_line}\n{middle_line}\n{border_line}"

    return banner


def print_menu(menu):
    for i in range(len(menu)):
        print(f"{i + 1}. {menu[i]}")


def validate_int_user(msg,menu):
    option=input(msg)
    while not option.isdigit():
        print("Error")
        print_menu(menu)
        option=input(msg)
    return int(option)

```


## ATM machine

My client needs a software that allows him to deposit, withdraw, check balance, and keep track of records of transaction. I thought that a program that imitates an ATM machine in real life would achieve all of these functions. The main functions of the ATM machine include: deposit, withdraw, balance checking, graph, conversion rates, address book, and learn more about the cryptocurrency (XMR). These main functions
were designed in order to fulfil the success criteria listed above. 

I first imported some python packages and functions defined in a document named my_lib to help with ceratin graphings, menu, and user validation process. After that, I designed the banner and menu using the functions imported. 

First, I input the value of the menu as a list, displaying all the features that the user may need, including deposit, withdrawal, balance checking, graph, conversion rates, address book, and learn more about the cryptocurrency. 

I set the initial value of the variable option as -1, which represents all the values that are not in the options so that it satisfies the conditions of the while loop next line. The number of option that the user inputs will be verified by the function validate_int_user. 

When the value of the variable option is 1, the user will be asked to enter the amount to deposit in which the value will be saved in the variable msg_deposit, while the validate_int_user function will verify the amount. Using the imported datetime package, the date will be recorded in the date variable. Finally, using the writelines() function, the data and amount of deposit will be written in the atm csv file in a new line. The message "Saved." will be returned to the user as feedback.

When the value of the variable option is 2, similarly, the user will be asked to enter the amount to withdraw in which the value will be saved in the variable msg_withdraw, while the validate_int_user function will verify the amount. Using the imported datetime package, the date will be recorded in the date variable. Finally, using the writelines() function, the data and amount of withdrawal will be written in the atm csv file in a new line. The message "Please don't forget your receipt." will be returned to the user as feedback.

When the value of the variable option is 3, the open function will open the atm csv file, and the readlines() function will read all lines. The for loop in the following line adds up all the amount stored in the file, including positive ones(deposit) and negative ones(withdrawal), which is the balance that will be printed using the banner function.

When the value of the variable option is 4, I initialized two functions, in_money and out_money with the initial value of 0. I used open function to open the atm csv file and readlines() function to read all lines. The int function will first make sure that the amount is an integer, then I used a for loop to identify the amount in the file. An if function was then used to identify whether the amount is positive or negative. If the amount is positive, the amount will be added to the in_money variable; if it's negative, the amount will be multiplied by -1 to make it positive and added to the out_money variable. After these operations were done, the two variables will be floor divided and squares were used to represent the variables. A squre represents roughly 1000 units. Finally, the graph will be printed. 

When the value of the variable option is 5, I used a while true loop. I defined the currency_type function as the user input, as they can be either Yen, US Dollar or Euro, and I used the upper() funciton to make sure that the input will be translated into upper case. If the input is USD, the website that contains real time conversion rates(stored in the variable rate) will be printed since it's always fluctuating, and the user will be asked to input the amount of cryptocurrency they want to check which will be stored in the variable int_amount. The two variables will be multiplied and the result will be printed, as the while loop is stopped by break function. The same procedure applies to two other currencies. When the user inputs none of these currency, they will be asked to reenter, which is the feedback.

When the value of the variable option is 6, a sub-menu will be printed which includes the basic features of the address book: check, add and delete address. I set the initial value of the variable option as -1, which represents all the values that are not in the options so that it satisfies the conditions of the while loop next line. The number of option that the user inputs will be verified by the function validate_int_user. If the option is 1, the open function will open the address book csv file and the for function was used to print all the lines. If the option is 2, the open function will open the address book csv file and the user will be asked to input the address and the description of it, which are stored respectively in the variable msg_address and msg_notes. Two variables will be integrated into one variable called address, and stored into the address book csv file using the writelines() function. If the option is 3, the address book csv file will be read using the padas plugin which is a file reader. The address book will be first printed with index in front of each line. Then, the try block was used as a test for the following lines. Then, the user will be asked to enter the line they want to delete, which will be stored into the variable row_to_delete. If the input is valid, the drop function from the pandas package will be used to delete the chosen line. The edited variable data will be printed again to show the user the edited version after which it will be stored into the csv file. If the value the user entered as they option is invalid(less than 0 or bigger than the number of lines of the file), the system will display "Invalid input. Please enter a valid number." as the feedback to the user. 

When the value of the variable option is 7, the open function was used to open the monero introduction csv file. After opening the file, the for loop was used to print every line in the file, while the end operator was used to indicate the end of a string output, which, in this case, is to put the content in the file in lines. 

```.py

import datetime

from my_lib import banner_maker,print_menu,validate_int_user


import csv

import pandas as pd


msg=banner_maker(msg="Welcome to ATM",symbol="¥",space=50)
print(msg)

menu=["Deposit","Withdraw","Balance","Graph","Conversion rates","Address book","Learn more"]
print_menu(menu)

option=-1 #any number not in the options

while option not in [1,2,3,4,5,6,7]:
    option=validate_int_user(msg="Enter an option(1-7): ",menu=menu)

if option==1:#deposit
    msg_deposit="Enter amount to deposit: "
    amount=validate_int_user(msg=msg_deposit,menu="")

    date=datetime.date.today()
    with open('atm.csv', mode='a') as f:
        line=f"{date},{amount}\n"
        f.writelines(line)
    print("Saved.")#feedback to the user

if option==2:
    msg_withdraw="Enter amount to withdraw: "
    amount=validate_int_user(msg=msg_withdraw,menu="")

    date=datetime.date.today()
    with open('atm.csv', mode='a') as f:
        line=f"{date},{-amount}\n"
        f.writelines(line)
    print("Please don't forget the receipt.")#feedback to the user

if option==3:
    with open('atm.csv', mode='r') as f:
        data=f.readlines()

    balance=0
    for line in data:
        date,amount=line.strip().split(',')
        balance+=int(amount)
    print(banner_maker(msg=f"Your balance is ¥{balance}",space=50,symbol="¥"))

if option==4:#graph of deposits and withdraw
    in_money=0
    out_money=0
    with open('atm.csv', mode='r') as f:
        data=f.readlines()
    for line in data:
        date,amount=line.strip().split(',')
        if int(amount)>0:
            in_money+=int(amount)
        else:
            out_money+=-1*int(amount)


    in_money_scaled=(in_money//1000)
    out_money_scaled=(out_money//1000)
    msg_deposit=f"{'Deposits'.ljust(10)} {'▦'*in_money_scaled}{in_money_scaled}"#integer division
    msg_withdraw=f"{'Withdraws'.ljust(10)} {'▦'*out_money_scaled}{out_money_scaled}"


    print(msg_deposit)
    print(msg_withdraw)
    print(f"Total transactions: {len(data)}")


if option==5:

    while True:

        currency_type=input("Please choose what currency you want to convert to, USD, EUR or JPY: ").upper()

        if currency_type=='USD':
            rate=float(input("Please check the conversion rate right now on https://www.google.com/finance/quote/XMR-USD and enter here: "))
            int_amount=int(input("Please enter the amount you want to check: "))
            result=rate*int_amount
            print(f"{int_amount} XMR is {result} USD.")
            break
        if currency_type=='EUR':
            rate=float(input("Please check the conversion rate right now on https://www.google.com/finance/quote/XMR-EUR and enter here: "))
            int_amount=int(input("Please enter the amount you want to check: "))
            result=rate*int_amount
            print(f"{int_amount} XMR is {result} EUR.")
            break
        elif currency_type=='JPY':
            rate=float(input("Please check the conversion rate right now on https://www.google.com/finance/quote/XMR-JPY and enter here: "))
            int_amount=int(input("Please enter the amount you want to check: "))
            result=rate*int_amount
            print(f"{int_amount} XMR is {result} JPY.")
            break
        else:
            print("Please enter a valid currency (USD, EUR, or JPY).")

if option==6:

        second_menu=["Check addresses","Add address","Delete address"]
        print_menu(second_menu)
        option=-1  
        while option not in [1,2,3]:
            option=validate_int_user(msg="Enter an option(1-3): ", menu=menu)

        if option==1:
            with open('address_book.csv', mode='r') as file_obj:
                for line in file_obj:
                    print(line,end='')

        if option==2:
            with open('address_book.csv', mode='a') as f:

                msg_address=input('Please enter the address: ')
                msg_notes=input('Please enter the description: ')
                address=f"{msg_address},{msg_notes}\n"
                f.writelines(address)
            print("Saved.") #feedback




        if option==3:
            # Read the CSV file
            data=pd.read_csv('address_book.csv')
            print(data)

            # Get the index of the row to delete from user input
            try:
                row_to_delete = int(input("Please enter the number of the line you want to delete: "))
                if 0<=row_to_delete<len(data):
                    data=data.drop(index=row_to_delete)
                    print(""
                          "")
                    print(data)

                    # Save the updated data back to the CSV file
                    data.to_csv('address_book.csv',index=False)
                else:
                    print("Invalid input. Please enter a valid row number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")



if option==7:  #learn more about the cryptocurrency
    with open('monero_intro.csv', mode='r') as file_obj:
        for line in file_obj:
            print(line,end='')

```

