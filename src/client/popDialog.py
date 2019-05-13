# Johns Hopkins University - Whiting School of Engineering
# Engineering for Professionals
# Spring 2019 - Foundations of Software Engineering
# TJ^3 Project Group
#
# Coding with Atom (=
#

import tkinter as tk

class popDialog:

    def popDialog(suspects, weapons, rooms):

        popupDialog = tk.Tk()
        popupDialog.geometry("300x200")
        popupDialog.title("What's Your Thoughts?")

        tk.Label(popupDialog, text="Murder Mystery:").grid(row=0)

        varSuspect = tk.StringVar()
        varWeapon = tk.StringVar()
        varRoom = tk.StringVar()

        tk.Label(popupDialog, text="Suspects: ").grid(row=1, column=0)
        # Suspect Options
        selectSuspect = tk.OptionMenu(popupDialog, varSuspect, *suspects)
        selectSuspect.configure(font=("Arial", 15))
        selectSuspect.grid(row=1, column=1)

        tk.Label(popupDialog, text="Weapons: ").grid(row=2, column=0)
        # Weapon Options
        selectWeapon = tk.OptionMenu(popupDialog, varWeapon, *weapons)
        selectWeapon.configure(font=("Arial", 15))
        selectWeapon.grid(row=2, column=1)

        tk.Label(popupDialog, text="Rooms: ").grid(row=3, column=0)
        # Room Options
        selectRoom = tk.OptionMenu(popupDialog, varRoom, *rooms)
        selectRoom.configure(font=("Arial", 15))
        selectRoom.grid(row=3, column=1)

        # Select Button
        selectBtn = tk.Button(popupDialog, text="Select") #, command=makeSelection)
        selectBtn.grid(row=4, column=1)

        tk.mainloop()
