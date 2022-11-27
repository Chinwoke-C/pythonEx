

if __name__ == '__main__':
    mile = 0
    gallon = 0
    total_mile = 0
    total_gallon = 0
    counter = 0
    mile_travelled = int(input("Enter mile or -1 to quit"))
    gallon_used = int(input("Enter gallons used"))
    while mile_travelled != -1 and gallon_used != -1:
        total_mile += mile_travelled
        total_gallon += gallon_used
        mile_per_gallon = mile_travelled / gallon_used
        print(f'The mile used for this trip is: {mile_per_gallon}')
    counter += 1

    mile_per_gallon_combined = total_mile / total_gallon
    print(f'The combined mile_per_gallon used for all trip is {mile_per_gallon_combined}')