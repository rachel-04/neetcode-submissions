class BankAccount:
    def __init__(self, __balance: int):
        self.__balance = __balance
    
    def get_balance(self)-> int:
        return self.__balance
    def set_balance(self, __balance: int)-> None:
        if(__balance >= 0):
            self.__balance = __balance
        else:
            print("Cannot set negative balance!")

    # TODO: Add setter method for balance




# Don't modify the code below this line
account = BankAccount(1000)
print(account.get_balance())
account.set_balance(-100)
print(account.get_balance())
account.set_balance(100)
print(account.get_balance())
account.set_balance(0)
print(account.get_balance())
