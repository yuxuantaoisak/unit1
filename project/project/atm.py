import datetime

from my_lib import banner_maker,print_menu,validate_int_user

import registration

import login


import csv

import pandas as pd


msg = banner_maker(msg="Welcome to ATM", symbol="¥", space=50)
print(msg)

menu=["Deposit", "Withdraw", "Balance", "Graph", "Conversion rates", "Address book", "Learn more"]
print_menu(menu)

option=-1 #any number not in the options

while option not in [1, 2, 3, 4, 5, 6, 7]:
    option = validate_int_user(msg="Enter an option(1-7): ", menu=menu)

if option == 1:#deposit
    msg_deposit = "Enter amount to deposit: "
    amount = validate_int_user(msg=msg_deposit, menu="")
    user = login.current_user
    date = datetime.date.today()
    with open('atm.csv', mode='a') as f:
        line = f"{date},{amount},{user}\n"
        f.writelines(line)
    print("Saved.") #feedback to the user

if option == 2:
    msg_withdraw = "Enter amount to withdraw: "
    amount = validate_int_user(msg=msg_withdraw, menu="")
    user = login.current_user
    date = datetime.date.today()
    with open('atm.csv', mode='a') as f:
        line = f"{date},{-amount},{user}\n"
        f.writelines(line)
    print("Please don't forget the receipt.")#feedback to the user

if option == 3:
    with open('atm.csv', mode='r') as f:
        data = f.readlines()
    user = login.current_user
    balance = 0
    for line in data:
        parts = line.strip().split(',')
        date, amount, user_x = parts[0], int(parts[1]), parts[2]
        if user_x == user:
            balance+=int(amount)
    print(banner_maker(msg=f"Your balance is ¥{balance}", space=50, symbol="¥"))

if option == 4:#graph of deposits and withdraw
    user = login.current_user
    in_money = 0
    out_money = 0
    with open('atm.csv', mode='r') as f:
        data = f.readlines()
        transaction = 0
    for line in data:
        parts = line.strip().split(',')
        date, amount, user_x = parts[0], int(parts[1]), parts[2]
        if user_x == user:
            transaction += 1

            if int(amount)>0:
                in_money+=int(amount)
            else:
                out_money+=-1*int(amount)


    in_money_scaled = (in_money//1000)
    out_money_scaled = (out_money//1000)
    msg_deposit = f"{'Deposits'.ljust(10)} {'▦'*in_money_scaled}{in_money_scaled}"#integer division
    msg_withdraw = f"{'Withdraws'.ljust(10)} {'▦'*out_money_scaled}{out_money_scaled}"


    print(msg_deposit)
    print(msg_withdraw)
    print(f"Total transactions: {transaction}")#need to fix the data part


if option == 5:
    while True:

        currency_type = input("Please choose what currency you want to convert to, USD, EUR or JPY: ").upper()

        if currency_type == 'USD':
            rate = float(input("Please check the conversion rate right now on https://www.google.com/finance/quote/XMR-USD and enter here: "))
            int_amount = int(input("Please enter the amount you want to check: "))
            result = rate*int_amount
            print(f"{int_amount} XMR is {result} USD.")
            break
        if currency_type == 'EUR':
            rate = float(input("Please check the conversion rate right now on https://www.google.com/finance/quote/XMR-EUR and enter here: "))
            int_amount = int(input("Please enter the amount you want to check: "))
            result = rate*int_amount
            print(f"{int_amount} XMR is {result} EUR.")
            break
        elif currency_type == 'JPY':
            rate = float(input("Please check the conversion rate right now on https://www.google.com/finance/quote/XMR-JPY and enter here: "))
            int_amount = int(input("Please enter the amount you want to check: "))
            result = rate*int_amount
            print(f"{int_amount} XMR is {result} JPY.")
            break
        else:
            print("Please enter a valid currency (USD, EUR, or JPY).")

if option == 6:

        second_menu = ["Check addresses","Add address","Delete address"]
        print_menu(second_menu)
        option=-1  # any number not in the options
        while option not in [1, 2, 3]:
            option = validate_int_user(msg="Enter an option(1-3): ", menu=menu)

        if option == 1:
            with open('address_book.csv', mode='r') as file_obj:
                for line in file_obj:
                    print(line, end='')

        if option == 2:
            with open('address_book.csv', mode='a') as f:

                msg_address = input('Please enter the address: ')
                msg_notes = input('Please enter the description: ')
                address=f"{msg_address},{msg_notes}\n"
                f.writelines(address)
            print("Saved.") #feedback




        if option == 3:
            # Read the CSV file
            data=pd.read_csv('address_book.csv')
            print(data)

            # Get the index of the row to delete from user input
            try:
                row_to_delete = int(input("Please enter the number of the line you want to delete: "))
                if 0 <= row_to_delete<len(data):
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


if option == 7:  #learn more about the cryptocurrency
    with open('monero_intro.csv', mode='r') as file_obj:
        for line in file_obj:
            print(line, end='')
