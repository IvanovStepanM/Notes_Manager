##notes_manager## this program manages notes
##It uploads menu from user_interface file and contains instructions for entered commands.

import pickle                           # technical imports
from datetime import date as dt

import Note                             # import of *.py files from working directory
from idgenerator import idgenerator
from user_interface import user_interface
from stats import stats
from gettxt import gettxt
from restoretxt import restoretxt

# Global constants for menu choices
ADD = 1
LOOK_UP = 2
CHANGE = 3
DELETE = 4
QUIT = 5
STATS = 6
GETTXT = 7
RESTORETXT = 8
# Global constant for the filename
FILENAME = 'notes.dat'

def main():                             ## main function loads notes and checks user's menu choice
    mynotes = load_notes()              # loads notes from data file
    choice = 0 # variable for user's choice

    while choice != QUIT:               
        choice = user_interface.get_menu_choice()   # loads user interface from user_interface.py
        if choice == LOOK_UP:               # here it checks what user have entered
            look_up(mynotes)                # and calls for a function to execute. In this case - to show a note by ID.
        elif choice == ADD:                 # Here- to add a new note
            add(mynotes)
            save_notes(mynotes) # save a new note to the file
        elif choice == CHANGE:
            change(mynotes)
            save_notes(mynotes) # save changed note to the file
        elif choice == DELETE:
            delete(mynotes)
            save_notes(mynotes) # delete a note from the file
        elif choice == STATS:
            stats.stats(mynotes)
        elif choice == GETTXT:                 # This one is to get a *.txt file of a current database 
            gettxt.gettxt(mynotes)
        elif choice == RESTORETXT:
            restoretxt.restoretxt() # recover notes from *.txt file
            mynotes = load_notes()  # update note list in this program
            save_notes(mynotes)     # save changes
        

# now we define all the functions listed above as actions from the menu related to the notes


def load_notes():       # This function loads notes from a database
    try:
        input_file = open(FILENAME, 'rb') # open the notes file (binary, reading)
        notes_dct = pickle.load(input_file)
        input_file.close()
    except IOError: # if can't open the file
        notes_dct = {} # then create an empty dictionary
    return notes_dct

def save_notes(mynotes):    # This function saves notes back to database.
    output_file = open(FILENAME, 'wb') # writing, binary code
    pickle.dump(mynotes, output_file) # pickle the dictionary and save it.
    output_file.close()

def look_up(mynotes): # show a note
        print("there are ", len(mynotes), "notes saved, their IDs are like the following:", list(mynotes)[0:10], '...')
        id = int(input('Enter ID to search:'))
        if id in mynotes:
            print("Here's data for the note with id", id, ':')
        print(mynotes.get(id, 'note with this ID is not found'))

def add(mynotes):   # This function adds a new note.
    title = input('Title:') # user inputs title for a new note
    further = input('Do you want to type note''s text now? (y/n)') # then it asks if a user wants to type a text of a note.
    if further.lower() == 'y':          # If yes a user will input a text.
        text = input('Text:')
        if text != '':                  
            date = dt.today()           # The function saves parameters of a note.
            id = idgenerator.main()     # Here it calls for idgenerator.py to generate a unique ID.
            completed = int(True)       # In this case the note is considered complete, beause
            datecompleted = dt.today()  # It has a title and a text.
            days_to_complete = datecompleted - date # It also calculates how long it took to complete the note.
            days_to_complete = days_to_complete.days
            message = 'It took %i days to complete this note' % (days_to_complete)
        else:                           # Alternatively, note's text can be left empty.
            text = 'No text'
            date = dt.today()
            id = idgenerator.main()
            completed = int(False)      # In this case the note is considered as not complete.
            datecompleted = 'Not completed'
            message = 'None'
            entry = Note.Note(id, date, title, text, completed, datecompleted, message) # create a Note object
            mynotes[id] = entry
            print('The note has been added with ID: %i.' % (id))
            return None
    else:                               # With a same result as above, user can refuse to type text now.
        text = 'No text'
        date = dt.today()
        id = idgenerator.main()
        completed = int(False)
        datecompleted = 'Not completed' # In this case the note is also considered as not complete.
        message = 'None'
    entry = Note.Note(id, date, title, text, completed, datecompleted, message) # create a Note object
    mynotes[id] = entry
    print('The note has been added with ID: %i.' % (id))

    
def change(mynotes):                    # This function changes the existing note.
    id = int(input('Enter ID to search:'))  # by its ID.

    if id in mynotes:
        option = input('Do you want to change the title? (y/n)')    # A user is aksed if he wants to change the title.
        if option.lower() == 'y':
            title = input('Enter a new TITLE for a note with this ID:') # First the title is being changed.
            text = input('Enter a new TEXT for a note with this ID:')   # Then it asks for a text for the note.
            if text != '':                                              # This if-else statements check
                completed = int(True)                                   # if user actually filled the text
                date = mynotes[id].get_date()
                datecompleted = dt.today()
                days_to_complete = datecompleted - date
                days_to_complete = days_to_complete.days
                message = 'It took %i days to complete this note' % (days_to_complete)
                entry = Note.Note(id, date, title, text, completed, datecompleted, message)
                mynotes[id] = entry # update the entry
                print('Note updated.')
            else:                                                       # or if he left the text blank.
                completed = int(False)
                date = mynotes[id].get_date()
                datecompleted = 'Not completed'
                message = 'None'
                entry = Note.Note(id, date, title, text, completed, datecompleted, message)
                mynotes[id] = entry # update the entry
                print('Note updated.')
        else:                                                           # This part is the same but in case user refused to
            title = mynotes[id].get_title()                             # change the title.
            text = input('Enter a new TEXT for a note with this ID:')
            if text != '':                                              # If user filled the text,
                date = mynotes[id].get_date()                           # then samely the note is considered complete.
                completed = int(True)
                datecompleted = dt.today()
                days_to_complete = datecompleted - date
                days_to_complete = days_to_complete.days
                message = 'It took %i days to complete this note' % (days_to_complete)
                entry = Note.Note(id, date, title, text, completed, datecompleted, message)
                mynotes[id] = entry # update the entry
                print('Note updated.')
            else:                                                       # If user left the text blank,
                date = mynotes[id].get_date()                           # then samely the note is considered incomplete.
                completed = int(False)
                datecompleted = 'Not completed'
                message = 'None'
                entry = Note.Note(id, date, title, text, completed, datecompleted, message)
                mynotes[id] = entry # update the entry
                print('Note updated.')
    else:
        print('There is no note with this ID.') # this message appears when there is no note with such ID.
                                            ## probably this "add" function could be shorter, but its features had been added
                                             ## step by step so I've decided not to re-write it.

def delete(mynotes):                            # This function deletes note by its ID.
    id = int(input('Enter the ID of the note to delete:'))
             
    # If ID is found, delete the entry.
    if id in mynotes:
        del mynotes[id]
        print('Entry deleted.')
    else:
        print('There is no note with this ID.')

main()