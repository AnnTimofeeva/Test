from util import Util

# this class is dealing with 2 accounts search options - search by account number, saerch by PPS number
class Search:

    @staticmethod
    def general_search(ds):
            Util.clear_screen()
            #print(book_list)
            search_info = input("Please enter PPSN you are looking for\n")
            search_list = []
            print("================================================")
            

            for account in ds.customer_accounts:
                #if (account.PPSN.count(search_info)):
                if (account.PPSN==search_info):
                    search_list.append(account)                         
                else:
                    continue
                
            print(f"Results fount: {len(search_list)}\n")
            print("Firstname    Lastname    PPSN      Account №  Account type  Overdraft(Y/N)  Interest rate(%)")
            print("===========================================================================================")
            for result in search_list:
                print(result.print_search_results())
        
            if len(search_list) == 0:
                print(f'There are no accounts with this PPSN')

            input("Return to continue...")


    @staticmethod
    def search_by_account_number(ds, account_number):
            search_info = account_number
            search_list = []
            found_account=None

            for account in ds.customer_accounts:
                if (account.account_number==search_info):
                    found_account =  account
                    break                       
                else:
                    continue
                
            return  found_account   
