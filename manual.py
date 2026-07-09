balance=1000
print('please Select 1.check balance 2.deposit 3.withdraw 4.exit')
user_input=int(input())
def deposit():
    print('enter deposit amount')
    deposit=int(input())
    return balance+deposit
def withdraw():
    print('enter withdraw amount')
    withdraw=int(input())
    if withdraw<=1000 and withdraw>0:
        return balance-withdraw
    else:
        print('insuficient balance')
        return balance
if user_input==1:
    print(balance)
elif user_input==2:
    print('new balance is',deposit())
elif user_input==3:
    print('remaining balance is',withdraw())
elif user_input==4:
    print('exit')
else:
    print('invalid number')
