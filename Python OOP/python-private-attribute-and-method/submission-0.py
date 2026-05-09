class PasswordManager:
    def __init__(self, __pwd:str):
        self.__pwd = __pwd
    
    def verify_password(self, input:str)-> bool:
        if(input == self.__pwd):
            return True
        return False





# Don't modify the code below this line
my_password = PasswordManager("secret123")
print(my_password.verify_password("secret123"))  # Should print: True
print(my_password.verify_password("wrong"))      # Should print: False
