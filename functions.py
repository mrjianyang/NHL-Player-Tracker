import pandas as pd
import sys
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import datetime

team_venue = {
    1 : ["Prudential Center"],
    2 : ["Barclays Center", "Nassau Coliseum"],
    3 : ["Madison Square Garden"],
    4 : ["Wells Fargo Center", "Wachovia Center"],
    5 : ["Consol Energy Center", "PPG Paints Arena"],
    6 : ["TD Garden"],
    7 : ["KeyBank Center", "Marine Midland Arena", "HSBC Arena", "First Niagra"],
    8 : ["Centre Bell"],
    9 : ["Canadian Tire Centre", "Scotiabank Place"],
    10 : ["Scotiabank Arena", "Air Canada Centre"],
    11 : ["Philips Arena"],
    12 : ["RBC Center", "PNC Arena"],
    13 : ["BB&T Center", "National Car Rental", "Office Depot Center", "BankAtlantic Center"],
    14 : ["St. Pete Times Forum", "Amalie Arena", "Tampa Bay Times Forum"],
    15 : ["Verizon Center"],
    16 : ["United Center"],
    17 : ["Joe Louis Arena", "Little Caesars Arena"],
    18 : ["BridgeStone Arena"],
    19 : ["Scottrade Center"],
    20 : ["Scotiabank Saddledome"],
    21 : ["Pepsi Center"],
    22 : ["Rexall Place", "Rogers Place"],
    23 : ["Rogers Arena"],
    24 : ["Honda Center"],
    25 : ["American Airlines Center"],
    26 : ["STAPLES Center"],
    27 : ["Jobing.com Arena", "Gila River Arena"],
    28 : ["SAP Center","HP Pavilion"],
    29 : ["Nationwide Arena"],
    30 : ["Xcel Energy Center"],
    52: ["MTS Centre"],
    53 : ["Jobing.com Arena", "Gila River Arena"],
    54 : ["T-Mobile Arena"]
}


pd.set_option('display.max_columns', 60)
pd.set_option('display.width', 250)
pd.set_option('display.max_rows', 1000)

def dateParse(x):
    pd.datetime.strptime(x, '%Y-%m-%d')

def read_data():
    data = pd.read_csv("output_ovie.csv", date_parser=dateParse)
    data["season"] = data["season"].astype(str)

    return data

# def query_append(query_list, query_id, param1=None, param2=None, param3=None):
#     # if (query_id not in query_list):
#     query_key={query_id: None}
#     query_vals = []
    
#     if (param1 != None):
#         query_vals.append(param1)
#     if (param2 != None):
#         query_vals.append(param2)
#     if (param3 != None):
#         query_vals.append(param3)

#         query_key[query_id]=query_vals

# def Execute_queries(query_list):
#     for key, value in query_list.items():
#         if (key == 1):
#             month_day(value)
#         elif (key==2):
#             select_player(value[0], value[1], value[2])
#         elif (key==3):
#             create_report(value[0], value[1])
#         elif (key==4):
#             select_season(value[0], value[1])
#         elif (key == 5):
#             sort_DF(value[0], value[1])
#         elif (key == 6):
#             Home_vs_Away_split(value[0], value[1])  
#     query_list.clear()

#1
def month_day(x):
    return datetime.datetime.fromtimestamp(x).strftime('%m-%d')

#2   
def select_player(data, fname, lname):
    try:
        data = data[ (data["firstName"] == fname) & (data["lastName"] == lname) ].reset_index()
    except:
        data = "Incorrect Entry"
#3
def create_report(root, data):
    f, ax = plt.subplots(figsize=(4, 6))
    sns.lineplot(x=data["date_time"], y=data["points"])

    canvas = FigureCanvasTkAgg(f, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=1, column=0)

    f, ax = plt.subplots(figsize=(4, 6))
    sns.lineplot(x=data["date_time"], y=data["goals"])

    canvas = FigureCanvasTkAgg(f, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=2, column=0)

    f, ax = plt.subplots(figsize=(4, 6))
    sns.lineplot(x=data["date_time"], y=data["assits"])

    canvas = FigureCanvasTkAgg(f, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=3, column=0)

    f, ax = plt.subplots(figsize=(4, 6))
    sns.lineplot(x=data["date_time"], y=data["shots"])

    canvas = FigureCanvasTkAgg(f, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=4, column=0)

#6
def Home_vs_Away_split(data, venue):
    team_id = data["team_id"].iloc[0]

    # if (venue == "Home"):
    #     for key, value in range(len(data[team_id])):
    #         df_home = data[data["venue"] == i]
    #         print(df_home)
    
    # elif (venue == "Away"):
    #     for i in range(len(team_venue[team_id])):
    #         df_away = data[~(data["venue"] == i)]
    #         print(df_away)

    # else:
    data = data.groupby(by="venue")
    print(data)

# def sort_month_most_points(data):
#     # tmp_data = data[ (data["season"] == curr_season ) ]
#     tmp_data = data
#     tmp_data["date_time"] = tmp_data["date_time"].apply(month_day)
#     tmp_data_grouped = tmp_data.groupby(["date_time", "points"]).sum()
#     # print (data)
#     print( tmp_data_grouped)




