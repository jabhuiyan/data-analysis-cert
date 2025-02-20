import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")


    # Create scatter plot
    plt.figure(figsize=(10,6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], label="Observed Data")

    # Create first line of best fit
    slope_all, intercept_all, _, _, _ = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years_all = range(1880, 2051)
    plt.plot(years_all, slope_all * pd.Series(years_all) + intercept_all, 'r', label="Best Fit Line (1880-2050)")

    # Create second line of best fit
    df_recent = df[df["Year"] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    years_recent = range(2000, 2051)
    plt.plot(years_recent, slope_recent * pd.Series(years_recent) + intercept_recent, 'g', label="Best Fit Line (2000-2050)")
    

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
