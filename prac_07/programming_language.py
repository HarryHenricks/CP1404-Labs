

class ProgrammingLanguage():


    def __init__(self, name="", typing="", reflection="", year=""):


        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):


        if self.typing == "Dynamic":
            print("True")
            return True
        elif self.typing == "Static":
            print("False")
            return False
        else:
            print("Error in typing argument")

    def __str__(self):
        return print("{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection, self.year))

