# this program shows how many notes are stored, what percent of them are incomplete.
class stats:
    def stats(mynotes):
        print("there are ", len(mynotes), "notes saved.")  # shows how many notes saved.

        not_completed = sum([1 for i in mynotes if mynotes[i].get_completed() == 0])
        total_notes = len(mynotes)
        if not_completed == 0:
            print('There are no uncompleted notes.')  # if all the notes are complete.
        else:
            how_many = round(100*int(not_completed)/int(total_notes),1) # counts uncomplete notes
            print(how_many, '% of notes are not completed')

        
