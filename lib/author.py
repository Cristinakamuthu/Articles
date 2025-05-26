class Author:
    def __init__(self,name,id=None):
        self.id = id 
        self.name = name

    def __repr__(self):
        return f"<Author {self.id}: {self.name}>"
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if isinstance(name,str):
            self.name = name
        else:
            raise TypeError("Name must be a string")
    
    def save(self):
        sql = """INSERT INTO authors(name)
                VALUE(?)
                """
        
