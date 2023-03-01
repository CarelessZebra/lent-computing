import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime, timedelta
from floodsystem.analysis import polyfit
import datetime

def plot_water_level_with_fit(station, dates, levels, p):
    plt.plot(dates, levels, "b", label="current levels")
    poly, d0 = polyfit(dates, levels, p)
    dates = matplotlib.dates.date2num(dates)
    x1 = np.linspace(dates[0], dates[-1], 100)
    plt.plot(x1, poly(x1-d0), "y", label="polynomial fit")
    [low, high] = station.typical_range
    H = np.ones(len(levels))*high
    L = np.ones(len(levels))*low
    plt.plot(dates, H, "r", label="typical high")
    plt.plot(dates, L, "g", label="typical low")
    plt.legend()
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)
    plt.tight_layout()
    plt.show()


def plot_water_levels(station, dates, levels):
    [low, high] = station.typical_range
    H = np.ones(len(levels))*high
    L = np.ones(len(levels))*low
    plt.plot(dates, H, "r", label="typical high")
    plt.plot(dates, L, "g", label="typical low")
    plt.plot(dates, levels, "b", label="current levels")
    plt.legend()
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)
    plt.tight_layout()
    plt.show()
