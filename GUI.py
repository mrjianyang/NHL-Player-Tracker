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

        def select_season(data, stype, field):
            colname = "season"
            
            if stype == 1:
                colname = "type"
            try:
                if field != "ALL":
                    data = (data[(data[colname] == field)])
                    self.queryText.delete('1.0', END)
                    self.queryText.insert(END, data)
                else:
                    reset_data()
            except:
                self.queryText.delete('1.0', END)
                self.queryText.insert(END, "Unable to Perform Query")

        def sort_DF(data, column):
            try:
                data = data.sort_values(by=[column, "date_time_GMT"])
                self.queryText.delete('1.0', END)
                self.queryText.insert(END, data)
            except:
                self.queryText.delete('1.0', END)
                self.queryText.insert(END, "Unable to Perform Query")

        def select_opponent(data, opponent):
            try:
                data = data[ (data["lastName"] == opponent) ].reset_index()
                self.queryText.delete('1.0', END)
                self.queryText.insert(END, data)
            except:
                self.queryText.delete('1.0', END)
                self.queryText.insert(END, "Unable to Perform Query")

        def select_pos(data, pos):
            try:
                data = data[ (data["position"] == pos) ].reset_index()
                self.queryText.delete('1.0', END)
                self.queryText.insert(END, data)
            except:
                self.queryText.delete('1.0', END)
                self.queryText.insert(END, "Unable to Perform Query")

        def help():
            self.queryText.delete('1.0', END)
            self.queryText.insert(END, "Refer to Github READme")

        #=========================================Player info Graphs===============================================

        # self.graphDependentvar=Button(toolbarframe, text='Dependent', width=10, font=('arial', 10, 'bold'), bd=2)
        # self.graphDependentvar.grid(row=0, column=0)

        #=========================================Player info Buttons===============================================

        self.btnSearchQuery=Button(toolbarframe, text='Reset', width=10, font=('arial', 10, 'bold'), bd=2,
                                    command=reset_data)
        self.btnSearchQuery.grid(row=1, column=0)

        self.btnSearchQuery = Menubutton(toolbarframe, text='Position', width=10, font=('arial', 10, 'bold'), bd=2, relief=RAISED)
        self.btnSearchQuery.menu = Menu(self.btnSearchQuery)
        self.btnSearchQuery["menu"] = self.btnSearchQuery.menu
        self.btnSearchQuery.menu.add_command(label="LW", command= lambda: select_pos(data, "LW"))
        self.btnSearchQuery.menu.add_command(label="C", command= lambda: select_pos(data, "C"))
        self.btnSearchQuery.menu.add_command(label="RW", command= lambda: select_pos(data, "RW"))
        self.btnSearchQuery.menu.add_command(label="D", command= lambda: select_pos(data, "D"))
        self.btnSearchQuery.menu.add_command(label="G", command= lambda: select_pos(data, "G"))
        self.btnSearchQuery.grid(row=1, column=1)

        self.btnSearchQuery = Menubutton(toolbarframe, text='Season', width=10, font=('arial', 10, 'bold'), bd=2, relief=RAISED)
        self.btnSearchQuery.menu = Menu(self.btnSearchQuery)
        self.btnSearchQuery["menu"] = self.btnSearchQuery.menu
        self.btnSearchQuery.menu.add_command(label="2018-2019", command= lambda: select_season(data,0, "20182019"))
        self.btnSearchQuery.menu.add_command(label="2017-2018", command= lambda: select_season(data,0, "20172018"))
        self.btnSearchQuery.menu.add_command(label="2016-2017", command= lambda: select_season(data,0, "20162017"))
        self.btnSearchQuery.menu.add_command(label="2015-2016", command= lambda: select_season(data,0, "20152016"))
        self.btnSearchQuery.menu.add_command(label="2014-2015", command= lambda: select_season(data,0, "20142015"))
        self.btnSearchQuery.menu.add_command(label="2013-2014", command= lambda: select_season(data,0, "20132014"))
        self.btnSearchQuery.menu.add_command(label="2012-2013", command= lambda: select_season(data,0, "20122013"))
        self.btnSearchQuery.menu.add_command(label="2011-2012", command= lambda: select_season(data,0, "20112012"))
        self.btnSearchQuery.menu.add_command(label="2010-2011", command= lambda: select_season(data,0, "20102011"))
        self.btnSearchQuery.menu.add_command(label="ALL",       command= lambda: select_season(data,0, "ALL"))
        self.btnSearchQuery.grid(row=1, column=2)

        self.btnSearchQuery = Menubutton(toolbarframe, text='Season Type', width=11, font=('arial', 10, 'bold'), bd=2, relief=RAISED)
        self.btnSearchQuery.menu = Menu(self.btnSearchQuery)
        self.btnSearchQuery["menu"] = self.btnSearchQuery.menu
        self.btnSearchQuery.menu.add_command(label="Regular", command= lambda: select_season(data,1, "R"))
        self.btnSearchQuery.menu.add_command(label="Playoffs", command= lambda: select_season(data,1, "P"))
        self.btnSearchQuery.menu.add_command(label="ALL",       command= lambda: select_season(data,1, "ALL"))        
        self.btnSearchQuery.grid(row=1, column=3)

        self.btnSearchQuery=Button(toolbarframe, text='Points', width=10, font=('arial', 10, 'bold'), bd=2,
                                    command= lambda: sort_DF(data, "pts"))
        self.btnSearchQuery.grid(row=1, column=4)

        self.btnSearchQuery=Button(toolbarframe, text='TOI', width=10, font=('arial', 10, 'bold'), bd=2,
                                        command= lambda: sort_DF(data, "toi"))
        self.btnSearchQuery.grid(row=1, column=5)

        self.btnSearchQuery=Button(toolbarframe, text='Shots', width=10, font=('arial', 10, 'bold'), bd=2,
                                    command= lambda: sort_DF(data, "s"))
        self.btnSearchQuery.grid(row=1, column=6)

        self.btnSearchQuery=Button(toolbarframe, text='Venue', width=10, font=('arial', 10, 'bold'), bd=2,
                                    command= lambda: sort_DF(data, "venue"))
        self.btnSearchQuery.grid(row=1, column=7)

        self.btnVenueQuery = Menubutton(toolbarframe, text='Split', width=10, font=('arial', 10, 'bold'), bd=2, relief=RAISED)
        self.btnVenueQuery.menu = Menu(self.btnVenueQuery)
        self.btnVenueQuery["menu"] = self.btnVenueQuery.menu
        self.btnVenueQuery.menu.add_command(label="Home", command= lambda: select_season(data, "ALL"))
        self.btnVenueQuery.menu.add_command(label="Away", command= lambda: select_season(data, "ALL"))        
        self.btnVenueQuery.grid(row=1, column=8)

        self.btnOpponentQuery = Menubutton(toolbarframe, text='Opponent', width=10, font=('arial', 10, 'bold'), bd=2, relief=RAISED)
        self.btnOpponentQuery.menu = Menu(self.btnOpponentQuery)
        self.btnOpponentQuery["menu"] = self.btnOpponentQuery.menu
        self.btnOpponentQuery.menu.add_command(label="Ducks", command= lambda: select_opponent(data, "Ducks"))
        self.btnOpponentQuery.menu.add_command(label="Coyotes", command= lambda: select_opponent(data, "Coyotes"))        
        self.btnOpponentQuery.menu.add_command(label="Bruins", command= lambda: select_opponent(data, "Bruins"))        
        self.btnOpponentQuery.menu.add_command(label="Sabres", command= lambda: select_opponent(data, "Sabres"))        
        self.btnOpponentQuery.menu.add_command(label="Flames", command= lambda: select_opponent(data, "Flames"))        
        self.btnOpponentQuery.menu.add_command(label="Hurricanes", command= lambda: select_opponent(data, "Hurricanes"))        
        self.btnOpponentQuery.menu.add_command(label="Blackhawks", command= lambda: select_opponent(data, "Blackhawks"))        
        self.btnOpponentQuery.menu.add_command(label="Avalanche", command= lambda: select_opponent(data, "Avalanche"))        
        self.btnOpponentQuery.menu.add_command(label="Blue Jackets", command= lambda: select_opponent(data, "Blue Jackets"))        
        self.btnOpponentQuery.menu.add_command(label="Stars", command= lambda: select_opponent(data, "Stars"))        
        self.btnOpponentQuery.menu.add_command(label="Red Wings", command= lambda: select_opponent(data, "Red Wings"))        
        self.btnOpponentQuery.menu.add_command(label="Oilers", command= lambda: select_opponent(data, "Oilers"))        
        self.btnOpponentQuery.menu.add_command(label="Panthers", command= lambda: select_opponent(data, "Panthers"))        
        self.btnOpponentQuery.menu.add_command(label="Kings", command= lambda: select_opponent(data, "Kings"))        
        self.btnOpponentQuery.menu.add_command(label="Wild", command= lambda: select_opponent(data, "Wild"))        
        self.btnOpponentQuery.menu.add_command(label="Canadiens", command= lambda: select_opponent(data, "Canadiens"))        
        self.btnOpponentQuery.menu.add_command(label="Predators", command= lambda: select_opponent(data, "Predators"))        
        self.btnOpponentQuery.menu.add_command(label="Devils", command= lambda: select_opponent(data, "Devils"))        
        self.btnOpponentQuery.menu.add_command(label="Islanders", command= lambda: select_opponent(data, "Islanders"))        
        self.btnOpponentQuery.menu.add_command(label="Rangers", command= lambda: select_opponent(data, "Rangers"))        
        self.btnOpponentQuery.menu.add_command(label="Senators", command= lambda: select_opponent(data, "Senators"))        
        self.btnOpponentQuery.menu.add_command(label="Flyers", command= lambda: select_opponent(data, "Flyers"))        
        self.btnOpponentQuery.menu.add_command(label="Penguins", command= lambda: select_opponent(data, "Penguins"))        
        self.btnOpponentQuery.menu.add_command(label="Sharks", command= lambda: select_opponent(data, "Sharks"))        
        self.btnOpponentQuery.menu.add_command(label="Blues", command= lambda: select_opponent(data, "Blues"))        
        self.btnOpponentQuery.menu.add_command(label="Lightning", command= lambda: select_opponent(data, "Lightning"))        
        self.btnOpponentQuery.menu.add_command(label="Maple Leafs", command= lambda: select_opponent(data, "Maple Leafs"))        
        self.btnOpponentQuery.menu.add_command(label="Canucks", command= lambda: select_opponent(data, "Canucks"))        
        self.btnOpponentQuery.menu.add_command(label="Golden Knights", command= lambda: select_opponent(data, "Golden Knights"))        
        self.btnOpponentQuery.menu.add_command(label="Capitals", command= lambda: select_opponent(data, "Capitals"))        
        self.btnOpponentQuery.menu.add_command(label="Jets", command= lambda: select_opponent(data, "Jets"))               
        self.btnOpponentQuery.grid(row=1, column=9)

        self.btnSearchQuery=Button(toolbarframe, text='Report', width=10, font=('arial', 10, 'bold'), bd=2)
        self.btnSearchQuery.grid(row=1, column=10)
        
        self.search = Entry(toolbarframe, width=30, bd=2, relief=RAISED)
        self.search.grid(row=1, column=11)
        self.search_btn = Button(toolbarframe, text="Search", width=10, 
                            font=('arial', 9, 'bold'), bd=2, 
                            command=lambda: searchGet(self.search, data))
        self.search_btn.grid(row=1, column=12)

        self.btnSearchQuery=Button(toolbarframe, text='Help', width=10, font=('arial', 10, 'bold'), bd=2,
                                    command=help)
        self.btnSearchQuery.grid(row=1, column=13)


       
