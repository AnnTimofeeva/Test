
from customer_account import Customer_account
from file_parser import FileParser

# this Class is dealing with reading and writing to accounts.txt file
class Datastore:

    def __init__(self):

        self._customer_accounts = []
        
        self.read_customer_accounts()

    def read_customer_accounts(self):

        file_parser = FileParser()
        self._customer_accounts = file_parser.read_customer_accounts("accounts.txt")

    
    def add_customer_account(self, customer_account):

        self._customer_accounts.append(customer_account)


    @property
    def customer_accounts(self):
        return self._customer_accounts
