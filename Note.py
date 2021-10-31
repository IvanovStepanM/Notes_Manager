class Note:  # 
    # The _ _init_ _ method initializes the attributes.
    def __init__(self, id, date, title, text, completed, datecompleted, message):
        self.__id = id # int
        self.__date = date
        self.__title = title
        self.__text = text
        self.__completed = completed # bool
        self.__datecompleted = datecompleted
        self.__message = message

    def set_id(self, id):
        self.__id = id

    def set_date(self, date):
            self.__date = date

    def set_title(self, title):
        self.__title = title

    def set_text(self, text):
        self.__text = text

    def set_completed(self, completed):
        self.__completed = completed

    def set_datecompleted(self, datecompleted):
        self.__datecompleted = datecompleted

    def set_message(self, message):
        self.__message = message


    def get_id(self):
        return self.__id

    def get_date(self):
        return self.__date

    def get_title(self):
        return self.__title

    def get_text(self):
        return self.__text

    def get_completed(self):
        return self.__completed

    def get_datecompleted(self):
        return self.__datecompleted
   
    def get_message(self):
        return self.__message

    def __str__(self):                              # attributes to show
        return 'Title: ' + self.__title + \
            '\nText: ' + self.__text + \
            '\nDate_created: ' + str(self.__date) + \
            '\nDate_completed: ' + str(self.__datecompleted) + \
            '\nMessage: ' + str(self.__message) + \
            '\nCompleted: ' + str(self.__completed)