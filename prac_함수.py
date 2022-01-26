def open_account():
    print('새로운 계좌가 개설되었습니다.')
open_account()

#입금
def deposit(balance, money):
    print('{}원이 입금되었습니다. 잔액은 {}원 입니다.'.format(money, balance + money))
    return balance + money


#출금
def withdraw(balance, money):
    if balance >= money:
        print('{}원이 출금되었습니다. 잔액은 {}원 입니다.'.format(money, balance-money))
        return balance - money
    else:
        print('잔액이 부족합니다. 현재 잔액은 {}원입니다.'.format(balance))
        return balance
    
def withdraw_night(balance, money):
    commission = 100
    if balance >= money:
        print('{}원이 출금되었으며 수수료는 {}원이고, 잔액은 {}원입니다.'.format(money + commission, commission, balance-money-commission))
        return balance - money - commission
    else:
        print['잔액이 부족합니다. 현재 잔액은 {}원 입니다.'.format(balance)]



balance = 0
balance = deposit(balance, 1000)
print(balance)
balance = withdraw(balance, 500)
print(balance)
balance = withdraw(balance, 1000)
print(balance)
balance = withdraw_night(balance, 300)
print(balance)