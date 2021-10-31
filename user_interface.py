class user_interface(): # Prints out menu options and accepts the command from user to transfer back to the notes_manager.


    def get_menu_choice():
        print('------------------------------------------------------')
        print('Menu')
        print('---------------------------')
        print('1. Add a note')
        print('2. Show a note')
        print('3. Update a note')
        print('4. Delete a note')
        print('5. QUIT the program')
        print('------')
        print('6. See statistics')
        print('7. Write down all notes to *.txt file')
        print('8. Restore notes from *.txt file')
        print()

        #Get the user's choice.
        while True:
            try:
                choice = int(input('Enter your choice: '))
                print('______________________________________________________')
                return choice
            except ValueError: # in case user writes non integer value
                print('Please type a number from menu options.')

#get_menu_choice()