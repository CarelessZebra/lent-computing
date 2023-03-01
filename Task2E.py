from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
import datetime
from floodsystem.datafetcher import fetch_measure_levels
import matplotlib.pyplot as plt

def run():
    dt = 10
    stations = build_station_list()
    update_water_levels(stations)
    stations = stations_highest_rel_level(stations, 5)
    n = 0
    for station in stations:
        plt.figure(n)
        n += 1
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_levels(station, dates, levels)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()

#plot_water_levels(, dt=datetime.timedelta(days=10), levels)
