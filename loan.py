import json
import os

print("1. Edit Accounts")
print("2. Create Account")
print("3. Delete Account")
print("4. View Account")

#### Function to update the accounts ####
def update_accounts(): # Function to update the accounts
    accjson = open('accounts.json')
    accounts = json.load(accjson)

    for i in list(accounts):
        # convert all values to int
        accounts[i]['totalloaned'] = int(accounts[i]['totalloaned'])
        accounts[i]['totalgivenback'] = int(accounts[i]['totalgivenback'])
        accounts[i]['averagelatetime'] = int(accounts[i]['averagelatetime'])
        accounts[i]['creditscore'] = int(accounts[i]['creditscore'])

        # dont do any actions if updated equals true
        if accounts[i]['updated'] == True:
            continue

        if accounts[i]['activeloan'] == "YES":
            accounts[i]['creditscore'] *= 0.98

        # subtract the amount in totalgivenback from the amount in totalloaned
        totalloanamount = accounts[i]['totalgivenback'] - accounts[i]['totalloaned']
        totalloanamount *= 0.97
        accounts[i]['creditscore'] += totalloanamount

        latetimecalc = accounts[i]['averagelatetime'] * 0.04
        if accounts[i]['averagelatetime'] != 0:
          accounts[i]['creditscore'] -= latetimecalc

        accounts[i]['updated'] = True

        with open('accounts.json', 'w') as outfile:
        # save accounts to json file
            json.dump(accounts, outfile, indent=4) 
update_accounts()


menuinput = input("What are you doing? ")

#### Edit Menu ####
if menuinput == "1":
    update_accounts()

    os.system('clear')

    accjson = open('accounts.json')
    accounts = json.load(accjson)

    # display the accounts in the accounts dictionary
    for i in accounts:
        print(accounts[i]['name'])

    selectmenu = input("Select an Account: ")

    # assign the input of the user to one of the accounts based on the input
    for i in accounts:
        if selectmenu == accounts[i]['name']:
            selection = i
        
    print(selection)

    os.system('clear')

    print("Account Details")
    print("Name: " + accounts[selection]['name'])
    print("Active Loan: " + accounts[selection]['activeloan'])
    print("Total Loaned: " + str(accounts[selection]['totalloaned']))
    print("Total Returned: " + str(accounts[selection]['totalgivenback']))
    print("Average Late Time: " + str(accounts[selection]['averagelatetime']))
    print("Credit Score: " + str(accounts[selection]['creditscore']))

    editmenu = input("Edit Which Detail: ")


    # if the users input is equal to one of the account details then assign the account number to a variable
    for key in accounts[selection]:
        if editmenu == key:
            editselection = key

    finaledit = input("What would you like to set the value to? ")

    accounts[selection][editselection] = finaledit

    accounts[selection]['updated'] = False

    accjson.close()

    with open("accounts.json", "w") as outfile:
        json.dump(accounts, outfile, indent=4)
    
    print("Account Details Updated")

    outfile.close()


#### Creation Menu ####
elif menuinput == "2":
    update_accounts()

    os.system('clear')

    accjson = open('accounts.json')
    accounts = json.load(accjson)

    addmenuone = input("What is the name of the account? ")
    addmenutwo = input("Do they have an active loan? ")

    # loop until you get through all the keys in accounts
    for i in accounts:
        if accounts[i] != None:
            onei = int(i) + 1
            addmenuthree = onei

    accounts[onei] = {'name': addmenuone, 'activeloan': addmenutwo, 'totalloaned': 0, 'totalgivenback': 0, 'averagelatetime': 0, 'creditscore': 100, 'updated': True}

    accjson.close()

    with open("accounts.json", "w") as outfile:
        json.dump(accounts, outfile, indent=4)

#### Deletion Menu ####
elif menuinput == "3":
    update_accounts()
  

    os.system('clear')

    accjson = open('accounts.json')
    accounts = json.load(accjson)

    for i in accounts:
        print(accounts[i]['name'])
    
    deletemenu = input('Which account do you want to delete? ')

    for i in list(accounts):
        if deletemenu == accounts[i]['name']:
            del accounts[i]
    
    accjson.close()

    with open("accounts.json", "w") as outfile:
        json.dump(accounts, outfile, indent=4)

#### View Menu ####
elif menuinput == "4":
    update_accounts()

    os.system('clear')

    accjson = open('accounts.json')
    accounts = json.load(accjson)

    for i in accounts:
        print(accounts[i]['name'])

    viewmenu = input('Which account do you want to view? ')

    for i in accounts:
        if viewmenu == accounts[i]['name']:
            viewselection = i

    print("Name: " + accounts[viewselection]['name'])
    print("Active Loan: " + accounts[viewselection]['activeloan'])
    print("Total Loan: " + str(accounts[viewselection]['totalloaned']))
    print("Total Returned: " + str(accounts[viewselection]['totalgivenback']))
    print("Average Loan Time: " + str(accounts[viewselection]['averagelatetime']))
    print("Credit Score: " + str(accounts[viewselection]['creditscore']))
    