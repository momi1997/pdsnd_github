# -*- coding: utf-8 -*-
"""This file contains the code to generate the UI
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from dash.dash import no_update
from io import StringIO
import pandas as pd
import utils

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__)

app.layout = html.Div(className="overall-style",children=[
    ########### FILTERING PART ############
    html.Div(id="filtering-div", className="card",
    children=[
        html.Div(className="container",children=[
            html.Div(children="choose your filters:",
            className="title"),
            html.Div(id="country-div", children=[
                html.Span(children="Would you like to see data for : ",
                className="questions"),
                #The user selects the city from these radio items
                dcc.RadioItems(
                    id="city-radio",
                    options=[
                        {"label" : "Chicago", "value" : "CHI"},
                        {"label" : "New York City", "value" : "NYC"},
                        {"label" : "Washington", "value" : "WA"}
                    ],
                    value="CHI",
                    className = "radio"                                
                )
            ],
            className="question-div"),
            html.Div(id="month-div", className="question-div",
            children=[
                html.Span(className="questions",
                children="Would you like to filter the data by month : "),
                #The user selects the month from these radio items
                dcc.RadioItems(
                    id="month-radio",
                    options=[
                        {"label" : "January", "value" : "1"},
                        {"label" : "February", "value" : "2"},
                        {"label" : "March", "value" : "3"},
                        {"label" : "April", "value" : "4"},
                        {"label" : "May", "value" : "5"},
                        {"label" : "June", "value" : "6"},
                        {"label" : "All Months", "value" : "all"}
                    ],
                    value="all",
                    className = "radio"
                )
            ]),
            html.Div(id="day-div", className="question-div",
            children=[
                html.Span(className="questions",
                children="Would you like to filter the data by day : "),
                #The user selects the day from these radio items
                dcc.RadioItems(
                    id="day-radio",
                    options=[
                        {"label" : "Saturday", "value" : "Saturday"},
                        {"label" : "Sunday", "value" : "Sunday"},                    
                        {"label" : "Monday", "value" : "Monday"},
                        {"label" : "Tuesday", "value" : "Tuesday"},
                        {"label" : "Wednesday", "value" : "Wednesday"},
                        {"label" : "Thursday", "value" : "Thursday"},
                        {"label" : "Friday", "value" : "Friday"},
                        {"label" : "All Days", "value" : "all"}
                    ],
                    value="all",
                    className = "radio"
                )
            ]),            
            #loads th data when clicked
            html.Button("Load Data", id="load-data-button",
            className="button center-horizontal"),
            dcc.Loading(type="circle", children=[
                html.Div(id="loading-div", style={"display":"none"})
            ])

                           
        ])
                
    ]),
    ################# STATS PART ###################
    #______________TIME STATS_______________________
    html.Div(className="stat-div", children=[
        dcc.Loading(type="circle", children=[
            html.Div(className="stat-card", children=[
                html.Div(className="stat-card-container", children=[
                    html.Div(className="stat-title",
                    children=[
                        "time stats:"
                    ]),
                    #Most common month
                    html.Div(className="stat-div",
                    children=[
                        #The question about the data
                        html.Div(className="stat-question",                        
                        children=["Most common month is: "]),
                        # The answer to that question
                        html.Div(id="most-common-month"
                        ,className="stat-answer")
                    ]),
                    #Most common day of week
                    html.Div(className="stat-div",
                    children=[
                        #The question about the data
                        html.Div(className="stat-question",                        
                        children=["Most common day of week: "]),
                        # The answer to that question
                        html.Div(id="most-common-dow",
                        className="stat-answer")
                    ]),
                    #Most common hour of day
                    html.Div(className="stat-div",
                    children=[
                        #The question about the data
                        html.Div(className="stat-question",                        
                        children=["Most common hour of day: "]),
                        # The answer to that question
                        html.Div(id="most-common-hod",
                        className="stat-answer")
                    ])                                         
                ])
            ])            
        ])

    ]),
    #________________STATION STAT___________________
    html.Div(className="stat-div", children=[
        dcc.Loading(type="circle", children=[
            html.Div(className="stat-card", children=[
                html.Div(className="stat-card-container", children=[
                    html.Div(className="stat-title",
                    children=[
                        "station stats:"
                    ]),
                    #Most common month
                    html.Div(className="stat-div",
                    children=[
                        #The question about the data
                        html.Div(className="stat-question",                        
                        children=["Most commonly used start station is: "]),
                        # The answer to that question
                        html.Div(id="most-common-start-station"
                        ,className="stat-answer")
                    ]),
                    #Most common day of week
                    html.Div(className="stat-div",
                    children=[
                        #The question about the data
                        html.Div(className="stat-question",                        
                        children=["Most commonly used end station is: "]),
                        # The answer to that question
                        html.Div(id="most-common-end-station",
                        className="stat-answer")
                    ]),
                    #Most common hour of day
                    html.Div(className="stat-div",
                    children=[
                        #The question about the data
                        html.Div(className="stat-question",                        
                        children=["Most common trip from start to end is: "]),
                        # The answer to that question
                        html.Div(id="most-common-trip",
                        className="stat-answer")
                    ])                                         
                ])
            ])            
        ])

    ]),
    #___________________TRIP STATS_________________
    html.Div(className="stat-div", children=[
        dcc.Loading(type="circle", children=[
            html.Div(className="stat-card", children=[
                html.Div(className="stat-card-container", children=[
                    html.Div(className="stat-title",
                    children=[
                        "trip duration stats:"
                    ]),
                    # Total travel time
                    html.Div(className="stat-div",
                    children=[
                        #The question about the data
                        html.Div(className="stat-question",                        
                        children=["Total travel time is: "]),
                        # The answer to that question
                        html.Div(id="total-travel-time"
                        ,className="stat-answer")
                    ]),
                    # Mean travel time
                    html.Div(className="stat-div",
                    children=[
                        #The question about the data
                        html.Div(className="stat-question",                        
                        children=["Mean travel time is: "]),
                        # The answer to that question
                        html.Div(id="mean-travel-time",
                        className="stat-answer")
                    ]),                                         
                ])
            ])            
        ])

    ]),
    #____________________USER STATS______________________
    html.Div(className="stat-div", children=[
        dcc.Loading(type="circle", children=[
            html.Div(className="stat-card", children=[
                html.Div(className="stat-card-container", children=[
                    html.Div(className="stat-title",
                    children=[
                        "user stats:"
                    ]),
                    # User types count
                    html.Div(className="stat-div",
                    children=[
                        #The question about the data
                        html.Div(className="stat-question",                        
                        children=["User types count is: "]),
                        # The answer to that question
                        html.Div(id="user-types-count"
                        ,className="stat-answer")
                    ]),
                    #Gender types count 
                    html.Div(className="stat-div",
                    children=[
                        #The question about the data
                        html.Div(className="stat-question",                        
                        children=["Gender count is: "]),
                        # The answer to that question
                        html.Div(id="gender-count",
                        className="stat-answer")
                    ]),
                    # Earliest year of birth
                    html.Div(className="stat-div",
                    children=[
                        #The question about the data
                        html.Div(className="stat-question",                        
                        children=["Earliest year of birth is: "]),
                        # The answer to that question
                        html.Div(id="earliest-year",
                        className="stat-answer")
                    ]),
                    # Most recent year of birth
                    html.Div(className="stat-div",
                    children=[
                        #The question about the data
                        html.Div(className="stat-question",                        
                        children=["Most recent year of birth: "]),
                        # The answer to that question
                        html.Div(id="most-recent-year",
                        className="stat-answer")
                    ]),
                    html.Div(className="stat-div",
                    children=[
                        #The question about the data
                        html.Div(className="stat-question",                        
                        children=["Most common year of birth: "]),
                        # The answer to that question
                        html.Div(id="most-common-year",
                        className="stat-answer")
                    ])                     
                ])
            ])            
        ])

    ]),
    ############# RAW DATA PART #####################
    html.Div(style={"width":"100%"}, children=[
        html.Div(id="raw-data-prompt-div", children=[
            "Would you like to see raw data ?"
        ]),
        html.Div(style={"width":"100%"}, children=[
            # Button that either shows the "view more" button and the table
            # or hides them
            html.Button("View Raw Data", id="view-raw-data-button",
            className="button center-horizontal")
        ])
    ]),


    html.Div(className="card", style={"overflow-x":"auto"}, children=[
        dcc.Loading(type="circle",
        children=[
            html.Div(style={"display":"none", "overflow-x":"auto"}, id="table-div", children=[
                #The html table that displays raw data
                html.Table(id="table")
            ]),                
        ]),

        # Adds five row to the table each time it's clicked
        html.Button("View more", id='view-more-button', className="button center-horizontal", 
        style={"display":"none"})
    ]),


    ################# APP STATE PART ################
    # Because the use of global variables is highly discouraged
    # in Dash documentation https://dash.plot.ly/sharing-data-between-callbacks
    # it's better to persist the state of the app in empty divs as an alternative.

    # The state of "View raw data" button
    html.Div(id="view-raw-data-state", children="view_raw_data" ,style={"display":"none"}),
    # dataframe div that will contain the csv representation of a loaded dataframe
    html.Div(id="dataframe-div", style={"display":"none"}),

    #These two divs are used to communicate with the view_raw_data function
    #This divs contains the version of the datatframe, each time load_data() is invoked
    #the content of this div gets incremented by one and notifies view_raw_data()
    #to hide the table because the old dataframe is invalid
    #The default value is 0
    html.Div(id="new-dataframe-version",children="0", style={"display":"none"}),
    #This div contains the precedent dataframe version before the new load_data()
    #click
    #The default value is 0
    html.Div(id="old-dataframe-version", children="0", style={"display":"none"}),
    # The number of rows to show in the raw data table
    # default value is 5
    html.Div(id="rows-num-div", children="5", style={"display":"none"}),

    #These two divs are used to communicate between view_raw_data() function
    # and view_more()
    # This div contains old raw data version
    html.Div(id="old-raw-data-version", children="0", style={"display":"none"}),
    #This div contains new raw data version
    html.Div(id="new-raw-data-version", children="0", style={"display":"none"}),

    #This div contains the results of time_stats() function before
    # dispatching them to their correct places
    html.Div(id="time-stats-placeholder", children="", style={"display":"none"}),

    #This div contains the results of station_stats() function before
    # dispatching them to their correct places
    html.Div(id="station-stat-placeholder", children="", style={"display":"none"}),

    #This div contains the results of trip_duration_stats() function before
    # dispatching them to their correct places
    html.Div(id="trip-duration-placeholder", children="", style={"display":"none"}),
    #This div contains the results of user_stats() function before
    # dispatching them to their correct places
    html.Div(id="user-stat-placeholder", children="", style={"display":"none"}),
    # Placeholder for implementation purposes
    html.Div(id="hidden-div"),
    html.Div(id="hidden-div1", style={"display":"none"})
])

    


@app.callback(
    [Output("dataframe-div","children"),
     Output("new-dataframe-version", "children"),
     Output("time-stats-placeholder","children"),
     Output("station-stat-placeholder","children"),
     Output("trip-duration-placeholder","children"),
     Output("user-stat-placeholder","children"),
     Output("loading-div","style")],
    [Input("load-data-button","n_clicks")],
    [State("city-radio", "value"),
     State("month-radio", "value"),
     State("day-radio","value"),
     State("old-dataframe-version", "children")]
)
def load_data(n_clicks, city, month, day, old_df_version):
    if n_clicks is None: 
        raise PreventUpdate
    #loads the data from csv file into a dataframe
    df = utils.load_data(city, month, day)
    # calculates the time stats from the dataframe
    time_stat = utils.time_stats(df)
    # calculates the station stats from the dataframe
    station_stat = utils.station_stats(df)
    # calculates the trip duration stats from the dataframe
    trip_duration_stat = utils.trip_duration_stats(df)
    # calculates the user stats from the dataframe
    user_stats = utils.user_stats(df)
    #returns a csv string that will be persisted in the dataframe-div
    #returns the new dataframe version
    return (df.to_csv(index=False),# Outputs the filtered datafram data as csv
            str(int(old_df_version) + 1), # Updates the dataframe version
            time_stat,
            station_stat,
            trip_duration_stat,
            user_stats,
            {"display":"none"})

@app.callback(
    [Output("most-common-month","children"),
     Output("most-common-dow","children"),
     Output("most-common-hod","children")],
     [Input("time-stats-placeholder","children")]
)
def display_time_stat(time_stat_str):
    if time_stat_str == "":
        raise PreventUpdate
    # Gets a tuple out of the time_stat_string
    time_stat = tuple(time_stat_str)
    return (time_stat[0], # returns most common month
            time_stat[1], # returns most common day of week
            time_stat[2]) # returns most common hour of day

@app.callback(
    [Output("most-common-start-station","children"),
     Output("most-common-end-station","children"),
     Output("most-common-trip","children")],
     [Input("station-stat-placeholder","children")]
)
def display_station_stat(station_stat_str):
    if station_stat_str == "":
        raise PreventUpdate
    # Gets a tuple out of the station_stat_string
    station_stat = tuple(station_stat_str) 
    return (station_stat[0], # returns most commonly used start station
            station_stat[1], # returns most commonly used end station
            station_stat[2]) # returns most common trip from start to end

@app.callback(
    [Output("total-travel-time","children"),
     Output("mean-travel-time","children")],
     [Input("trip-duration-placeholder","children")]
)
def display_trip_duration_stats(trip_duration_str):
    if trip_duration_str == "":
        raise PreventUpdate
    # Gets a tuple out of the trip_duration_str
    trip_duration_stat = tuple(trip_duration_str)
    return (trip_duration_stat[0], # returns total travel time
            trip_duration_stat[1]) # returns mean travel time

@app.callback(
    [Output("user-types-count","children"),
     Output("gender-count","children"),
     Output("earliest-year","children"),
     Output("most-recent-year","children"),
     Output("most-common-year","children")],
     [Input("user-stat-placeholder","children")]
)
def display_user_stat(user_stat_str):
    if user_stat_str == "":
        raise PreventUpdate
    # Gets a tuple out of the user_stat_str
    user_stat = list(user_stat_str)
    return (user_stat[0], # returns user types count
            user_stat[1], # returns gender count
            user_stat[2], # returns the earliest year of birth
            user_stat[3], # returns the most recent year of birth
            user_stat[4]) # returns the most common year of birth
            

@app.callback(
    [Output("view-raw-data-button", "children"),
     Output("view-more-button", "style"),
     Output("view-raw-data-state", "children"),
     Output("table-div","style"),
     Output("old-dataframe-version", "children"),
     Output("new-raw-data-version","children")],
    [Input("view-raw-data-button","n_clicks"),
     Input("new-dataframe-version", "children")],
    [State("view-raw-data-state","children"),
     State("old-dataframe-version", "children"),
     State("new-raw-data-version","children")]
)
def view_raw_data(n_clicks, new_df_version, view_raw_data_state,
                  old_df_version, new_raw_data_version):
    print("old df version: " + old_df_version)
    print("new df version: " + new_df_version)
    print("view_raw_data_state is: " + view_raw_data_state)
    #Stops the callback if it's the first inialization of n_clicks
    #if n_clicks is None:
    #    raise PreventUpdate
    # if n_clicks is odd it means that the raw data is displayed
    if int(new_df_version) == 0:
        #The default value means that Dash is initializing the callbacks
        #In this case there's no loaded data because load_data() hasn't been
        #called yet so we prevent the callback from running 
        raise PreventUpdate

    if int(new_df_version) > int(old_df_version):
        
        if int(new_df_version) == 1:
            
            return (no_update, # keeps the toggle button text 
                    no_update, # keeps the view more button 
                    no_update, # keeps the toggle button state
                    {"display":"inline"}, # keeps the data table hidden
                    new_df_version, # updates old-dataframe version to the new version
                    str(int(new_raw_data_version) + 1)) # updates the row data version            
        else:
            
            #If there's a new version of the data we need to hide the data table
            #and set the text of the view-raw-data-button button to "View Raw Data" because
            #the data is invalid
            #We also need to update old-dataframe-version div with the new version
            return ("view raw data", # updates the toggle button text 
                    {"display":"none"}, # hides the view more button 
                    "view_raw_data", # updates the toggle button state
                    {"display":"none"}, # hides the data table
                    new_df_version, # updates old-dataframe version to the new version
                    str(int(new_raw_data_version) + 1)) # updates the row data version

    else:
        if view_raw_data_state == "view_raw_data":
        # If old_df_version == new_df_version this means that there is no new data
        # and that the function was called with a click on the button 
        # If view_raw_data_state == view_raw_data this means that the user is
        # asking for viewing the raw data
            return ("hide raw data", # updates the toggle button text 
                    {"display":"inline"},# displays the view more button 
                    "hide_raw_data",# updates the toggle button state
                    {"display":"inline"},# displays the table 
                    no_update,# we keep the old value because there's no change to data
                    no_update) # we keep the same value for new_raw_data_version
        else:
            
            # If view_raw_data_state == hide_raw_data, it means that 
            # the user is asking for hiding the raw data 
            return ("view raw data", # updates the toggle button text 
                    {"display":"none"}, # hides the view more button 
                    "view_raw_data", # updates the toggle button state
                    {"display":"none"}, # hides the data table
                    no_update,# we keep the old value because there's no change to data
                    no_update) # we keep the same value for new_raw_data_version



def generate_table(df, limit):
    return (
        # Table header
        [html.Tr([html.Th(col) for col in df.columns])] +

        #Table body
        [html.Tr([html.Td(df.iloc[i][col]) for col in df.columns])
            # even if the user clicks more than the total number of
            # rows in the dataframe we always select the minimun between
            # the limit and the dataframe length 
            for i in range(min(len(df), limit))]
    )

@app.callback(
    [Output("table","children"),
     Output("rows-num-div","children"),
     Output("old-raw-data-version","children")],
    [Input("view-more-button", "n_clicks"),
     Input("new-raw-data-version","children")],
    [State("dataframe-div","children"),
     State("rows-num-div","children"),
     State("old-raw-data-version","children")]
)
def view_more(n_clicks, new_raw_data_version, dataframe_csv, rows_num,
             old_raw_data_version):

    # -> If n_clicks is none it means either that the callback is being
    # initialized or that the button hasn't been clicked yet
    # -> If the callback is being initialized, we want to prevent the update of
    # all the callbacks but if new_raw_data_version is more that 0 it means that
    # data is loaded and that we need to draw the data that why we also add
    # to the condition that there was update to the data.

    if n_clicks is None and int(new_raw_data_version) == 0:
        
        raise PreventUpdate

    if int(new_raw_data_version) > int(old_raw_data_version):
       
        # if new_raw_data_version > old_raw_data_version
        # it means that there is new loaded data to draw
        # so we set the number of rows back to the default 5
        # and we also draw the table with 5 rows
        
        df = pd.read_csv(StringIO(dataframe_csv), nrows=5)

        return (generate_table(df, 5), # returns the table html with only 5 rows
                str(10), # resets the number of rows to show 10 rows
                new_raw_data_version) # updates old-raw-data-version div
    # gets the number of rows to show
    else:
        print("else is executed")
        rows_num = int(rows_num)
        # gets the dataframe from the csv string
        df = pd.read_csv(StringIO(dataframe_csv), nrows=rows_num)
        return (generate_table(df, rows_num), # returns the table html
                str(rows_num + 5), # updates the number of rows to show
                                   # For each click, the number of rows is
                                   # increased by five
                no_update) # keeps the same value for old-raw-data-version div


if __name__ == '__main__':
    app.run_server(debug=True)
