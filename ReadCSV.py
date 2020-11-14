#Read data from CSV files

import csv
from HashTable import HashMap

with open('./Data/package.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    hash_map = HashMap()

    # Set all three trucks to empty lists
    first_truck = []
    second_truck = []
    third_truck = []

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

        package = [id, address, city, state, zip, delivery,
                 size, note, delivery_start, address_location,
                 delivery_status]

        # Third Truck: Wrong address
        if package[0] == '9':
            third_truck.append(package)

        # Second truck: Load packages with 2nd truck or delayed constraints on the second truck, exclude "Must group"
        if 'Can only be on truck 2' in package[7] or 'Delayed' in package[7]:
                second_truck.append(package)

        # First truck: Load "Must" group and "by time" packages on first truck:
        if package[5] != 'EOD' or package[0] == 19:
            if package not in second_truck and package not in third_truck:
                first_truck.append(package)

        # Evenly distribute remaining packages between second and third trucks
        if package not in first_truck and package not in second_truck and package not in third_truck:
            if len(second_truck) < len(third_truck):
                second_truck.append(package)
            else:
                third_truck.append(package)

        # Insert package into hash table
        hash_map.insert(id, package)

    #Verify logic loaded trucks correctly
    print(len(first_truck))
    print(len(second_truck))
    print(len(third_truck))

    def get_first_truck():
        return first_truck

    def get_second_truck():
        return second_truck

    def get_third_truck():
        return third_truck

    def get_all_packages():
        return hash_map










