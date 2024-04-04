class Pet():
    def __init__(self, name, owner):
        self.is_alive = True # It's alive!!!
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)


class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        Pet.__init__(self,name,owner)
        self.lives = lives

    def talk(self):
        """ Print out a cat's greeting.
        >>> Cat('Thomas', 'Tammy').talk()
        Thomas says meow!
        """
        print(super().talk()," says meow")


    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero, 'is_alive'
        becomes False. If this is called after lives has reached zero, print out
        that the cat has no more lives to lose.
        """
        self.lives -= 1
        if self.lives == 0:
            self.is_alive = False
            print("No more lives to lose")



# 2 Tutorial: More cats! Fill in this implemention of a class called NoisyCat, which is
# just like a normal Cat. However, NoisyCat talks a lot – twice as much as a regular
# Cat! Make sure to also fill in the repr method for NoisyCat, so we know how
# to construct it! As a hint: You can use several string formatting methods to make
# this easier.
# E.g.:
# >>> 'filling in {} spaces {} and {}'.format('blank', 'here', 'here')
# 'filling in blank spaces here and here'

class NoisyCat(Cat): # Fill me in!
    """A Cat that repeats things twice."""

    def talk(self):
        """Talks twice as much as a regular cat.
        >>> NoisyCat('Magic', 'James').talk()
        Magic says meow!
        Magic says meow!
        """
        print('{} \n {}'.format(super().talk(),super().talk()))

    def __repr__(self):
        """The interpreter-readable representation of a NoisyCat
        >>> muffin = NoisyCat('Muffin', 'Catherine')
        >>> repr(muffin)
        "NoisyCat('Muffin', 'Catherine')"
        >>> muffin
        NoisyCat('Muffin', 'Catherine')
        """
        self.talk.__repr__()
