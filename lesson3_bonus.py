def create_departure_data():
    list_of_departures = [{"flight_number" : "AS213", "destination" : "London", "departure_time" : "20:00", "gate" : "B12", "passengers" : 234, "maximum_capacity" : 300, "delay_in_minutes" : 10, "cancelled" : False},
                          {"flight_number" : "AS224", "destination" : "Paris", "departure_time" : "19:00", "gate" : "C3", "passengers" : 234, "maximum_capacity" : 300, "delay_in_minutes" : 0, "cancelled" : False},
                          {"flight_number" : "AS313", "destination" : "Tokyo", "departure_time" : "18:00", "gate" : "A55", "passengers" : 123, "maximum_capacity" : 140, "delay_in_minutes" : 0, "cancelled" : False},
                          {"flight_number" : "AS423", "destination" : "Stockholm", "departure_time" : "17:00", "gate" : "B67", "passengers" : 321, "maximum_capacity" : 400, "delay_in_minutes" : 0, "cancelled" : False},
                          {"flight_number" : "AS414", "destination" : "Helsinki", "departure_time" : "17:30", "gate" : "D10", "passengers" : 421, "maximum_capacity" : 500, "delay_in_minutes" : 0, "cancelled" : False},
                          {"flight_number" : "AS513", "destination" : "Dubai", "departure_time" : "22:00", "gate" : "C33", "passengers" : 0, "maximum_capacity" : 130, "delay_in_minutes" : 0, "cancelled" : False},
                          {"flight_number" : "AS525", "destination" : "Barcelona", "departure_time" : "21:00", "gate" : "B20", "passengers" : 321, "maximum_capacity" : 350, "delay_in_minutes" : 67, "cancelled" : True},
                          {"flight_number" : "BX421", "destination" : "Amsterdam", "departure_time" : "20:45", "gate" : "E14", "passengers" : 153, "maximum_capacity" : 200, "delay_in_minutes" : 50, "cancelled" : False},
                          {"flight_number" : "BX313", "destination" : "New York", "departure_time" : "14:00", "gate" : "D66", "passengers" : 175, "maximum_capacity" : 210, "delay_in_minutes" : 0, "cancelled" : False},
                          {"flight_number" : "BR555", "destination" : "San Fransisco", "departure_time" : "12:30", "gate" : "A67", "passengers" : 56, "maximum_capacity" : 70, "delay_in_minutes" : 0, "cancelled" : True},
                          {"flight_number" : "AR123", "destination" : "Hong Kong", "departure_time" : "11:45", "gate" : "Not Assigned", "passengers" : 140, "maximum_capacity" : 200, "delay_in_minutes" : 0, "cancelled" : False}]
    return list_of_departures

def print_departure_board(departures):
    for departure in departures:
        print(f"{departure["flight_number"]} - {departure["destination"]} - {departure["departure_time"]} - Gate {departure["gate"]}")

def print_flight_status(departures):
    for departure in departures:
        status = "ON TIME"
        delay = departure["delay_in_minutes"]
        cancelled = departure["cancelled"]
        if delay >= 60:
            status = "SEVERELY DELAYED"
        elif delay >= 20 and delay <= 59:
            status = "DELAYED"
        elif delay >= 1 and delay <= 19:
            status = "SLIGHT DELAY"
        elif cancelled:
            status = "CANCELLED"
        print(f"{departure["flight_number"]} - {departure["destination"]} - {status}")

def print_flight_analysis(departures):
    number_of_scheduled_flights = len(departures)
    cancelled_flights = 0
    delayed_flights = 0
    on_time = 0
    total_passengers = 0
    largest_flight = 0
    capacity_80 = 0

    for departure in departures:
        if departure["cancelled"]:
            cancelled_flights += 1
        if departure["delay_in_minutes"] > 0:
            delayed_flights += 1
        if departure["delay_in_minutes"] == 0 and not departure["cancelled"]:
            on_time += 1
        total_passengers += departure["passengers"]
        if departure["passengers"] > largest_flight:
            largest_flight = departure["passengers"]
        if departure["passengers"] / departure["maximum_capacity"] > 0.8:
            capacity_80 += 1

    average_number_of_passengers = int(total_passengers / number_of_scheduled_flights)

    print(f"Number of scheduled flights {number_of_scheduled_flights}")
    print(f"Cancelled flights: {cancelled_flights}")
    print(f"Delayed flights: {delayed_flights}")
    print(f"Flights on time: {on_time}")
    print(f"Total passengers: {total_passengers}")
    print(f"Average numbers of passengers: {average_number_of_passengers}")
    print(f"Flight with the largest number of passengers: {largest_flight}")
    print(f"Number of flights with more than 80% of capacity filled: {capacity_80}")

def search_for_flight(departures):
    flight = input("Enter flight number: ")
    found = False
    while not found:
        for departure in departures:
            if flight == departure["flight_number"]:
                status = "ON TIME"
                if departure["cancelled"]:
                    status = "CANCELLED"
                print(f"Destination: {departure["destination"]}")
                print(f"Departure: {departure["departure_time"]}")
                print(f"Gate: {departure["gate"]}")
                print(f"Passengers: {departure["passengers"]}")
                print(f"Status: {status}")
                found = True
        break
    if not found:
        print("Flight not found.")

def print_all_gates():
    letters = ["A", "B", "C"]
    numbers = [1, 2, 3, 4]

    for letter in letters:
        for number in numbers:
            print(f"Gate {letter}{number}")



departures = create_departure_data()
print_departure_board(departures)
print("")
print_flight_status(departures)
print("")
print_flight_analysis(departures)
print("")
search_for_flight(departures)
print("")
print_all_gates()