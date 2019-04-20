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
# Candlestick
# Knife
# Lead Pipe
# Revolver
# Rope
# Wrench
#
# Will need revision

class weapons:

    WEAPON_CANDLESTICK = "Candlestick"
    WEAPON_KNIFE = "Knife"
    WEAPON_LEAD_PIPE = "Lead Pipe"
    WEAPON_REVOLVER = "Revolver"
    WEAPON_ROPE = "Rope"
    WEAPON_WRENCH = "Wrench"

    def _init_(self, name):
        self.name = name
        self.location = location
