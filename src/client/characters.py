# Johns Hopkins University - Whiting School of Engineering
# Engineering for Professionals
# Spring 2019 - Foundations of Software Engineering
# TJ^3 Project Group
#
# This page was last modified (4.19.2019) by Jenna S. Nuth
# Coding with Atom (=
#
# References:
# https://youtu.be/ajR4BZBKTr4
# https://inventwithpython.com/makinggames.pdf
# https://www.raywenderlich.com/2614-multiplayer-game-programming-for-teens-with-python-part-1
#
# Reverend Green
# Colonel Mustard
# Mrs. Peacock
# Professor Plum
# Miss Scarlet
# Mrs. White
#
# Will need revision

class characters:

    CHARACTER_REVEREND_GREEN = "Reverend Green"
    CHARACTER_COLONEL_MUSTARD = "Colonel Mustard"
    CHARACTER_MRS_PEACOCK = "Mrs. Peacock"
    CHARACTER_PROFESSOR_PLUM = "Professor Plum"
    CHARACTER_MISS_SCARLET = "Miss Scarelet"
    CHARACTER_MRS_WHITE = "Mrs. White"

    def _init_(self, name):
        self.name = name
        self.gender = gender
        self.color = color
        self.location = location

class characterGreen(characters):
    def getInfo(self):
        self.name = CHARACTER_REVEREND_GREEN
        print(self.CHARACTER_REVEREND_GREEN)

class characterMustard(characters):
    def getInfo(self):
        print(self.CHARACTER_COLONEL_MUSTARD)

class characterPeacock(characters):
    def getInfo(self):
        print(self.CHARACTER_MRS_PEACOCK)

class characterPlum(characters):
    def getInfo(self):
        print(self.CHARACTER_PROFESSOR_PLUM)

class characterScarlet(characters):
    def getInfo(self):
        print(self.CHARACTER_MISS_SCARLET)

class characterWhite(characters):
    def getInfo(self):
        print(self.CHARACTER_MRS_WHITE)
