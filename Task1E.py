from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1E"""

    # Build list of stations
    stations = build_station_list()

    # Find sorted rivers
    sorted_list = rivers_by_station_number(stations, 9)

    # Display first 9 rivers
    print(sorted_list)

if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()
