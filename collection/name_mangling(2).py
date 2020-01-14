class Person:
    info_form =   """name : %s
age : %s
"""

    def __init__(self, name):
        self.n = name
    def p_name(self):
        return self.__name()
    def __name(self):
        return self.n
    def person_info(self):
        print(self.info_form%(self.__name(), 40))
    

class empoloy(Person):
    def __init__(self, name, part):
        super().__init__(name)
        self.part = part

    def p_name(self):
        return self.__name()
    def __name(self):
        return self.part+":"+self.n
