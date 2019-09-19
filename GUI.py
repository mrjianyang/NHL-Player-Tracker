from tkinter import *
import functions as fn
import pandas as pd

class db:
    def __init__(self, root, data, query_list):
        self.root = root
        self.root.title("NHL Player Database")
        self.root.geometry("1350x750+0+0")
        frame = Frame(root)
        frame.grid(row=2)

        #=========================================Frames===============================================

        mainframe = Frame(self.root)
        mainframe.grid()

        'Create Display Frame for toolbar'
        toolbarframe = Frame(mainframe, width=1350, padx=2, bd=2, relief=RIDGE)
        toolbarframe.pack(side=TOP)

        'Create Display Frame for Query'
        QueryFrame = Frame(mainframe, bd=2, width=1348, height=600, padx=20, relief=RIDGE)
        QueryFrame.pack(side=BOTTOM)

        #=========================================Widgets===============================================

        'Display query'
        self.queryText = Text(QueryFrame, font=('arial', 8), width=215, height=48, padx=2, pady=2)
        self.queryText.grid(row=0,column=0)
        self.queryText.insert(END, data)


        'vertical scroll bar'
        scrollbar = Scrollbar(QueryFrame)
        scrollbar.grid(row=0, column=1, sticky='ns')
        scrollbar.config(command=self.queryText.yview)

        'horizontal scroll bar'
        scrollbarx = Scrollbar(QueryFrame, orient='horizontal')
        scrollbarx.grid(row=1,column=0, sticky='ew')
        scrollbarx.config(command=self.queryText.xview)

        
        #=========================================Functions===============================================
        def reset_data():
            fn.read_data()
            self.queryText.delete('1.0', END)
            self.queryText.insert(END, data)
        
        def searchGet(search, data):
            name = search.get().title().split()
            fn.select_player(data, name[0], name[1])

        def select_player(data, fname, lname):
            try:
                data = data[ (data["firstName"] == fname) & (data["lastName"] == lname) ].reset_index()
                self.queryText.delete('1.0', END)
                self.queryText.insert(END, data)
            except:
                self.queryText.delete('1.0', END)
                self.queryText.insert(END, "Unable to Perform Query. Try Capitalizing Names")

        def select_season(data, season):
            try:
                curr_season = season
                if season != "ALL":
                    data = (data[(data["season"] == season)])
                    self.queryText.delete('1.0', END)
                    self.queryText.insert(END, data)
                else:
                    data = (data)
            except:
                self.queryText.insert(END, "Unable to Perform Query")

        def sort_DF(data, column):
            try:
                data = data.sort_values(by=[column, "date_time"])
                self.queryText.delete('1.0', END)
                self.queryText.insert(END, data)
            except:
                self.queryText.delete('1.0', END)
                self.queryText.insert(END, "Unable to Perform Query")

        def help():
            self.queryText.delete('1.0', END)
            self.queryText.insert(END, "Refer to Github READme")

        #=========================================Buttons===============================================

        self.btnSearchQuery=Button(toolbarframe, text='Reset', width=10, font=('arial', 10, 'bold'), bd=2,
                                    command=reset_data)
        self.btnSearchQuery.grid(row=0, column=0)

        self.btnSearchQuery=Button(toolbarframe, text='Position', width=10, font=('arial', 10, 'bold'), bd=2,
                                    command= lambda: sort_DF(data, "position"))
        self.btnSearchQuery.grid(row=0, column=1)

        self.btnSearchQuery = Menubutton(toolbarframe, text='Season', width=10, font=('arial', 10, 'bold'), bd=2, relief=RAISED)
        self.btnSearchQuery.menu = Menu(self.btnSearchQuery)
        self.btnSearchQuery["menu"] = self.btnSearchQuery.menu
        self.btnSearchQuery.menu.add_command(label="2018-2019", command= lambda: select_season(data, "20182019"))
        self.btnSearchQuery.menu.add_command(label="2017-2018", command= lambda: select_season(data, "20172018"))
        self.btnSearchQuery.menu.add_command(label="2016-2017", command= lambda: select_season(data, "20162017"))
        self.btnSearchQuery.menu.add_command(label="2015-2016", command= lambda: select_season(data, "20152016"))
        self.btnSearchQuery.menu.add_command(label="2014-2015", command= lambda: select_season(data, "20142015"))
        self.btnSearchQuery.menu.add_command(label="2013-2014", command= lambda: select_season(data, "20132014"))
        self.btnSearchQuery.menu.add_command(label="2012-2013", command= lambda: select_season(data, "20122013"))
        self.btnSearchQuery.menu.add_command(label="2011-2012", command= lambda: select_season(data, "20112012"))
        self.btnSearchQuery.menu.add_command(label="2010-2011", command= lambda: select_season(data, "20102011"))
        # self.btnSearchQuery.menu.add_command(label="ALL",       command= lambda: fn.select_season(data, "ALL"))
        self.btnSearchQuery.grid(row=0, column=2)

        self.btnSearchQuery=Button(toolbarframe, text='Points', width=10, font=('arial', 10, 'bold'), bd=2,
                                    command= lambda: sort_DF(data, "pts"))
        self.btnSearchQuery.grid(row=0, column=3)

        self.btnSearchQuery=Button(toolbarframe, text='TOI', width=10, font=('arial', 10, 'bold'), bd=2)
        self.btnSearchQuery.grid(row=0, column=4)

        self.btnSearchQuery=Button(toolbarframe, text='Shots', width=10, font=('arial', 10, 'bold'), bd=2,
                                    command= lambda: sort_DF(data, "s"))
        self.btnSearchQuery.grid(row=0, column=5)

        self.btnSearchQuery=Button(toolbarframe, text='Venue', width=10, font=('arial', 10, 'bold'), bd=2)
        self.btnSearchQuery.grid(row=0, column=6)

        self.btnSearchQuery=Button(toolbarframe, text='Home', width=10, font=('arial', 10, 'bold'), bd=2)
        self.btnSearchQuery.grid(row=0, column=7)

        self.btnSearchQuery=Button(toolbarframe, text='Away', width=10, font=('arial', 10, 'bold'), bd=2)
        self.btnSearchQuery.grid(row=0, column=8)

        self.btnSearchQuery=Button(toolbarframe, text='Report', width=10, font=('arial', 10, 'bold'), bd=2)
        self.btnSearchQuery.grid(row=0, column=9)
        
        self.search = Entry(toolbarframe, width=30, bd=2, relief=RAISED)
        self.search.grid(row=0, column=10)
        self.search_btn = Button(toolbarframe, text="Search", width=10, 
                            font=('arial', 10, 'bold'), bd=2, 
                            command=lambda: searchGet(self.search, data))
        self.search_btn.grid(row=0, column=11)

        self.btnSearchQuery=Button(toolbarframe, text='Help', width=10, font=('arial', 10, 'bold'), bd=2)
        self.btnSearchQuery.grid(row=0, column=12)

        
        

        

        # # b4 = Button(frame, text="Sort Month", command= lambda: fn.sort_month_most_points(data))
        # # b4.grid(row=0, column=1)

        # # b4 = Button(frame, text="Go", command= lambda: fn.sort_month_most_points(data))
        # # b4.grid(row=0, column=1)

        # # b5 = Button(frame, text="Clear", command= lambda: fn.sort_month_most_points(data))
        # # b5.grid(row=0, column=2)

        # # b6 = Button(frame, text="Sort Venue", command= lambda: fn.sort_DF(query_list, 6, data, "venue"))
        # # b6.grid(row=0, column=3)

        # b7 = Button(frame, text="Sort Points", command= lambda: fn.query_append(query_list, 5, data, "points"))
        # b7.grid(row=0, column=4)

        # # b6 = Button(frame, text="Home vs Away Split", command= lambda: fn.sort_DF(data, "points"))
        # # b6.grid(row=0, column=5)

        # b8 = Menubutton(frame, text="Home vs Away", bd=2)
        # b8.menu = Menu(b8)
        # b8["menu"] = b8.menu
        # b8.menu.add_command(label="Home", command= lambda: fn.query_append(query_list, 6, data, "Home"))
        # b8.menu.add_command(label="Away", command= lambda: fn.query_append(query_list, 6, data, "Away"))
        # b8.menu.add_command(label="By Venue", command= lambda: fn.query_append(query_list, 6, data, "venue"))
        # b8.grid(row=0, column=5)

        # search = Entry(frame)
        # search.grid(row=0, column=6)
        # search_btn = Button(frame, text="Add Player", command=lambda: fn.query_append(query_list, 2, search, data))
        # search_btn.grid(row=0, column=7)

        # b9 = Button(frame, text="Show Report", command= lambda: fn.create_report(frame, data))
        # b9.grid(row=0, column=8)

        # # b2 = Button(frame, text="Clear Players", command= lambda: fn.create_report(frame, data))
        # # b2.grid(row=0, column=9)

        # b10 = Button(frame, text="Execute", command= lambda: fn.Execute_queries(query_list))
        # b10.grid(row=0, column=10)


