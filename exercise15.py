def get_list_of_wagons(*wagons):
    """Return a list of wagons.

    :param wagons: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(wagons)

print((get_list_of_wagons(1, 7, 12, 3, 14, 8, 5)))


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """

    misplaced_wagon1, misplaced_wagon2, locomotive, *remaining_wagons = each_wagons_id
    return [locomotive, *missing_wagons, *remaining_wagons, misplaced_wagon1, misplaced_wagon2]

print(fix_list_of_wagons([2, 5, 1, 7, 4, 12, 6, 3, 13], [3, 17, 6, 15]))

def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    
    return {**route, 
            "stops" : list(kwargs.values())}

print(add_missing_stops({"from": "New York", 
                         "to": "Miami"},
                      stop_1="Washington, DC", 
                      stop_2="Charlotte", 
                      stop_3="Atlanta",
                      stop_4="Jacksonville", 
                      stop_5="Orlando"))

def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    
    return {**route, **more_route_information}

print(extend_route_information({"from": "Berlin", "to": "Hamburg"}, {"length": "100", "speed": "50"}))


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    return list(map(list, zip(*wagons_rows)))

print(fix_wagon_depot([
                    [(2, "red"), (4, "red"), (8, "red")],
                    [(5, "blue"), (9, "blue"), (13,"blue")],
                    [(3, "orange"), (7, "orange"), (11, "orange")],
                    ]))

"""[
[(2, "red"), (5, "blue"), (3, "orange")],
[(4, "red"), (9, "blue"), (7, "orange")],
[(8, "red"), (13,"blue"), (11, "orange")]
]"""