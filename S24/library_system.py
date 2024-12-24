import enum
class BookGenre(enum.Enum):

    FICTION = 1
    NON_FICTION = enum.auto()
    SCIENCE = enum.auto()
    HISTORY = enum.auto()
    BIOGRAPHY = enum.auto()

class MembershipLevel(enum.Enum):
    BASIC = 100
    PREMIUM = 200
    GOLD = 500    

class BookNotAvailableError(Exception):
    pass

class LateReturnError(Exception):
    pass

class InvalidMembershipError(Exception):
    pass

class Book:
     def __init__(self,title, genre, is_available ):
        self._title = title
        self._genre = genre
        self._is_available = is_available

     @property
     def title(self):
        return self._title
     @title.setter
     def title(self, new_title):
        if isinstance(new_title, str) and len(new_title) > 0:
            self._title = new_title
        else:
            raise ValueError("Invalid title name")

     @property
     def genre(self):
        return self._genre     

     @genre.setter
     def genre(self, new_genre):
        if new_genre in BookGenre:
            self._genre = new_genre
        else:
            raise ValueError("Invalid genre")

     @property
     def is_available(self):
        return self._is_available

     @is_available.setter
     def is_available(self, new_is_available):
        if isinstance(new_is_available, bool):
            self._is_available = new_is_available

     def borrow(self):  
      if self.is_available == False:
        raise BookNotAvailableError(f"{self.title} is not available")
      self.is_available = False
    
     def return_book(self,is_late):
      if not isinstance(is_late, bool):
        raise TypeError("is_late must be a boolean value (True or False).")
      if is_late == True:
        raise LateReturnError(f"{self.title} is late")
      self.is_available = True

class Member:
    def __init__(self,name,membership_level):
        self._name = name
        self._membership_level = membership_level
      

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name) > 0:
            self._name = new_name
        else:
            raise ValueError("Invalid name")

    @property
    def membership_level(self):
        return self._membership_level
    
    @membership_level.setter
    def membership_level(self, new_membership_level):
        if new_membership_level in MembershipLevel.__members__.values():
            self._membership_level = new_membership_level
        else:
            raise InvalidMembershipError("INVALID_LEVEL")
    
    def get_fee(self):    
        
        if self.membership_level not in MembershipLevel.__members__.values():
             
            raise InvalidMembershipError("INVALID_LEVEL")
        return self.membership_level.value