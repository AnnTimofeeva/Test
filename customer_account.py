# class Customer_account:
# Demonstration of git commands
from util import Util

# when creating new Customer account instance, we automatically assign new account number adding 1 to the previous account number
# and store next account number as a class property
class Customer_account:

    next_account_number = 1

    def __init__(self, firstname, lastname, PPSN,account_type, overdraft, balance, interest_rate, accnt_number=0):
        
        if accnt_number != 0:
            self._account_number = accnt_number
            Customer_account.next_account_number = self._account_number+1
        else: 
              
            self._account_number = Customer_account.next_account_number
            Customer_account.next_account_number = Customer_account.next_account_number + 1

        self._firstname = firstname
        self._lastname =  lastname 
        self._PPSN = PPSN
        self._account_type = account_type
        self._overdraft = overdraft
        self._balance = balance
        self._interest_rate = interest_rate
    

# this method displays list of all accounts crerated in the system matching the PPS number provived by user
    def print_search_results(self):
        repr = f"{self.firstname.ljust(10)} {self.lastname.ljust(15)} "
        repr = repr + f"{self.PPSN.ljust(10)} {str(self.account_number).ljust(10)} {self.account_type.ljust(15)} {self.overdraft.ljust(15)} "
        repr = repr + f"{float(self.interest_rate)}%"

        return repr

# this method displas list of all accounts crerated in the system    

    def __repr__(self):
        repr = f"{self.firstname.ljust(15)} {self.lastname.ljust(15)} "
        repr = repr + f"{str(self.account_number).ljust(10)} {str(float(self.balance)).ljust(10)} "
        repr = repr + f"{self.interest_rate}"

        return repr

# this method prepares customer accounts data for writnig in the txt file    
    def file_text(self):
    
        return f"{self.firstname}|{self.lastname}|{self.PPSN}|{self.account_type}|{self.overdraft}|{self.balance:.2f}|{self.interest_rate}|{self.account_number}" 

# this method updates customer accounts data when user makes transactions
#when account has no overdraft option and transaction sum insuffisient to withdraw, whole transaction cancels
# if new balance >10000 euro, interest rate updates to 5%
    def update(self, new_balance,ds):
        overdraft = self.overdraft
        #print(f"Your current balance = {self.balance}")
        if (overdraft=="N") and (new_balance<0):
            Util.press_return("Insuffisient funds, transaction cancelled. Press return to continue...")
            return False
        else:    
            self.balance = new_balance
            if (self.balance)>10000:
                self.interest_rate=5.00
            else:
                self.interest_rate=2.00
            print(f"Transaction successfully completed. Account number {self.account_number} is updated. It's balance = {self.balance}\n")
            Util.press_return("Press return to continue...")    
        return True

# setters and getters
    @property
    def account_number(self):
        return self._account_number
    
    @account_number.setter
    def account_number(self, new_account_number):
        self._account_number = new_account_number


    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstame(self, new_firstname):
        self._firstname = new_firstname

    @property
    def lastname(self):
        return self._lastname

    @lastname.setter
    def lastname(self, new_lastname):
        self._lastname = new_lastname

    @property
    def PPSN(self):
        return self._PPSN

    @PPSN.setter
    def PPSN(self, new_PPSN):
        self._PPSN = new_PPSN

    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, new_account_type):
        self._account_type = new_account_type

    @property
    def overdraft(self):
        return self._overdraft

    @overdraft.setter
    def overdraft(self, new_overdraft):
        self._overdraft = new_overdraft

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        self._balance = new_balance

    @property
    def interest_rate(self):
        return self._interest_rate
    
    @interest_rate.setter
    def interest_rate(self, new_interest_rate):
        self._interest_rate = new_interest_rate
