from models.account import Account
from models.customer import Customer
from models.customers import Customers
from models.currency import Currency
from bank_functions import displayMenu
from bank_functions import initCustomerData
from bank_functions import verifyPin
from bank_functions import checkBalance
from bank_functions import getCustomerDetails
from bank_functions import sendMoney
from bank_functions import validateBalance
from bank_functions import displayCustomerDetails

## returns list of initial customers
bankCustomers = initCustomerData()

displayMenu()

userOption = int(input(' Select a menu to proceed \n\n'))

if userOption == 1:
    phoneNo = input('Enter phone number \n')
    pin = input('Enter Pin \n')
    if verifyPin(phoneNo,pin,bankCustomers):
        checkBalance(getCustomerDetails(phoneNo,bankCustomers))
    else:
        print('Could not Validate the Details provided !')

elif userOption == 2:
    phoneNo = input('Enter phone number \n')
    amount = float(input('Enter amount\n'))
    recipientPhone = input('Enter Recipient phone number \n')
    pin = input('Enter Pin \n')

    if verifyPin(phoneNo,pin,bankCustomers):  
        validateBalance(getCustomerDetails(phoneNo,bankCustomers),amount)
        sendMoney(getCustomerDetails(phoneNo,bankCustomers),getCustomerDetails(recipientPhone,bankCustomers),amount)
    else:
        print('Could not Validate the Details provided !')
        exit()
    displayCustomerDetails(bankCustomers)
elif userOption ==3:
    exit()
else:
    userOption = 0
