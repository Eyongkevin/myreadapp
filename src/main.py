from src.db.models import reader

class MenuDisplay:

    @staticmethod
    def display_main_menu():
        print(
            """
        WELCOME TO MY READ APP

        MENU
        ------------
        1. DATA MANIPULATION
        2. DATA QUERY
        00. QUIT
            """
        )
    
    @staticmethod
    def display_DM_menu():
        print(
            """
        1. INSERT READER
        2. INSERT BOOK
        3. INSERT MYREAD
        99. BACK
            """
        )



def main():
    while True:
        MenuDisplay.display_main_menu()
        option: int = int(input('Choose an option to continue: '))

        if option == 1:
            # TODO: OPERATION FOR MANIPULATION
            while True:
                MenuDisplay.display_DM_menu()
                option: int = int(input('Choose an option to continue: '))

                if option == 1:
                    # TODO: INSERT READER
                    pass
                elif option == 2:
                    # TODO: INSERT BOOK
                    pass
                elif option == 3:
                    # TODO: INSERT MYREAD
                    pass
                elif option == 99:
                    break
                else:
                    print('Option not recognized. Please, try again')
                    

        elif option == 2:
            # TODO: OPERATIONS FOR QUERY
            pass
        
        elif option == 0:
            print('PROGRAM IS QUITING')
            break
        else:
            print('Option not recognized. Please, try again')




if __name__ == '__main__':
    main()