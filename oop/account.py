class Account:
    def __init__(self, account_number, pin, initial_balance=0):
        self._account_number = account_number
        self._pin = pin
        self._balance =initial_balance
        self._overdraft_limit = 0
        self._owner_details = {}  

    def deposit(self, amount):
    
        if amount > 0:
            self._balance += amount
            return f"Deposited ${amount}. New balance: ${self._balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        
        if amount > 0 and self._balance >= amount:
            self._balance -= amount
            return f"Withdrew ${amount}. New balance: ${self._balance}"
        else:
            return "Insufficient funds or invalid withdrawal amount."

    def view_account_details(self):
    
        return f"Account Number: {self._account_number}\nBalance: ${self._balance}"

    def change_account_owner(self, owner_name, owner_email):
        
        self._owner_details["name"] = owner_name
        self._owner_details["email"] = owner_email
        return "Owner details updated successfully."

    def set_overdraft_limit(self, limit):

        self._overdraft_limit = limit
        return f"Overdraft limit set to ${limit}"
    
    def freeze_account(self):
        
        self._is_frozen = True
        return "Account frozen."

    def unfreeze_account(self):
    
        self._is_frozen = False
        return "Account unfrozen."


    def close_account(self):
        
        return "Account closed successfully."



my_account = Account(account_number="123456", pin="1234", initial_balance=1000)
print(my_account.view_account_details())
print(my_account.deposit(200))
print(my_account.withdraw(300))
print(my_account.unfreeze_account())
print(my_account.freeze_account())
print(my_account.change_account_owner("Mutesi Aline", "alinemutesiii@gmail.com"))
print(my_account.set_overdraft_limit(500))
print(my_account.close_account())





                
                
                       
                       
                
