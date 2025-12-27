import argparse
import tkinter as tk

#create and read parsers

parser = argparse.ArgumentParser() #create parser 
parser.add_argument("target",help="Type the target IP adress, USAGE : python3 pytarget.py <TARGET>") #Ip argument
args = parser.parse_args() #read user argument

#tkinter

root = tk.Tk() #create window, (root=window)
root.title("pytarget") #window title
root.geometry("300x50") #window size

root.mainloop()

