class Movie:
    def __init__(self, title, gender):
        self.title = title
        self.gender = gender

    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, title):
        self.__title = title
    
    @property
    def gender(self):
        return self.__gender
    
    @title.setter
    def gender(self, gender):
        self.__gender = gender