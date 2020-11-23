from pydantic import BaseModel

class Base(BaseModel):

    def __setitem__(self, key, value):
        self.__dict__[key] = value
    
    def __getitem__(self, key):
        return self.__dict__[key]