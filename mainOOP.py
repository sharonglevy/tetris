# Object oriented programming in python

# Class creation
class dog:
    # this argument will be called and will be passes
    # any arguments that we put in d = dog()
    # for ex if we want to put a name to the dog we'll do the following
    def __init__(self, name):
        self.name = name
    # will start defining what dog can do
    # all methods will start with self
    def bark(self, name):
        print("bark" + name)

    def meow(self):
        return False

# creating a new instance of type dog
# and we can create as many instances as we want
d = dog("tim")
# Bark is a METHOD if I want to call that method on my instance of the class

