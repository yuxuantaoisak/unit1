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
| 2       | Create a login system     | A flow diagram and the code for login                                                                     | 30min         | Sep 14                 | B,C       |
| 3       | Create success criteria   | To have a list of criteria that can used to evaluate the final product                                    | 20min         | Sep 19                 | A         |
| 5       | Create an ATM machine     | A flow diagram and code for an ATM machine system                                                         | 40min         | Sep 20                 | B,C       |
| 4       | Create system diagram     | To have a clear idea of the hardware and software requirements for the  proposed solution                 | 10min         | Sep 24                 | B         |
| 6       | Create a test plan        | Have the code tested to see if it aligns with the success criteria and  has the described functionalities | 30min         | Sep 29                 | B         |
| 7       | Create citation for codes | A complete citation on sources used throughout the development of the product                             | 20min         | Sep 29                 | C         |                                                                                                

# Criteria C: Development

My client requires a system to protect the private data. I thought about using a login system to accomplish this requirement using a if condition and the open command to work with a csv file. 

A you can see in the flow diagram in **Fig 3**, in th first line I am defining a function called try_login, this function has two inputs of type string, and the output is a boolean representing True if the
user logins correctly or false otherwise. This is saved in the variable success. Then in line two, I used the open function to open the csv file named 'users.csv' and used readlines function to access all the usernames and passwords. After that, I initialized the logged_in function as False and used a for loop to define 'uname' 
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
