class Book:
    def __init__(self, title, author, is_issued=False):
        self.title = title   #wignis saxeli
        self.author = author    #wignis avtori
        self.is_issued = is_issued  #wignis statusi

    def to_list(self):
        #csv-s formati
        return [self.title, self.author, 'Issued' if self.is_issued else 'Not Issued']

    def from_list(self, data):
        #statusis logika
        self.title, self.author, is_issued = data
        self.is_issued = is_issued == 'Issued'
