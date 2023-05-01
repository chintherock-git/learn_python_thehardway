class Bank():
    def __init__(self,owner,account):
        self.owner=owner
        self.account=account
        
    def deposit(self,amount):
        self.account=self.account+amount
        return f"Successfully Deposited"
    
    def withdraw(self,amount):
        if amount>self.account:
            return "You do not have sufficient balance"
        else:
            self.account=self.account-amount
            return "Withdrawal Accepted!!"
            
    def __str__(self):
        return f"Account Owner :{self.owner} \nAccount Balance : ${self.account}"
    
if __name__=="__main__":
    acct1=Bank('Rita',10000)
    print(acct1)
    print(acct1.deposit(1000))
    print(acct1.withdraw(500))
        