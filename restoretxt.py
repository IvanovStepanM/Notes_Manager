# This program restores "notes.dat" file from a back-up file "notes.txt".
#  Works both when "notes.dat" is lost or when you want to come back to an old version, saved in *.txt

class restoretxt:        
         
        def restoretxt():
            import pickle   
            FILENAME = 'notes.txt'              # back up text file
            FILENAMETOREWRITE = 'notes.dat'     # this database will be re-writen
            def load_notes():                   # first we extract data from the text file
                try:
                    input_file = open(FILENAME, 'rb') # open the notes *.txt file (binary, reading)
                    notes_dct = pickle.load(input_file) # load data from *.txt file.
                    input_file.close()
                    return notes_dct
                except FileNotFoundError:                                                # Exception in case
                    print('Failure: there is no note.txt file in a working directory.')  # there is not text file in wd.
                
            mynotes = load_notes()
            try:
                output_file = open(FILENAMETOREWRITE, 'wb') # writing, binary code
                pickle.dump(mynotes, output_file) # try to copy from *.txt to *.dat
                output_file.close()
                
                print('Notes were restored from notes.txt file')       # <= if all fine, this will appear.
            
            except IOError: # if notes.txt was empty
                print('For some reason dataset in the text file was empty.') # but why would you do that?

        