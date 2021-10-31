class gettxt:       # This program creates a back-up output file "notes.txt" as a copy of data in "notes.dat".
    def gettxt(mynotes):
        import pickle
        FILENAME = 'notes.txt'                      # the data will be uploaded to this txt file
        output_file = open(FILENAME, 'wb')
        pickle.dump(mynotes, output_file)           # saves mynotes to *.txt file
        output_file.close()
        print('All notes were saved to the notes.txt file')