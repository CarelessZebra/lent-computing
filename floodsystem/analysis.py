import matplotlib
import numpy as np
def polyfit(dates, levels, p):
    """given the water level time history(dates, levels) for a station
    this computes the least squares fit of a polynomial degree p and returns
    a tuple of the polynomial object and the shift in the time axis"""
    #convert dates to floats
    dates = matplotlib.dates.date2num(dates)
    #get shift in data
    shift = dates[0]
    #find coefficient of best-fit polynomial
    p_coeff = np.polyfit(dates-shift, levels, p)
    #convert coefficient into a polynomial
    poly = np.poly1d(p_coeff)
    return poly, shift

