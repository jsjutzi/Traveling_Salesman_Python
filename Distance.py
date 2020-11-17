import csv
import datetime

# Read CSV files for distances
with open('./Data/distance.csv') as csvfile:
    distance_csv = list(csv.reader(csvfile, delimiter=','))

with open('./Data/location.csv') as csvfile2:
    location_csv = list(csv.reader(csvfile2, delimiter=','))

    # Calculate total distance -- O(1)
    def calculate_total_distance(row, col, total):
        distance = distance_csv[row][col]
        # If row, col pair has empty value, use inverse -- O(1)
        if distance >= '':
            distance = distance_csv[col][row]
        return total + float(distance)

    # Calculate current distance -- O(1)
    def calculate_current_distance(row, col):
        distance = distance_csv[row][col]

        # If row, col pair has empty value, use inverse -- O(1)
        if not distance:
            distance = distance_csv[col][row]

        return float(distance)

    # Calculate total time for given truck -- O(n)
    # Trucks move at an average of 18 mph for this purpose
    def calculate_truck_time(distance, truck_time_list):
        new_time = distance / 18
        distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(new_time * 60, 60))
        total_time = distance_in_minutes + ':00'
        truck_time_list.append(total_time)
        total = datetime.timedelta()

        for i in truck_time_list:
            (h, m, s) = i.split(':')
            total += datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

        return total

    # These lists represent sorted trucks that are optimized for efficiency in the following function
    first_truck = []
    first_truck_index_list = []

    second_truck = []
    second_truck_index_list = []

    third_truck = []
    third_truck_index_list = []

    # This algorithm uses the 'greedy' approach to optimize the delivery route for each truck.
    # It takes 3 parameters as listed below:
    # 1. The list of packages for a truck that hasn't been optimized.
    # 2. The truck number
    # 3. The current location of the truck.

    # The algorithm works in the following steps:
    # 1. It checks for the base case (the package list is empty or invalid) and returns out of the function.
    # 2. If step 1 passed, it then iterates through each package in the list to find the shortest possible distance
    #    to the next location based on the current location.  It re-assigns the "lowest_value" each time a lesser
    #    distance is found, ensuring that the minimum value is used for the next step.
    # 3. The algorithm then iterates through the package list AGAIN, this time conducting a boolean check
    #    to see if the distance between the current location and location of the currently iterated package is equal
    #    to the "lowest_value" that has already been determined.
    # 4. If that boolean is true, the algorithm checks to see which truck the package is associated with and appends
    #    values to the necessary truck lists.  The package is then removed from the package list, current location is
    #    updated, and the function calls itself recursively with the updated arguments.  This continues until we reach
    #    the base case, where the list is empty.

    #    This function has a space-time complexity of O(n^2)

    def calculate_shortest_route(package_list, truck_num, current_location):
        if len(package_list) == 0 or not len(package_list):
            return package_list

        lowest_value = 50.0
        new_location = 0

        for package in package_list:
            value = int(package[9])
            current_distance = calculate_current_distance(current_location, value)
            # Update lowest_value if the current distance is lesser
            if current_distance <= lowest_value:
                lowest_value = current_distance

        for package in package_list:
            if calculate_current_distance(current_location, int(package[9])) == lowest_value:
                if truck_num == 1:
                    # Load on first truck
                    first_truck.append(package)
                    first_truck_index_list.append(package[0])

                    # Update current location and package list for next recursive call
                    current_location = new_location
                    package_list.pop(package_list.index(package))

                    # Recursively call function
                    calculate_shortest_route(package_list, 1, current_location)
                elif truck_num == 2:
                    # Load on second truck
                    second_truck.append(package)
                    second_truck_index_list.append(package[0])

                    # Update current location and package list for next recursive call
                    current_location = new_location
                    package_list.pop(package_list.index(package))

                    # Recursively call function
                    calculate_shortest_route(package_list, 2, current_location)
                elif truck_num == 3:
                    # Load on third truck
                    third_truck.append(package)
                    third_truck_index_list.append(package[0])

                    # Update current location and package list for next recursive call
                    current_location = new_location
                    package_list.pop(package_list.index(package))

                    # Recursively call function
                    calculate_shortest_route(package_list, 3, current_location)

    # Getter functions to return optimized trucks -- All are O(1)
    first_truck_index_list.insert(0, '0')
    second_truck_index_list.insert(0, '0')
    third_truck_index_list.insert(0, '0')

    def get_first_truck_indexes():
        return first_truck_index_list

    def get_first_truck():
        return first_truck

    def get_second_truck_indexes():
        return second_truck_index_list

    def get_second_truck():
        return second_truck

    def get_third_truck_indexes():
        return third_truck_index_list

    def get_third_truck():
        return third_truck

    # Get address info for packages
    def get_package_addresses():
        return location_csv
