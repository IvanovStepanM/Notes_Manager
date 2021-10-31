# This program generates unique ID for a new note.
class idgenerator:

    def main():
            import random
            import pickle
            FILENAME = 'notes.dat'
            try:
                input_file = open(FILENAME, 'rb') # open the notes file (binary, reading)
                notes_dct = pickle.load(input_file)
                input_file.close()
            except EOFError:    # if can't open the file
                notes_dct = {} # then create an empty dictionary.
            id = random.randint(0, 9)   # First let's generate a random number from 0 to 9 to make id search easy.
            if id in notes_dct:             # If such number alreay exists then
                id = random.randint(0, 99)      # let's try a two-digit number for id.
                #print(list(my_notes))
                return id
            else:
                #print(list(my_notes))
                return id
    main()

#idgenerator.main()