import dash_core_components as dcc
import dash_html_components as html


layout = html.Div(className="overall-style",children=[
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