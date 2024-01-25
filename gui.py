from tkinter import *
import tkinter as tk

window=tk.Tk()
window.geometry("500x500") #window size
window.title("Tkinter") #Title of the window

label=Label(window,text="Sample Label",width=10,height=3) #LABEL
label.pack()
button=Button(window,text="Submit",width=10,height=3,bg='blue') #BUTTON
button.pack()

#.pack is layout manager

window.mainloop() #Enables the window to be visible