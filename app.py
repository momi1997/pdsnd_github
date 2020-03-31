# -*- coding: utf-8 -*-
"""This file contains the code to generate the UI
"""
import dash
from layout import layout


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__)

app.layout = layout






