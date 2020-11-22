# Student Name: Jack Jutzi
# Student ID: 001073745

import datetime
from ReadCSV import get_all_packages, display_data_to_user, display_status_to_user
from Packages import get_total_distance
from Distance import get_first_truck
from Distance import get_second_truck
from Distance import get_third_truck
from Distance import get_second_truck_second_load
class Main:
    # This is the opening message shown to a user when the program initiates
    print('*************************************')
    print('*************************************')
    print("**** WGU Package Delivery System ****")
    print('*************************************')
    print('*************************************')
    print()
    print(f'Total route mileage after all deliveries was {get_total_distance():.2f} miles.')

    # Give user option to lookup a single package at a given time
    # Or to look up all packages for a given time

    print("""
    Please select from the following options or enter 'exit' to exit program:
        1. Lookup single package for a given time
        2. Lookup all packages for a given time
    """)
    lookup_choice = input("")

    while lookup_choice != 'exit':
        # Choice 1
        # Lookup single package at a given time

        if lookup_choice == '1':
            try:
                lookup_package = input('Please enter a package id: ')
                lookup_time = input('Please enter exact time (hh:mm:ss): ')

                # Use built-in datetime class to format timedelta - will be used for comparisons
                (h, m, s) = lookup_time.split(':')
                entered_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

                # Deal with time differences -- O(n)
                start_time = get_all_packages().get_value(lookup_package)[8]
                end_time = get_all_packages().get_value(lookup_package)[11]

                # Convert start time
                (h, m, s) = start_time.split(':')
                converted_start_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

                # Convert end time (delivery time)
                (h, m, s) = end_time.split(':')
                converted_end_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

                # Check for packages that are loaded on trucks that have not left the hub yet
                if converted_start_time >= entered_time:
                    # Reset defaults for current iteration
                    get_all_packages().get_value(str(lookup_package))[10] = 'At Hub'
                    get_all_packages().get_value(str(lookup_package))[12] = 'Will leave hub at {}'.format(start_time)
                    display_data_to_user(lookup_package)

                # Check for packages that have already left the hub
                elif converted_start_time < entered_time:
                    # Check to see if package is in transit or has already been delivered
                    if entered_time < converted_end_time:
                        get_all_packages().get_value(str(lookup_package))[10] = 'In Transit'
                        get_all_packages().get_value(str(lookup_package))[12] = 'Went out for delivery at {}'.format(start_time)
                        display_data_to_user(lookup_package)
                    else:
                        get_all_packages().get_value(str(lookup_package))[10] = 'Delivered'
                        get_all_packages().get_value(str(lookup_package))[12] = 'Package delivered at {}'.format(end_time)
                        display_data_to_user(lookup_package)

            except ValueError:
                print('There was a problem with your entry, exiting program')
                exit()
        # Choice 2
        # Lookup all packages for a given time
        elif lookup_choice == '2':
            try:
                lookup_time = input('Please enter exact time (hh:mm:ss): ')

                # Use built-in datetime class to format timedelta - will be used for comparisons
                (h, m, s) = lookup_time.split(':')
                entered_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

                # Deal with time differences -- O(n)
                for index in range(1, 41):
                    start_time = get_all_packages().get_value(str(index))[8]
                    end_time = get_all_packages().get_value(str(index))[11]

                    # Convert start time
                    (h, m, s) = start_time.split(':')
                    converted_start_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

                    # Convert end time (delivery time)
                    (h, m, s) = end_time.split(':')
                    converted_end_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

                    # Check for packages that are loaded on trucks that have not left the hub yet
                    # Check for packages that are loaded on trucks that have not left the hub yet
                    if converted_start_time >= entered_time:
                        # Reset defaults for current iteration
                        get_all_packages().get_value(str(index))[10] = 'At Hub'
                        get_all_packages().get_value(str(index))[12] = 'Will leave hub at {}'.format(start_time)
                        display_status_to_user(index)

                    # Check for packages that have already left the hub
                    elif converted_start_time < entered_time:
                        # Check to see if package is in transit or has already been delivered
                        if entered_time < converted_end_time:
                            get_all_packages().get_value(str(index))[10] = 'In Transit'
                            get_all_packages().get_value(str(index))[12] = 'Went out for delivery at {}'.format(
                                start_time)
                            display_status_to_user(index)
                        else:
                            get_all_packages().get_value(str(index))[10] = 'Delivered'
                            get_all_packages().get_value(str(index))[12] = 'Package delivered at {}'.format(
                                end_time)
                            display_status_to_user(index)

            except ValueError:
                print('There was a problem with your entry, exiting program')
                exit()


        # Exit program
        elif lookup_choice == 'exit':
            exit()




