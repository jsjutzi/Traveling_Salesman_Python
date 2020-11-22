import Distance
import ReadCSV
import datetime

# Set default lists
first_truck = []
second_truck = []
third_truck = []
second_truck_second_trip = []

first_truck_distances = []
second_truck_distances = []
third_truck_distances = []
second_truck_second_trip_distances = []

# Departure times for delivery trucks
first_truck_times = ['8:00:00']
second_truck_times = ['8:00:00']
third_truck_times = ['10:34:00']
second_truck_second_trip_times = ['08:58:00']


addresses_updated = False

# Get delivery batches for each truck
first_delivery_batch = ReadCSV.get_first_delivery_batch()
second_delivery_batch = ReadCSV.get_second_delivery_batch()
third_delivery_batch = ReadCSV.get_third_delivery_batch()
fourth_delivery_batch = ReadCSV.get_fourth_delivery_batch()


# Update start_time for each package in each truck -- O(n)
def add_start_time_to_packages(batch, times, truck):
    for item in batch:
        item[8] = times[0]

        if truck == 1:
            first_truck.append(item)
        elif truck == 2:
            second_truck.append(item)
        elif truck == 3:
            third_truck.append(item)
        elif truck == 4:
            second_truck_second_trip.append(item)


add_start_time_to_packages(first_delivery_batch, first_truck_times, 1)
add_start_time_to_packages(second_delivery_batch, second_truck_times, 2)
add_start_time_to_packages(third_delivery_batch, third_truck_times, 3)
add_start_time_to_packages(fourth_delivery_batch, second_truck_second_trip_times, 4)

# Get list of addresses
address_list = Distance.get_package_addresses()


# Append distance and address id data for packages in given truck -- O(n^2)
def add_distance_and_address_id(truck, distances):
    for current_index, current_package in enumerate(truck):
        for current_address in address_list:
            if current_package[1] == current_address[1]:
                distances.append(current_package[0])
                # Add address index value to package
                truck[current_index][9] = address_list.index(current_address)


add_distance_and_address_id(first_truck, first_truck_distances)
add_distance_and_address_id(second_truck, second_truck_distances)
add_distance_and_address_id(third_truck, third_truck_distances)
add_distance_and_address_id(second_truck_second_trip, second_truck_second_trip_distances)

# Sort packages for efficiency
Distance.calculate_shortest_route(first_truck, 1, 0)
Distance.calculate_shortest_route(second_truck, 2, 0)
Distance.calculate_shortest_route(third_truck, 3, 0)
Distance.calculate_shortest_route(second_truck_second_trip, 4, 0)

# Initialize truck distances total
first_truck_distance_total = 0
second_truck_distance_total = 0
third_truck_distance_total = 0

# Get total count of truck indexes
first_truck_index_count = len(Distance.get_first_truck_indexes())
second_truck_index_count = len(Distance.get_second_truck_indexes())
third_truck_index_count = len(Distance.get_third_truck_indexes())
second_truck_second_trip_index_count = len(Distance.get_second_truck_second_indexes())


# Convert package id's to address id's for distance calculator -- O(n)
def convert_ids(package_list, row, col):
    matching_row = 0
    matching_col = 0

    for current_package in package_list:
        if int(current_package[0]) == row:
            matching_row = current_package[9]
        if int(current_package[0]) == col:
            matching_col = current_package[9]

    return [matching_row, matching_col]


# Calculate distances to sort truck one -- O(n^2)
for index in range(first_truck_index_count):
    try:
        row = int(Distance.get_first_truck_indexes()[index])
        column = int(Distance.get_first_truck_indexes()[index + 1])

        first_truck_packages = Distance.get_first_truck()

        # Convert package id's to address id's for distance calculation -- O(n)
        converted_ids = convert_ids(first_truck_packages, row, column)
        row = converted_ids[0]
        column = converted_ids[1]

        first_truck_distance_total = Distance.calculate_total_distance(row, column, first_truck_distance_total)
        first_truck_distance_current = Distance.calculate_current_distance(row, column)

        delivery_time = Distance.calculate_truck_time(first_truck_distance_current, first_truck_times)
        Distance.update_first_truck(index, 11, str(delivery_time))
        updated_first_truck = Distance.get_first_truck()[index][0]

        ReadCSV.get_all_packages().update(int(updated_first_truck), first_truck)
    except IndexError:
        pass

# Calculate distances to sort truck two -- O(n^2)
for index in range(second_truck_index_count):
    try:
        row = int(Distance.get_second_truck_indexes()[index])
        column = int(Distance.get_second_truck_indexes()[index + 1])

        second_truck_packages = Distance.get_second_truck()

        # Convert package id's to address id's for distance calculation -- O(n)
        converted_ids = convert_ids(second_truck_packages, row, column)
        row = converted_ids[0]
        column = converted_ids[1]

        second_truck_distance_total = Distance.calculate_total_distance(row, column, second_truck_distance_total)
        second_truck_distance_current = Distance.calculate_current_distance(row, column)

        delivery_time = Distance.calculate_truck_time(second_truck_distance_current, second_truck_times)

        Distance.update_second_truck(index, 11, str(delivery_time))
        updated_second_truck = Distance.get_first_truck()[index][0]

        ReadCSV.get_all_packages().update(int(updated_second_truck), second_truck)

    except IndexError:
        pass

# Account for return to hub for both trucks -- O(1)

new_second_truck_distance_current = Distance.calculate_current_distance(0, 12)
second_truck_return_to_hub_time = Distance.calculate_truck_time(new_second_truck_distance_current, second_truck_times)
print('truck 2 return to hub time', second_truck_return_to_hub_time)

last_location_second_truck = Distance.get_second_truck()[-1][9]
second_truck_distance_total = second_truck_distance_total + Distance.calculate_current_distance(last_location_second_truck, 1)

new_first_truck_distance_current = Distance.calculate_current_distance(0, 6)
first_truck_return_to_hub_time = Distance.calculate_truck_time(new_first_truck_distance_current, first_truck_times)
print('truck 1 return to hub time', first_truck_return_to_hub_time)

last_location_first_truck = Distance.get_first_truck()[-1][9]
third_truck_distance_total = first_truck_distance_total + Distance.calculate_current_distance(last_location_first_truck, 1)

# Calculate distances to sort truck three -- O(n^2)
for index in range(third_truck_index_count):
    try:
        row = int(Distance.get_third_truck_indexes()[index])
        column = int(Distance.get_third_truck_indexes()[index + 1])

        third_truck_packages = Distance.get_third_truck()

        # Convert package id's to address id's for distance calculation -- O(n)
        converted_ids = convert_ids(third_truck_packages, row, column)
        row = converted_ids[0]
        column = converted_ids[1]

        third_truck_distance_total = Distance.calculate_total_distance(row, column, third_truck_distance_total)
        third_truck_distance_current = Distance.calculate_current_distance(row, column)

        delivery_time = Distance.calculate_truck_time(third_truck_distance_current, third_truck_times)

        Distance.update_third_truck(index, 11, str(delivery_time))
        updated_third_truck = Distance.get_third_truck()[index][0]

        ReadCSV.get_all_packages().update(int(updated_third_truck), third_truck)
    except IndexError:
        pass

for index in range(second_truck_second_trip_index_count):
    try:
        # Correct wrong address:

        row = int(Distance.get_second_truck_second_indexes()[index])
        column = int(Distance.get_second_truck_second_indexes()[index + 1])

        second_truck_second_trip_packages = Distance.get_second_truck_second_load()

        # Convert package id's to address id's for distance calculation -- O(n)
        converted_ids = convert_ids(second_truck_second_trip_packages, row, column)
        row = converted_ids[0]
        column = converted_ids[1]

        second_truck_distance_total = Distance.calculate_total_distance(row, column, second_truck_distance_total)
        second_truck_distance_current = Distance.calculate_current_distance(row, column)

        delivery_time = Distance.calculate_truck_time(second_truck_distance_current, second_truck_second_trip_times)

        Distance.update_second_truck_second_load(index, 11, str(delivery_time))
        updated_second_truck = Distance.get_second_truck_second_load()[index][0]

        ReadCSV.get_all_packages().update(int(updated_second_truck), second_truck_second_trip)
    except IndexError:
        pass

print("First truck mileage: ", first_truck_distance_total)
print("Second truck mileage: ", second_truck_distance_total)
print("Third truck mileage: ", third_truck_distance_total)


def get_total_distance():
    return second_truck_distance_total + third_truck_distance_total

# >>>> TESTING TRUCK TIMES
