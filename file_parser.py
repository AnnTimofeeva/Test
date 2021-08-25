from customer_account import Customer_account


class FileParser():
#test 1
    def read_customer_accounts(self, filename):

        customer_accounts = []
        try:
            fo = open(filename, "r")

            # store the file contents as a list of strings
            lines = fo.readlines()
            fo.close()
        except IOError:
            print(f"Warning: Could not open file {filename} for reading.")
            input("Return to continue...")
            # return the empty list of customers
            return customer_accounts
        # parse each line of accounts file and create a Account object
        for line in lines:
            account = self.parse_customer_accounts_text(line)
            customer_accounts.append(account)
        
        return customer_accounts
#--------------------------------------------------------------------------
# reads lines from file accounts.txt and builds new Customer_account object using this info
    def parse_customer_accounts_text(self, accounts_text):

        fields = accounts_text.split("|")

        firstname = fields[0]
        lastname = fields[1]
        PPSN = fields[2]
        account_type = fields[3]
        overdraft = fields[4]
        balance = float(fields[5])
        interest_rate = float(fields[6])
        account_number =int(fields[7])
        #def __init__(self, firstname, lastname, PPSN,account_type, overdraft, balance, interest_rate, account_number=0):
        return Customer_account(firstname, lastname, PPSN, account_type, overdraft, balance, interest_rate,account_number)

#-------------------------------------------------------------------------------------------
# for each Customer account object in the programs writes line in the file accounts.txt to store data about this object
#1 object - 1 line in the file separated | symbol
    def write_customer_accounts(self, filename, customer_accounts):
        

        # list to contain text versions of accounts for writing
        lines = []
        first_account = True

        # build a list of customer accounts file strings
        for account in customer_accounts:
            if first_account == True:
                lines.append(account.file_text())
                first_account = False
            else:
                # if this isn't the first account, add a newline before writing
                lines.append(f"\n{account.file_text()}")
        
        try:
            fo = open(filename, "w")
            fo.writelines(lines)
            fo.close()
        except IOError:
            print(f"Warning: Could not open {filename} for writing")
            input("Return to continue...")