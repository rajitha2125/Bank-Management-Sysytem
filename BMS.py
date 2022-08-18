 # This is Bank Management System Project file.

customer_dict = {}
mobile_acc_link = {}
def createAccount():
    name = input('Enter the name of customer: ')
    user_name = input('Enter the user name : ')
    mobile_no = int(input('Enter the mobile number of customer: '))
    initial_depo = int(input('Enter the initial deposit amount: '))
    if initial_depo <= 0:
        print('Invalid Amount')
        return
    pin = int(input('Create PIN: '))
    customer = CustomerAccount(name=name,user_name=user_name,mobile_no=mobile_no, initial_depo=initial_depo, pin=pin)
    customer_dict[customer.cust_acc_num] = customer
    customer_dict[customer.user_name] = customer
    mobile_acc_link[customer.mobile_no] = customer.cust_acc_num
    print('New User Created!')
    print(f'Welcome {customer.name} to YashIvan Bank. {customer.cust_acc_num} is your account number')

def login():
    user_name = input('Enter your User Name :  ')
    account_pin = int(input('Enter your Account PIN: '))
    if user_name in customer_dict.keys() and account_pin == customer_dict[user_name].pin :
        print(f'\n{customer_dict[user_name].name} Logged in')
        customer_dict[user_name].basic_details()
    else:
        print('Account either not exist or the pin is wrong')
        return
    while True:
        user_input1 = input(''' Press 1 for Deposit:
Press 2 for Withdrawl:
Press 3 for Mini Statment:
Press 4 to log out\n''')
        if user_input1 == '1':
            customer_dict[user_name].deposit()
        elif user_input1 == '2':
            customer_dict[user_name].withdrawyal()
        elif user_input1 == '3':
            mobile = int(input('Enter the mobile number : '))
            if mobile in mobile_acc_link.keys():
                #secondary = mobile_acc_link[mobile]
                customer_dict[user_name].balanceEnquiry()
            else:
                print('The mobile number you have enter does not have an account associated with it')
        elif user_input1 == '4':
            print("Thanks for visiting YashIvan Bank....")
            return
        else:
            print('Invalid input try again')
        print('\n*********************************************\n')
        customer_dict[user_name].basic_details()


class CustomerAccount():
    acc_num = 123000
   
    def __init__(self, name,user_name, mobile_no, initial_depo, pin):

        self.name                 = name
        self.cust_acc_num         = CustomerAccount.acc_num
        self.user_name            = user_name
        self.mobile_no            = mobile_no
        self.acc_balance          = initial_depo
        self.pin                  = pin

        CustomerAccount.acc_num       = CustomerAccount.acc_num + 1
        #BankAccount.no_of_cust    = BankAccount.no_of_cust + 1

    def basic_details(self):
        print(f'User: {self.name}\t Account No: {self.cust_acc_num}\t Balance: ₹{self.acc_balance}')
    
    def deposit(self):
        amount = int(input('Enter the deposit amount: '))
        if amount > 0:
            self.acc_balance      = self.acc_balance + amount
            print(f'Transaction completed. Current Balance: ₹{self.acc_balance}')
        else:
            print('Invalid amount transaction aborted')

    def withdrawyal(self):
        amount = int(input('Enter the withdrawl amount: '))
        if amount <= self.acc_balance and amount > 0:
            self.acc_balance      = self.acc_balance - amount
            print(f'Transaction completed. Current Balance: ₹{self.acc_balance}')
        else:
            print('Invalid amount transaction aborted')
    def balanceEnquiry(self):
        print(f'Customer Name : {self.name}')
        print(f'Account No: {self.cust_acc_num}')
        print(f'Balance: ₹{self.acc_balance}')
          
while True:
    print("**"*20)
    print("-------- Welcome to YashIvan Bank ------")
    print("**"*20)
    print("--> Press 1 for creating a new customer: ")
    print("--> Press 2 for logging in as an existing customer: ")
    print("--> Press 3 for Exit/Quit ")
    
    ch=int(input("Enter your choice of service : "))
    if ch==1:
        print('Creating New User')
        createAccount()
    elif ch==2:
        print('Logging into your account ')
        login()
    elif ch==3:
        print("Thanks for visiting YashIvan Bank....")
        break
    else:
        print(" Invalid option.")
