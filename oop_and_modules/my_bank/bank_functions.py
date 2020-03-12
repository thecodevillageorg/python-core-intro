from models.account import Account
from models.customer import Customer
from models.customers import Customers
from models.currency import Currency

def initCustomerData():
    customers = []
    customerA= Customer(1,'John K','123456','54634636','1234',Account(1,'23456',Currency(1,'KES','Kenya Shillings','Kshs'),10000))
    customers.append(customerA)
    customerB = Customer(1,'Brian O','98765','363463','7689',Account(2,'9845673',Currency(1,'KES','Kenya Shillings','Kshs'),5000))
    customers.append(customerB)
    customerC = Customer(1,'Ann M','353534','3463636','4567',Account(3,'98965757',Currency(1,'KES','Kenya Shillings','Kshs'),3000))
    customers.append(customerC)
    bankCustomers= Customers(customers)
    return bankCustomers


def displayMenu():
    print('\n\n** Welcome to The Codevillage Bank **\n')
    print('1 Check Balance \n\n')
    print('2 Send Money \n\n')
    print('3 Press any key to Exit \n\n')


def verifyPin(phoneNo,pin,customers):
    matched = False
    for cust in customers.customers:
        print(cust.msisdn,cust.pin)
        if cust.msisdn == phoneNo and cust.pin == pin:
            print('Customer With Pin Found \n')
            matched=True
            break
    if not matched:
        print('Could not Validate the Details provided !')
    return matched


def getCustomerDetails(phoneNo,customers):
    for cust in customers.customers:
        if cust.msisdn == phoneNo:
            customer = cust
            break
    return customer


def checkBalance(cust):
    print('Dear ',cust.name,'Your account Bal is {}'.format(cust.account.balance))

def validateBalance(cust,amount):
    if amount > cust.account.balance:
        print('Dear ',cust.name,'You have insufficient balance to complete transaction. Balance is {}'.format(cust.account.balance))
        exit()

def sendMoney(sender,receiver,amount):
    sender.account.balance -= amount
    print('Dear {}, {} {} sent to {}, balance {} '.format(sender.name,sender.account.currency.shortName,amount,receiver.name,sender.account.balance))
    receiver.account.balance += amount

    print('Dear {}, You have received {} {} from {}, balance {} '.format(receiver.name,receiver.account.currency.shortName,amount,sender.name,receiver.account.balance))


def displayCustomerDetails(customers):
    for x in customers.customers:
        print('MSISDN:',x.msisdn,x.name,x.account.accountNumber,x.account.balance)

