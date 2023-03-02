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
    X = []
    Y = []
    L = []
    for station in stations:
        try:
            level = 1/(1+2**station.latest_level)
            L.append(level)
            X.append(station.coord[1])
            Y.append(station.coord[0])
        except:
            pass
    print(L)
    plt.scatter(X,Y,c=L,cmap="viridis")
    plt.colorbar()
    plt.show()

if __name__ == "__main__":
    print("*** Extension: CUED Part IA Flood Warning System ***")
    run()
