#create a class handles the core operation of atm
class ATM:
    def __init__(self):  #default constructor
        self.balance=0  #initialize

    def check_balance(self):
        return self.balance
    
    def deposit(self, amount):
        if amount <=0:
            raise ValueError("Invalid amount!Deposit must be +ve")
        self.balance += amount

    def withdraw(self, amount):  # Fixed indentation
        if amount <=0:
            raise ValueError("Invalid amount!withdraw must be +ve")
        if amount > self.balance:
            raise ValueError('Insufficient amounts.')
        self.balance -= amount

#create a class for interaction
class ATMController:
    def __init__(self):
        self.atm = ATM() # create atm obj

    def get_number(self, prompt):
        while True:
            try:
                number = float(input(prompt))
                return number
            except ValueError:
                print('Please enter a valid number.')

    def display_menu(self):   #atm menu options
        print('\nWelcome to the ATM!')
        print('1. Check Balance')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Exit')    

    def check_balance(self):
        balance = self.atm.check_balance()
        print(f'Your current balance is: NPR{balance}')   
    
    def deposit(self):
        while True:
            try:
                amount = self.get_number('Enter the amount to deposit: ')
                self.atm.deposit(amount)
                print(f'Successfully deposited NPR{amount}.')
                break
            except ValueError as error:
                print(error)
 
    def withdraw(self):  # Fixed indentation
        while True:
            try:
                amount = self.get_number('Enter the amount to withdraw: ')
                self.atm.withdraw(amount)
                print(f'Successfully withdrew NPR{amount}.')
                break
            except ValueError as error:
                print(error)    

    def run(self):  # Fixed indentation (now properly part of ATMController)
        while True: 
            self.display_menu()
            choice = input('Please choose an option: ')
            if choice == '1':
                self.check_balance()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                print('Thank you for using the ATM.')
                break
            else:
                print('Invalid choice. Please try again.')


def main():
    #Main function to start the program
    atm = ATMController()
    atm.run()


if __name__ == '__main__':
    main()