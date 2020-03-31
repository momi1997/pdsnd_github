from app import app
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from dash.dash import no_update
from io import StringIO
import pandas as pd
import utils


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



def generate_table_header(df):
    """
    Generate table header from the provided Dataframe

    Args:
        (pandas.DataFrame) df - dataframe that we want to operate on
    
    Returns:
        (list) - a list of dash html table headers
    """
    return [html.Tr([html.Th(col) for col in df.columns])]

def generate_table_rows(df, limit):
    """
    Generates the desired number of rows from the provided dataframe

    Args:
        (pandas.DataFrame) df - dataframe that we want to operate on
    
    Returns:
        (list) - a list for dash html table rows
    """
    return (
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
     State("old-raw-data-version","children"),
     State("table","children")]
)
def view_more(n_clicks, new_raw_data_version, dataframe_csv, rows_num,
             old_raw_data_version, table_content):
    """
    Generates an html table each time the "View More" button is clicked

    Args:
        (int or None) n_clicks - how many times the "View More" button was clicked
                                If None, it means that the button has never been
                                clicked and that it's being initialized.
        (str) new_raw_data_version - a string representing the new version number of
                                    dataframe_csv.
                                    This number gets updated each time load_data() gets called.
        (str) dataframe_csv - a string representation of a pandas Dataframe
        (str) rows_num - the number of rows to skip when creating a new table rows
        (str) old_raw_data_version - a string representing the old version number of
                                    dataframe_csv
                                    This number gets updated when view_more()
                                    is called directly after load_data()
        (list) table_content - a list of html table rows that were generated by
                                a previous call to this function.

    Note: The previous arguments are provided to the function by the Dash framework
    using the decorator at the top of the function.
    
    Returns:
        (tuple) a tuple containing:
            (list) - a list of html table rows
            (str) - the number of rows to skip for the next call
            (str or dash.dash._NoUpdate) - If it's a string, it's the new value for 
                                            the hidden div that contains the old version
                                            number of dataframe_csv.
                                            If it's a _NoUpdate object then the hidden
                                            div is not updated.
    
    Note: The return value is fed to the Dash framework that will update
    the UI.
    """
    # -> If n_clicks is none it means either that the callback is being
    # initialized or that the button hasn't been clicked yet.
    # -> If the callback is being initialized, we want to prevent the update of
    # the callback but if new_raw_data_version is more than 0, it means that
    # data is loaded and that we need to draw the table
    if n_clicks is None and int(new_raw_data_version) == 0:
        
        raise PreventUpdate

    if int(new_raw_data_version) > int(old_raw_data_version):
       
        # if new_raw_data_version > old_raw_data_version
        # it means that there is new loaded data to draw
        # we draw the first five rows of the table
        df = pd.read_csv(StringIO(dataframe_csv), nrows=5)

        return (generate_table_header(df) + generate_table_rows(df, 5), # returns the table html with only 5 rows
                str(5), # we skip 5 lines in the csv string in the next call
                new_raw_data_version) # updates old-raw-data-version div

    else:
        print("else is executed")
        rows_num = int(rows_num)
        # we skip the lines that we have already drawn and
        # we read five more lines
        df = pd.read_csv(StringIO(dataframe_csv), nrows=5,
                        skiprows=rows_num)
        return (table_content + generate_table_rows(df, rows_num), # appends the new rows to the previous table
                str(rows_num + 5), # updates the number of rows to skip
                                   # For each click, the number of rows to skip is
                                   # increased by five
                no_update) # keeps the same value for old-raw-data-version div