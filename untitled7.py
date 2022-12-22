# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 19:51:59 2022

@author: pulle
"""

from tkinter import*

root = Tk()
root.geometry("900x600")
root.title("Project 170")
root.configure(bg="lavender")

class History_in_space():
    def year_2008(self):
        print("\n", "Grade 3", "\n")
        print("\n", "45.0", "\n")
        
        
class History_in_medical():
    def year_2008(self):
        print("\n", "Grade 5", "\n")
        print("\n", "60.0", "\n")
        
class History_in_sports():
    def year_2008(self):
        print("\n", "Grade 10", "\n")
        print("\n", "62.5", "\n")
        
space = History_in_space()
space.year_2008()

medical = History_in_medical()
medical.year_2008()

sports = History_in_sports()
sports.year_2008()


root.mainloop()