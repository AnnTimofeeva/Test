import os

class Util:
#utility class to store some additional methods 
    @staticmethod
    def clear_screen():
        os.system('cls')

    @staticmethod
    def  press_return(message):
        print (message)
        input()        