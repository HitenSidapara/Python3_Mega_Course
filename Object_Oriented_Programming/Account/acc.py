class Account:

    def __init__(self, filename):
        self.filename = filename
        with open(filename, 'r+') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filename, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):

    def __init__(self,filepath,fee):
        self.fee = fee
        Account.__init__(self,filepath)


    def transfer(self,amount):
         self.balance = self.balance - amount -self.fee



checking = Checking("balance.txt",2)
print("Balance is :"+str(checking.balance))
checking.withdraw(200)
checking.commit()
print("Balance is :"+str(checking.balance))
checking.transfer(500)
checking.commit()
print("Balance is :"+str(checking.balance))
checking.deposit(700)
checking.commit()
print("Balance is :"+str(checking.balance))
