import csv
from HashTable import HashMap

# Read CSV file for packages
with open('./Data/package.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    hash_map = HashMap()

    # Set all three trucks to empty lists
    first_delivery_batch = []
    second_delivery_batch = []
    third_delivery_batch = []
    fourth_delivery_batch = []

    # Helper function to determine if packages is already assigned to batch -- O(1)
    def isNotAssignedToBatch(package):
        return package not in first_delivery_batch and package not in second_delivery_batch and package not in third_delivery_batch and package not in fourth_delivery_batch

    # Populate Hash Table -- O(n)
    for row in readCSV:
        id = row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zip = row[4]
        delivery = row[5]
        size = row[6]
        note = row[7]
        delivery_start = ''
        address_location = ''
        delivery_status = 'At hub'
        delivery_end = ''
        lookup_location_data = ''

        package = [id, address, city, state, zip, delivery,
                   size, note, delivery_start, address_location,
                   delivery_status, delivery_end, lookup_location_data]

        # Add second trip time-constrained packages to fourth batch

        # Add all non-delayed packages with time constraints to first batch
        if package[5] != 'EOD' and 'Delayed' not in package[7] or package[0] in ['19', '39', '21', '7']:
            if package[0] not in ['9']:
                first_delivery_batch.append(package)

        # Fourth Batch - delayed with time constraints
        if package[0] in ['6', '25', '22', '26'] and package not in first_delivery_batch:
            fourth_delivery_batch.append(package)

        # Second Batch: Load packages with 2nd truck or delayed constraints in the second batch
        if 'Can only be on truck 2' in package[7] or package[5] == 'EOD':
            if isNotAssignedToBatch(package) and len(second_delivery_batch) < 4:
                second_delivery_batch.append(package)

        if isNotAssignedToBatch(package):
            # Correct wrong address - this truck doesn't leave hub until after 10:20
            if package[0] == '9':
                package[1] = '410 S State St'
                package[4] = '84111'
            third_delivery_batch.append(package)

        # Insert package into hash table
        hash_map.insert(id, package)

    # Verify logic loaded batches correctly
    print(len(first_delivery_batch))
    print(len(second_delivery_batch))
    print(len(third_delivery_batch))
    print(len(fourth_delivery_batch))

    def get_first_delivery_batch():
        return first_delivery_batch

    def get_second_delivery_batch():
        return second_delivery_batch

    def get_third_delivery_batch():
        return third_delivery_batch

    def get_fourth_delivery_batch():
        return fourth_delivery_batch

    def get_all_packages():
        return hash_map

    def display_data_to_user(lookup_package):
        # Display current package data to user
        print()
        print("Package ID: {}".format(get_all_packages().get_value(str(lookup_package))[0]))
        print("Delivery Address: {}".format(get_all_packages().get_value(str(lookup_package))[1]))
        print("Must Be Delivered By: {}".format(get_all_packages().get_value(str(lookup_package))[5]))
        print("Delivery City: {}".format(get_all_packages().get_value(str(lookup_package))[2]))
        print("Delivery Zip Code: {}".format(get_all_packages().get_value(str(lookup_package))[4]))
        print("Package Weight: {}".format(get_all_packages().get_value(str(lookup_package))[6]))
        print("Status: {}".format(get_all_packages().get_value(str(lookup_package))[12]))
        print()

    def display_status_to_user(lookup_package):
        # Display current package status data to user
        print("Package ID: {} Status: {}".format(get_all_packages().get_value(str(lookup_package))[0], get_all_packages().get_value(str(lookup_package))[12]))







