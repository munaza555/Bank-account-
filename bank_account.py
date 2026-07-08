class BankAccount:
    def __init__(account, account_holder, balance,):
        account.account_holder=account_holder
        account.__balance=balance

    def bala(account):
          return account.__balance
    def deposit(account):
        print('Enter Deposit amount')
        deposit=int(input(''))
        account.__balance+=deposit
        return account.bala()
    def withdraw(account):
        print('enter withdraw amount')
        withdraw=int(input())
        if withdraw<=account.__balance and withdraw>=0:
            account.__balance-=withdraw
            return account.bala()
        else:
            print('insuficient balance')
            return account.bala()

print('First enter name and then initial Amount')
acc1=BankAccount(input(''),int(input()))
print("new balance is",acc1.deposit())
print("remaining balance is",acc1.withdraw())
print('First enter name and then initial Amount')
acc2=BankAccount(input(''),int(input()))
print("new balance is",acc2.deposit())
print("remaining balance is",acc2.withdraw())
