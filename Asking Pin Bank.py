correct_pin = 1234
balance = 5000

try:
        user_pin = int(input('Enter your PIN: '))
except ValueError :
        print('Enter a valid pin')
        exit()

if user_pin == correct_pin:
        print('PIN Correct')
        print('Option: A = Balance')
        print('Option: B = Deposit')
        print('Option: C = Withdraw')
        Option = input('Enter option: ').upper()
        if Option == "A":
            print('Your balance is: RS.',balance)
            
        elif Option == "B":
            amount = int(input('Deposit Amount: '))
            balance += amount
            print('Current Balance: ',balance)
            
        elif Option == "C":
            amount = int(input('Enter withdrawal amount: '))
            
            if amount > balance:
                print('Inadequate Balance')
            else:
                balance = balance - amount
                print('Please take your cash.')
                print('Remaining balance is: RS.',balance)
                
        else:
            print('Enter a valid option')
            print('Retry')

else:
        print("Error")
        print('Invalid Pin!!!')

