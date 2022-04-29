# File: grace_p2.py
# Author: Isaiah Grace
# Date: 2022/4/19
# Lab Section: Tuesday
# Email: isaiah.grace@maine.edu
# Description: Retail customer database manager
# Collabs: N/a

# --- Project 2 ---

database = {}

def add_usr(dict, name, customer_list=[]):
    if name in dict:
        print("There is already a customer by that name.")
        return
    
    if len(customer_list): #if provided with customer info, fill dict
        dict.update({name: customer_list})
        return

    customer_list[0] = input("What is the customer's phone number: ")
    customer_list[1] = input("What is the customer's current balance: ")
    customer_list[2] = input("What is the customer's number of recent purchases: ")

    dict.update({name: customer_list})

def rem_usr():
    pass

def update_balance():
    pass

def inc_purchases():
    pass

def print_database():
    pass

# The fun parts ---

def populate_dict():
    file = open('customers.txt', 'r')
    
    for line in file:
        line = line.split()
        name = line.pop(0) + ' ' + line.pop(0) #format to push to dict

        add_usr(database, name, line)

def input_loop():
    usr_input = input("Please enter an option (or [q] to quit)): ")

    while usr_input != 'q':
        usr_input = input("Please enter an option (or [q] to quit)): ")

        #TODO: Needs if statements for all options
        if usr_input == 'a':
            add_usr(database, input("Customer name: "))
        if usr_input == 'r':
            pass
        if usr_input == 'x':
            pass
        if usr_input == 'i':
            pass
        if usr_input == 'p':
            pass
        if usr_input == 'help' or usr_input == 'h':
            print("[a] -> Add customer to database.")
            print("[r] -> Remove customer from database.")
            print("[x] -> Alter customer balance.")
            print("[i] -> Increment customer num of purchases.")
            print("[p] -> Print a pretty list of the current database.")

        print('\n')

    print("Goodbye")


# Start script ---
populate_dict()
