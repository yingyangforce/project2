# File: grace_p2.py
# Author: Isaiah Grace
# Date: 2022/4/19
# Lab Section: Tuesday
# Email: isaiah.grace@maine.edu
# Description: Retail customer database manager
# Collabs: N/a

## --- Project 2 ---

database = {}

def add_usr(dict, name, customer_list=[]):
    if name in dict:
        print("There is already a customer by that name.")
        return
    
    if len(customer_list): ##if provided with customer info, fill dict
        dict.update({name: customer_list})
        return

    customer_list.append(input("What is the customer's phone number: "))
    customer_list.append(input("What is the customer's current balance: "))
    customer_list.append(int(input("What is the customer's number of recent purchases: ")))

    dict.update({name: customer_list})

    print("Customer added.")

def rem_usr(dict, name):
    if name in dict:
        dict.pop(name)

        print("User removed from list.")
        return
    
    print(f"I can't find {name} in my list. Please check formatting.")

def update_balance(dict, name):
    if name in dict:
        dict[name][1] = input("Enter new balance: ")

        print("Balance updated.")
        return
    
    print(f"I can't find {name} in my list. Please check formatting.")

def inc_purchases(dict, name):
    if name in dict:
        dict[name][2] = int(dict[name][2]) + 1

        print("Purchase count increased.")
        return

    print(f"I can't find {name} in my list. Please check formatting.")

def print_database(dict):
    print()

    for name in dict:
        print(f"{name}:")
        print(f" • Phone #:  {database[name][0]}")
        print(f" • Current balance:  {database[name][1]}")
        print(f" • Recent purchases:  {database[name][2]}")
        print()


## The fun parts ---

def populate_dict():
    file = open('customers.txt', 'r')
    
    for line in file:
        line = line.split()
        name = line.pop(0) + ' ' + line.pop(0) ##format to push to dict

        add_usr(database, name, line)

def input_loop():
    print("Welcome to your favorite user database manager. Enter [h] for a list of commands.")

    usr_input = input("Please enter an option (or [q] to quit)): ")

    while usr_input != 'q':
        if usr_input == 'a':
            add_usr(database, input("Customer name to add: "))
        if usr_input == 'r':
            rem_usr(database, input("Customer name to remove: "))
        if usr_input == 'x':
            update_balance(database, input("Customer name to change balance: "))
        if usr_input == 'i':
            inc_purchases(database, input("Customer to inc num. of purchases: "))
        if usr_input == 'p':
            print_database(database)
        if usr_input == 'help' or usr_input == 'h':
            print("Help: ")
            print("[a] -> Add customer to database.")
            print("[r] -> Remove customer from database.")
            print("[x] -> Alter customer balance.")
            print("[i] -> Increment customer num of purchases.")
            print("[p] -> Print a pretty list of the current database.")
        
        print()

        usr_input = input("Please enter an option (or [q] to quit)): ")

    print("Goodbye")


## Start script ---
populate_dict()
input_loop()
