from models.account import Account
from models.customer import Customer
from models.customers import Customers
from models.currency import Currency

customers = []

customerA= Customer(1,'John K','123456','35353','1234',Account(1,'23456',Currency(1,'KES','Kenya Shillings','Kshs'),10000))
customers.append(customerA)

customerB = Customer(1,'Brian O','98765','353535','7689',Account(2,'9845673',Currency(1,'KES','Kenya Shillings','Kshs'),5000))
customers.append(customerB)

customerC = Customer(1,'Ann M','353534','532225','4567',Account(3,'98965757',Currency(1,'KES','Kenya Shillings','Kshs'),3000))
customers.append(customerC)

bankCustomers= Customers(customers)


print('\n\n** Welcome to The Codevillage Bank **\n')

print('1 Check Balance \n\n')

print('2 Send Money \n\n')

print('3 Press any key to Exit \n\n')

userOption = int(input(' Select a menu to proceed \n\n'))

if userOption == 1:
    phoneNo = input('Enter phone number \n')
    pin = input('Enter Pin \n')
    matched = False
    for cust in customers:
        print(cust.msisdn,cust.pin)
        if cust.msisdn == phoneNo and cust.pin == pin:
            print('Customer With Pin Found, Print Balance \n')
            print('Dear ',cust.name,'Your account Bal is {}'.format(cust.account.balance))
            matched=True
            break
    if not matched:
        print('Could not Validate the Details provided !')

elif userOption == 2:
    phoneNo = input('Enter phone number \n')
    amount = float(input('Enter amount\n'))
    recipientPhone = input('Enter Recipient phone number \n')
    pin = input('Enter Pin \n')
    senderMatched = False
    for cust in customers:
        if cust.msisdn == phoneNo and cust.pin == pin:
            print('Sender With Pin Found')
            sender = cust
            senderMatched=True
            break
    if not senderMatched:
        print('Could not Validate the Details provided !')
    
    print(sender.name)


    if amount > sender.account.balance:
        print('Dear ',sender.name,'You have insufficient balance to complete transaction. Balance is {}'.format(sender.account.balance))
        exit()

    print('Verify Recipient ...')
    recipientMatched = False
    for recepient in customers:
        if recepient.msisdn == recipientPhone:
            print('Recipient Found')
            receiver = recepient
            recipientMatched=True
            break
    if not recipientMatched:
        print('Could not Validate the Recipient Details provided !')
        exit()

    print(receiver.name)

    sender.account.balance -= amount

    print('Dear {}, {} {} sent to {}, balance {} '.format(sender.name,sender.account.currency.shortName,amount,receiver.name,sender.account.balance))

    receiver.account.balance += amount

    print('Dear {}, You have received {} {} from {}, balance {} '.format(receiver.name,receiver.account.currency.shortName,amount,sender.name,receiver.account.balance))
    for x in bankCustomers.customers:
        print('MSISDN:',x.msisdn,x.name,x.account.accountNumber,x.account.balance)
elif userOption ==3:
    exit()
else:
    userOption = 0
