class Bank(object):
    def __init__(self,CardNumber,pin):
        self.CardNumber=CardNumber
        self.pin=pin
    def details(self):
        print("Withdraw money")
        print("Check balance")


jane= Bank(int(input("enter your card number")),int(input("enter your pin")))
print(jane.details())