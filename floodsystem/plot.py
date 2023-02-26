import matplotlib as plt
import numpy as np
from analysis import polyfit
def plot_water_level_with_fit(station, dates, levels, p):
    """This function plots the water levels against time with
    the best-fit polynomial from analysis.polyfit function"""
    #plot_water_levels(stations, dates, levels)
    poly, shift = polyfit(dates, levels, p)
    dates = plt.dates.date2num(dates)
    #plot polynomial fit with 100 points along the interval
    x1 = np.linspace(dates[0], dates[-1], 100)
    plt.plot(x1, poly(x1-shift))
    plt.show()