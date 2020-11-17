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
    package_id_addresses = []

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

        # Third Batch: Wrong address
        if package[0] == '9':
            third_delivery_batch.append(package)

        # Second Batch: Load packages with 2nd truck or delayed constraints in the second batch
        if 'Can only be on truck 2' in package[7] or 'Delayed' in package[7]:
            second_delivery_batch.append(package)

        # First Batch: Load "Must" group and "by time" packages in first batch:
        if package[5] != 'EOD' or package[0] == 19:
            if package not in second_delivery_batch and package not in third_delivery_batch:
                first_delivery_batch.append(package)

        # Evenly distribute remaining packages between second and third trucks
        if package not in first_delivery_batch and package not in second_delivery_batch and package not in third_delivery_batch:
            if len(second_delivery_batch) < len(third_delivery_batch):
                second_delivery_batch.append(package)
            else:
                third_delivery_batch.append(package)

        # Insert package into hash table
        hash_map.insert(id, package)

    # Verify logic loaded trucks correctly
    print(len(first_delivery_batch))
    print(len(second_delivery_batch))
    print(len(third_delivery_batch))

    def get_first_delivery_batch():
        return first_delivery_batch

    def get_second_delivery_batch():
        return second_delivery_batch

    def get_third_delivery_batch():
        return third_delivery_batch

    def get_all_packages():
        return hash_map









