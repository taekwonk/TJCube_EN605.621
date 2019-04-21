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
# Ballroom
# Billiard room
# Conservatory
# Dining room
# Hall
# Kitchen
# Library
# Lounge
# Study
#
# Will need revision

class rooms:

    ROOM_BALLROOM = "Ballroom"
    ROOM_BILLIARD_ROOM = "Billiard Room"
    ROOM_CONSERVATORY = "Conservatory"
    ROOM_DINING_ROOM = "Dining Room"
    ROOM_HALL = "Hall"
    ROOM_KITCHEN = "Kitchen"
    ROOM_LIBRARY = "Library"
    ROOM_LOUNGE = "Lounge"
    ROOM_STUDY = "Study"

    def _init_(self, name):
        self.name = name
        self.location = location
        self.secretPassage = secretPassage
