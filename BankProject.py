#Arisdelsy Bruno


class BankAccount:

    "Mimics a bank interaction"
    bank_name = ''
    num_accounts = 0

    def __init__(self, ID, f_name, l_name, balance, actual_password):
        self.ID = ID
        self.f_name = f_name
        self.l_name = l_name
        self.balance = balance
        self.actual_password = actual_password
        self.logged_in = False
        BankAccount.num_accounts = BankAccount.num_accounts + 1

    def logInUser(self, password): 
        password = input("Enter Password Please:")
        if password == self.actual_password:
            self.logged_in = True
            print("Logged in")
            return True
        else:
            self.logged_in = False
            print("Not logged in")
            return False

    def getAccountInfo(self):
        if self.logged_in == True:
            print("User: "+ self.f_name +" "+ self.l_name)
            print("ID: "+str(self.ID))
        else:
            print("Not Logged In")
        
    def depositMoney(self, amount):
        if self.logged_in == True:
            self.balance = self.balance+amount
            print("\n New Balance:", self.balance)
        else:
            print("Not Logged In")      

    def withdrawMoney(self, amount):
        if self.logged_in == True:
            if self.balance >= amount:
                self.balance -= amount
                print("\n You Successfully Withdrew: ", amount)
            else:
                print("No money")
        else:
            print("Not Logged In")
    def getBalance(self):
        if self.logged_in == True:
            print(self.balance)
        else:
            print("Not Logged In")

    def changePassword(self, new_password):
        if self.logged_in == True:
            if len(new_password) >= 8:
                if any(char.isdigit() for char in new_password):
                    if any(char.isupper() for char in new_password):
                        self.actual_password = new_password
                        print("Password successfully changed!")
        else:
            print("Not Logged In")                        
                
   
my_acc1 = BankAccount(12500, "Nicholas", "Font", 1000, "MyPassword34")
if my_acc1.logInUser("MyPassword34") == True:
    my_acc1.getAccountInfo()
    my_acc1.withdrawMoney(500)
    my_acc1.getBalance()
    my_acc1.changePassword("MyNewPassword35")
my_acc2 = BankAccount(14000, "Samantha", "Echavarria", 1000, "AnotherPW0000")
if my_acc2.logInUser("AnotherPW0000") == True:
    my_acc2.getBalance()
    my_acc2.depositMoney(1000)
print("Number of accounts is: ", BankAccount.num_accounts)
