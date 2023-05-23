# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Staff Directory Project for python
# In this project I constructed a Staff directory that includes employee ID's and other user requirements

employee = {149045687: "Monica Jane",
            189018972: "Steven Young",
            178300183: "Yolonda Adams",
            174628103: "Janet Jackson",
            163628930: "Venus Vroom",
            183627384: "Johnathan Abdul"}

check = {149045687: 3500,
         189018972: 3650,
         178300183: 3520,
         174628103: 3750,
         163628930: 4000,
         183627384: 4850}

department = {149045687: ["Digital", "Marketing", "Advertising"],
              189018972: ["IT", "Data Analyst", "Statistics"],
              178300183: ["Product Management", "Designer", "Package Manager"],
              174628103: ["UX Designer", "UI Designer", "Graphic Designer"],
              163628930: ["Interior Designer", "Art Director", "Photographer"],
              183627384: ["Film Director", "Screen Writer", "Script Manager"]}


def main():
    name = input("What is your name? ")
    while True:
        try:
            id_number = int(input("What is your employee ID number? "))
            if id_number not in employee.keys() or employee[id_number] != name:
                print("Try again.")
                continue
            break
        except ValueError:
            print("Please only enter valid employee ID numbers!")

    while True:
        print("Please select an option:")
        print("1. Check")
        print("2. Address change")
        print("3. Job application")
        print("4. Withdraw")
        print("5. Quit")
        option = input()
        if option == "1":
            billing(id_number, check)
        elif option == "2":
            address_change()
        elif option == "3":
            add_departments(id_number)
        elif option == "4":
            withdraw(id_number)
        elif option == "5":
            break
        else:
            print("Try again.")


def billing(id_number, balance_dict):
    while True:
        print("Would you like to check your current paycheck or cash out your paycheck?")
        print("1. Check paycheck")
        print("2. Cash out paycheck")
        option = input()
        if option == "1":
            try:
                print(f"Current paycheck is: {balance_dict[id_number]}")
            except KeyError:
                print("Employee ID not found!")
        elif option == "2":
            try:
                amount = float(input("How much would you like to cash out? "))
                balance_dict[id_number] -= amount
                if balance_dict[id_number] < 0:
                    print(f"You will get a refund of {abs(balance_dict[id_number])}")
                print(f"You withdrew: {amount}")
            except ValueError:
                print("Please only enter valid amounts!")
        else:
            print("Try again.")


def address_change():
    address = input("Would you like to change your address? ")
    if address.lower() == "yes":
        new_address = input("Enter your new address: ")
        print("Your new address is:", new_address)
    else:
        print("Your address will remain the same.")


def add_departments(id_number):
    departments = input("What department would you like to add? ")
    if id_number in department.keys():
        department[id_number].append(departments)
        print("Welcome")
    else:
        department[id_number] = [departments]
        print("Goodbye")
        print("Current Department for", employee[id_number], ":", department[id_number])
    print(department[id_number])


def withdraw(id_number):
    action = input("Would you like to withdraw from the company or move to another department? ")
    if id_number in department.keys() and action in department[id_number]:
        department[id_number].remove(action)
        print(f"Department for {employee[id_number]}: {department[id_number]}")
    else:
        print(f"{employee[id_number]} is not in this department {action}.")


if __name__ == "__main__":
    main()

