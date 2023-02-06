from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()

    # Find sorted station distances
    sorted_list = stations_by_distance(stations, (52.2053, 0.1218))

    # Display first 10 and last 10
    print("first 10 closest stations")
    print(sorted_list[:10])
    print("first 10 furthest stations")
    print(sorted_list[-10:])


if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()
