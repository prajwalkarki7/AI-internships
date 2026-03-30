class Accountholder:
    all_accounts = []

    def __init__(self, first_name, last_name, account_number):
        self.first_name = first_name
        self.last_name = last_name
        self.account_number = account_number

    def client_info():
        name = input("Enter the first name: ")
        caste = input("Enter your last name: ")
        number = input("Enter your account number: ")
        
        new_obj = Accountholder(name, caste, number)
        Accountholder.all_accounts.append(new_obj)
        print(f"Account created for {name}!")
        return new_obj
       
class Transaction:
    balance = 1000
    transactions=[]
    
    def deposit():
        Accountholder.client_info()
        
        search_num = input("Enter your account number to search: ")
        

        matches = list(filter(lambda acc: acc.account_number == search_num, Accountholder.all_accounts))
        
        if matches:
            amount = int(input("Enter deposit amount: "))
            Transaction.balance += amount
            print(f"Success! balance is now: {Transaction.balance}")
            Transaction.transactions.append(Transaction.balance)
        else:
            print("Account not found.")
    
    def withdraw():
        search_num = input("Enter your account number to search: ")
        
        matches = list(filter(lambda acc: acc.account_number == search_num, Accountholder.all_accounts))
        
        if matches:
            amount = int(input("Enter withdrawal amount: "))
            if amount > Transaction.balance:
                print("Insufficient funds.")
            else:
                Transaction.balance -= amount
                print(f"Success! balance is now: {Transaction.balance}")
                for acc in Accountholder.all_accounts:
                 Transaction.transactions.append(Transaction.balance)
        else:
            print("Account not found.")
    
    def display_transactions():
        search_num = input("Enter your account number to search: ")
        
        matches = list(filter(lambda acc: acc.account_number == search_num, Accountholder.all_accounts))
        if matches:
         for acc in Accountholder.all_accounts:
            print(f"All transactions for {acc.first_name} is: {Transaction.transactions}")

    def Delete():
       search_num = input("Enter your account number to search: ")
       matches = list(filter(lambda acc: acc.account_number == search_num, Accountholder.all_accounts))
       if matches:
              Accountholder.all_accounts.remove(matches[0])
              print("Account deleted successfully.")
        
       else:
        print("Account not found.")
        

class main:
        while True:
            choice = input("Enter 1 to deposit, 2 to withdraw, or 3 to view transaction details, 4 to delete an account:, 5 to logout ")
            if choice == '1':
                Transaction.deposit()
            elif choice == '2':
                Transaction.withdraw()
            elif choice == '3':
                Transaction.display_transactions()
            elif choice=='4':
                Transaction.Delete()
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

obj=main()