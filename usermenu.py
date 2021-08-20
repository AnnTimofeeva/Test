from util import Util
from customer_account import Customer_account 
from file_parser import FileParser
from search_class import Search
# more comments to test git
#123 

class UserMenu():

# validates all balance inputs (for creating accounts and for making accounts transactions)
#if input is invalid, returns false, else returns balance
    def prompt_for_balance_input(self, message):

        balance_valid = False

        while balance_valid == False:
            try:
                balance = float(input(message))
            except ValueError:
                print("Sorry, invalid input. Please enter sum in digital format")
            else:
                balance_valid = True

        return balance
#----------------------------------------------------------------------------------------
#validates user info input for creating new account, returns false when invalid, else returs user info
    def prompt_for_user_info(self, message):
        input_valid = False

        while input_valid == False:
            try:
                user_info = str(input(message))
            except ValueError:
                print("Sorry, invalid input. Please enter user details")
            else:
                if user_info.isalpha():
                    input_valid = True

        return user_info  

#----------------------------------------------------------------------------------------
#validates user PPS number input (alphanumeric only), returns false when invalid or PPSN input
    def prompt_for_PPSN_input(self, message):
        input_valid = False

        while input_valid == False:
            try:
                PPSN_input = str(input(message))
            except ValueError:
                print("Sorry, invalid input. PPS number must be in alphanumeric format")
            else:
                if PPSN_input.isalnum():
                    input_valid = True

        return PPSN_input     
#----------------------------------------------------------------------------------------
#validates user account number input (integer only) for transactions, returns false when invalid or account number in integer format  
    def prompt_for_account_number(self, message):

        account_number_valid = False 

        while account_number_valid == False:
            try:
                account_number = int(input(message))
            except ValueError:
                print("Account number must be a numeric value")
            else:
                account_number_valid = True

        return account_number
#---------------------------------------------------------------------------------------
#validates user input for overdraft option (should be only Y, y, N, n characters), returns false when invalid or overdraft option input
    def prompt_for_overdraft_option(self, message):

        overdraft_option = None 
        
        while (overdraft_option  not in ["Y","N","y","n"]):
            try:
                overdraft_option = str(input(message))
            except ValueError:
                print("Please enter Y or N for overdraft option\n")
        return overdraft_option

#---------------------------------------------------------------------------------------

    def clearscreen(self):
        Util.clear_screen()   
#-------------------------------------------------------------------------------------------
    def do_user_menu(self, ds):

        selection = "0"

        while(selection != "9"):
            self.clearscreen()
            selection = self.show_user_menu(ds)

            if(selection not in ["1", "2", "3", "4","5","6","7","8","9"]):
                self.clearscreen()
                Util.press_return(f"Invalid menu option [{selection}]. Press return to try again.")

        # application is now exiting - write customer accounts list to file
        file_parser = FileParser()

        file_parser.write_customer_accounts("accounts.txt", ds.customer_accounts)
#------------------------------------------------------------------------------------------------
    def show_user_menu(self, ds):

        print(f"Welcome to Banking Account Management System!")
        print("**********************************************")
        print("Menu options:")
        print("1. View existing customer accounts")
        print("2. Create new customer account")
        print("3. View account information for PPSN")
        print("4. Transfer funds from one account to another")
        print("5. Withdraw from selected account")
        print("6. Make a deposit to selected account")
        print("7. Save data to file")
        print("8. Help")
        print("9. Exit\n")
        selection = input("Please choose an option (1-9): ")

        if(selection == "1"):
            print("View accounts\n")
            self.view_customer_accounts(ds)

        elif(selection == "2"):
            print("Add account\n")
            self.add_customer_accounts(ds)
        
        elif(selection =="3"):           
            print("Search in accounts\n")
            Search.general_search(ds)
        
        elif (selection =="4"):
            print("Make a transfer between two accounts\n")
            self.transfer_funds(ds)

        elif(selection =="5"):
            print("Make a withdrawal from account\n")
            self.withdraw_funds(ds)
            

        elif( selection =="6"):
            print("Make a deposit to account\n")
            self.deposit_funds(ds)

        elif (selection=="7"):
            print("Saving data to file")
            self.save_data_tofile("accounts.txt",ds) 

        elif (selection=="8"):
            print("Help info about this App")
            self.user_help()   

        return selection
#--------------------------------------------------------------------------------------------------------
# displays help info when user selects menu option number 8
    def user_help(self):
        self.clearscreen()
        print("*****************************************************")
        print("Thank you for using Banking Customer Management System!")
        print("When the App starts, please choose option from 1-9:")
        print("After choosing option 1-9 you will be asked to provide input for further operations")
        print("Please, read carefully what input you need to provide")
        print("Our helpline is accessable via phone 111-333-444 or by email helpline@bankingapp.centralbank.com")
        Util.press_return("Press return to go back to the main menu")   


#--------------------------------------------------------------------------------------------------------
# saves all accounts in the system to accounts.txt file - option 7 user menu
    def save_data_tofile(self,filename, ds):
        file_parser = FileParser()
        file_parser.write_customer_accounts(filename, ds.customer_accounts)
        Util.press_return(f"Your data is saved in file {filename}. Press return to continue...")
     
#--------------------------------------------------------------------------------------------------------
# displays list of all accounts in the system - option 1 in the user menu
    def view_customer_accounts(self, ds):
        self.clearscreen()
        print ("List of all accounts")
        print("Firstname      Lastname     Account №   Balance   Interest rate(%)")
        print("=====================================================================")

        for account in ds.customer_accounts:
            print(account)

        Util.press_return("Press return to continue")     
#---------------------------------------------------------------------------------------------------------
# makes money withdrawal from account provided by user - option 5 in the user menu
    def withdraw_funds(self,ds):
        account_number = self.prompt_for_account_number("Enter the account number for withdrawal: ")
        account_to_withdraw = Search.search_by_account_number(ds,account_number)
        
        if (account_to_withdraw!=None):
            withdrawal_sum  = self.prompt_for_balance_input("Enter the sum to withdraw: ")                
            new_balance = int(account_to_withdraw.balance)-int(withdrawal_sum)
            account_to_withdraw.update(new_balance,ds)
        else: 
            print(f"Account N {account_number} not found. Please check the input and try again") 
            Util.press_return("Press return to continue")     

#---------------------------------------------------------------------------------------------------------
# makes transfer between accounts provided by user - option 4 in the user menu
    def transfer_funds(self,ds):     
        
        sender_account_number = self.prompt_for_account_number("Enter the sender account number: ")
        account_to_send = Search.search_by_account_number(ds,sender_account_number)
        if (account_to_send!=None): 
            receiver_account_number= self.prompt_for_account_number("Enter the recepient account number: ")  
            account_to_receive = Search.search_by_account_number(ds,receiver_account_number)

            if (account_to_receive!=None):
                transfer_sum = self.prompt_for_balance_input("Enter the sum to transfer: ")
                    
                print(f"Would you like to transfer {transfer_sum} from account number {sender_account_number} to account number {receiver_account_number}?")
                userinput = input("Press Y to continue or any other key to cancel\n") 
                if (userinput.upper()=="Y"):
                    new_sender_balance = int(account_to_send.balance)-int(transfer_sum)
                    if (account_to_send.update(new_sender_balance,ds)==True):
                        new_recepient_balance =int(account_to_receive.balance)+int(transfer_sum)
                        account_to_receive.update(new_recepient_balance,ds)     
                else:
                    Util.press_return("Transaction cancelled. Press return to continue")
            elif (account_to_receive==None):
                print(f"Account N {receiver_account_number} not found. Please check the input and try again")   
                Util.press_return("Press return to continue")             
                            
        elif (account_to_send==None): 
                print(f"Account N {sender_account_number} not found. Please check the input and try again") 
                Util.press_return("Press return to continue")
                    
                  
#--------------------------------------------------------------------------------------------------------
# makes a deposit to account number provided by user  - option 6 in the user menu 
    def deposit_funds(self,ds):
        account_number= self.prompt_for_account_number("Enter the account number for deposit: ")
        account_to_deposit = Search.search_by_account_number(ds,account_number)
        
        if (account_to_deposit!=None):
                deposit_sum = self.prompt_for_balance_input("Enter the amount of money for deposit: ")
                new_balance = int(account_to_deposit.balance)+int(deposit_sum)
                account_to_deposit.update(new_balance,ds)
        else:
                print(f"Account N {account_number} not found. Please check the input and try again")   
                Util.press_return("Press return to continue")       
#---------------------------------------------------------------------------------------------------------
#creates new account with user deatails provided
#if it is deposit account - opening balance is 50 by default, if current account - 25
# interest rate =2% by deafault
    def add_customer_accounts(self, ds):
        print("Add a new customer account")
        print("===========================\n")

        firstname   = self.prompt_for_user_info("First name: ")
        lastname    = self.prompt_for_user_info("Last name: ")
        PPSN        = self.prompt_for_PPSN_input("PPSN: ")
        
        overdraft   = self.prompt_for_overdraft_option("Please enter Y or N for overdraft option\n")
                    
        account_type = None
        
        while account_type == None:
            try:
                account_type= int(input("Please enter account type (1 for deposit account, 2 for current account): "))
                if account_type==1:
                    str_account_type = "deposit"
                    balance = 50.00
                elif account_type==2:
                    str_account_type = "current"
                    balance = 25.00
                else: 
                    raise ValueError
            except:
                print("Invalid account type. Please enter 1 for deposit account, 2 for current account")
                account_type = None
                continue
        #creates new account object and appends it to the account list in Datastore class                 
        customer_account = Customer_account(firstname, lastname, PPSN,str_account_type, overdraft.upper(), balance, interest_rate=2.0)
        ds.add_customer_account(customer_account)
        print(f"Account N {customer_account._account_number} for {customer_account.firstname} {customer_account.lastname} has been created")

        Util.press_return("Press return to continue")

    
