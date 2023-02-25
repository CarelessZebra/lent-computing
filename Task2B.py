from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold


def run():
   #build list of stations
   stations = build_station_list()
   update_water_levels(stations)
   #get the list of tuples of stations and relative levels where the relative water level is above the tolerance of 08
   stations_with_levels_over_threshold = stations_level_over_threshold(stations, 0.8)
   for x in stations_with_levels_over_threshold:
       print(x[0].name + " " + str(x[1]) )

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
