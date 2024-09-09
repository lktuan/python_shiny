from shiny.express import ui, render, input
from pathlib import Path
from shinywidgets import render_plotly

import pandas as pd
import plotly.express as px

file_path = Path(__file__).parent / "penguins.csv"
df = pd.read_csv(file_path)

ui.h1("My Dashboard")

ui.p("This is sometext")

ui.input_slider("mass", "Max body mass", 2000, 8000, 6000)


@render.data_frame
def data():    
    return df[df['body_mass_g'] < input.mass()]

@render_plotly
def plot():
    df_subset = df[df['body_mass_g'] < input.mass()]
    return px.scatter(df_subset, x="bill_depth_mm", y = "bill_length_mm")