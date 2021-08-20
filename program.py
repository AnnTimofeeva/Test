from datastore import Datastore 
from usermenu import UserMenu 
# main program file
datastore = Datastore()
user_menu = UserMenu()

user_menu.do_user_menu(datastore)

