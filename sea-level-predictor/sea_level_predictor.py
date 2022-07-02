import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('sea-level-predictor/epa-sea-level.csv')

    # Create scatter plot
    df_x = df['Year']
    df_y = df['CSIRO Adjusted Sea Level']
    plt.scatter(df_x, df_y, color='black')

    # Create first line of best fit
    line_1 = linregress(df_x, df_y)
    x1 = np.arange(df_x.min(), 2051, 1)
    y1 = x1 * line_1.slope + line_1.intercept
    plt.plot(x1, y1, color='red')

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    df_2000_x = df_2000['Year']
    df_2000_y = df_2000['CSIRO Adjusted Sea Level']

    line_2 = linregress(df_2000_x, df_2000_y)
    x2 = np.arange(2000, 2051, 1)
    y2 = x2 * line_2.slope + line_2.intercept

    plt.plot(x2, y2, color='orange')

    # set labels
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()