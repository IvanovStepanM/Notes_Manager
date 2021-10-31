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

def main(): 
    mynotes = load_notes()
    choice = 0 # variable for user's choice

    while choice != QUIT:
        choice = user_interface.get_menu_choice()
        if choice == LOOK_UP:
            look_up(mynotes)
        elif choice == ADD:
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
        elif choice == GETTXT:
            gettxt.gettxt(mynotes)
        elif choice == RESTORETXT:
            restoretxt.restoretxt() # recover notes from *.txt file
            mynotes = load_notes()  # update note list in this program
            save_notes(mynotes)     # save changes
        

# now we define all the functions listed above as actions from the menu related to the notes


def load_notes():
    try:
        input_file = open(FILENAME, 'rb') # open the notes file (binary, reading)
        notes_dct = pickle.load(input_file)
        input_file.close()
    except EOFError: # if can't open the file
        notes_dct = {} # then create an empty dictionary
    return notes_dct

def save_notes(mynotes):
    output_file = open(FILENAME, 'wb') # writing, binary code
    pickle.dump(mynotes, output_file) # pickle the dictionary and save it.
    output_file.close()

def look_up(mynotes): # show a note
        print("there are ", len(mynotes), "notes saved, their IDs are like the following:", list(mynotes)[0:10], '...')
        id = int(input('Enter ID to search:'))
        if id in mynotes:
            print("Here's data for the note with id", id, ':')
        print(mynotes.get(id, 'note with this ID is not found'))

def add(mynotes):
    title = input('Title:') # user inputs data for a new note
    further = input('Do you want to type note''s text now? (y/n)')
    if further.lower() == 'y':
        text = input('Text:')
        if text != '':
            date = dt.today()
            id = idgenerator.main()
            completed = int(True)
            datecompleted = dt.today()
            days_to_complete = datecompleted - date
            days_to_complete = days_to_complete.days
            message = 'It took %i days to complete this note' % (days_to_complete)
        else:
            text = 'No text'
            date = dt.today()
            id = idgenerator.main()
            completed = int(False)
            datecompleted = 'Not completed'
            message = 'None'
            entry = Note.Note(id, date, title, text, completed, datecompleted, message) # create a Note object
            mynotes[id] = entry
            print('The note has been added with ID: %i.' % (id))
            return None
    else:
        text = 'No text'
        date = dt.today()
        id = idgenerator.main()
        completed = int(False)
        datecompleted = 'Not completed'
        message = 'None'
    entry = Note.Note(id, date, title, text, completed, datecompleted, message) # create a Note object
    mynotes[id] = entry
    print('The note has been added with ID: %i.' % (id))

    
def change(mynotes):
    id = int(input('Enter ID to search:'))

    if id in mynotes:
        option = input('Do you want to change the title? (y/n)')
        if option.lower() == 'y':
            title = input('Enter a new TITLE for a note with this ID:')
            text = input('Enter a new TEXT for a note with this ID:')
            if text != '':
                completed = int(True)
                datecompleted = str(dt.today())
                days_to_complete = datecompleted - date
                days_to_complete = days_to_complete.days
                message = 'It took %i days to complete this note' % (days_to_complete)
                entry = Note.Note(id, date, title, text, completed, datecompleted, message)
                mynotes[id] = entry # update the entry
                print('Note updated.')
            else:
                completed = int(False)
                datecompleted = 'Not completed'
                message = 'None'
                entry = Note.Note(id, date, title, text, completed, datecompleted, message)
                mynotes[id] = entry # update the entry
                print('Note updated.')
        else:
            title = mynotes[id].get_title()
            text = input('Enter a new TEXT for a note with this ID:')
            if text != '':
                date = mynotes[id].get_date()
                completed = int(True)
                datecompleted = dt.today()
                days_to_complete = datecompleted - date
                days_to_complete = days_to_complete.days
                message = 'It took %i days to complete this note' % (days_to_complete)
                entry = Note.Note(id, date, title, text, completed, datecompleted, message)
                mynotes[id] = entry # update the entry
                print('Note updated.')
            else:
                date = mynotes[id].get_date()
                completed = int(False)
                datecompleted = 'Not completed'
                message = 'None'
                entry = Note.Note(id, date, title, text, completed, datecompleted, message)
                mynotes[id] = entry # update the entry
                print('Note updated.')
    else:
        print('There is no note with this ID.')


def delete(mynotes):
    id = int(input('Enter the ID of the note to delete:'))
             
    # If ID is found, delete the entry.
    if id in mynotes:
        del mynotes[id]
        print('Entry deleted.')
    else:
        print('There is no note with this ID.')

main()