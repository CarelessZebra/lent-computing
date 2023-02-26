from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
   #build list of stations
   stations = build_station_list()
   update_water_levels(stations)
   #get the list of 10 stations where current relative level is highest 
   station_list = stations_highest_rel_level(stations, 10)
   for x in station_list:
       print(x.name + " " + str(x.relative_water_level()))

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
