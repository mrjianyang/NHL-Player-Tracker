import GUI as guii
from tkinter import *
import functions as fn
import pandas as pd
import sys

def main():
    root = Tk()
    root.geometry("800x100")

    data = fn.read_data()
    data = data.iloc[::-1]
    query_list = []
    b = guii.db(root, data, query_list)
    
    root.mainloop()

if __name__ == "__main__":
    #cache current season
    query_output = ""

    curr_season = "ALL"
    main()