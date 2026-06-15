"""
Question

Write a Python program to create a simple ATM system. The program should ask the
user to enter a PIN. If the PIN is correct, display options to check balance, deposit
money, or withdraw money. If the PIN is incorrect, display ‘Invalid PIN’. While
withdrawing, the program should check whether the account has sufficient balance.
Bonus (optional ):
Display ‘Insufficient Balance’ if the withdrawal amount is greater than the
available balance
"""

correct_pin = '1234'
balance = 5000

user_pin = input('Enter your PIN: ')

if user_pin == correct_pin:
        print('PIN Correct')
        print('Option: A = Balance')
        print('Option: B = Deposit')
        print('Option: C = Withdraw')
        
        Option = input('Enter option: ')
        
        if Option == "A":
            print('Your balance is: RS.' + str(balance))
            
        elif Option == "B":
            amount = int(input('Deposit Amount: '))
            balance = balance + amount
            print('Current Balance: ' + str(balance))
            
        elif Option == "C":
            amount = int(input('Enter withdrawal amount: '))
            
            if amount > balance:
                print('sInadequate Balance')
            else:
                balance = balance - amount
                print('Please take your cash.')
                print('Remaining balance is: RS.' + str(balance))
                
        else:
            print("Error")
            print('Invalid Pin!!!')

else:
        print('Wrong PIN')
        print('Retry!!!')
