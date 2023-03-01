import matplotlib
import numpy as np
import datetime
from floodsystem.datafetcher import fetch_measure_levels


def polyfit(dates, levels, p):
    dates = matplotlib.dates.date2num(dates)
    shift = dates[0]
    p_coeff = np.polyfit(dates-shift, levels, p)
    poly = np.poly1d(p_coeff)
    return poly, shift

def most_at_risk(stations):
    dt = 5
    max = 0
    ans = ""
    for station in stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        dates = matplotlib.dates.date2num(dates)
        d0 = dates[0]
        p_coeff = np.polyfit(dates-d0, levels, 4)
        poly = np.poly1d(p_coeff)
        x1 = np.linspace(dates[0], dates[-1], 100)
        diff = poly(x1-station.typical_range[1])
        sum = np.sum(diff)
        if sum > max:
            ans = station.name
            max = sum
        print(max, ans, sum, station.name)
        print(ans)
    print(ans)
