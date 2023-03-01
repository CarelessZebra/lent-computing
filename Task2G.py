from floodsystem.analysis import most_at_risk
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
import datetime
from floodsystem.datafetcher import fetch_measure_levels
import matplotlib.pyplot as plt

def run():
    stations = build_station_list()
    update_water_levels(stations)
    stations = stations_highest_rel_level(stations, 10)
    most_at_risk(stations)

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
