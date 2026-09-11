def create_departure_data():
    list_of_departures = [{"flight_number" : "AS213", "destination" : "London", "departure_time" : "20:00", "gate" : "B12", "passengers" : 234, "maximum_capacity" : 300, "delay_in_minutes" : 10, "cancelled" : False},
                          {"flight_number" : "AS224", "destination" : "Paris", "departure_time" : "19:00", "gate" : "C3", "passengers" : 234, "maximum_capacity" : 300, "delay_in_minutes" : 0, "cancelled" : False},
                          {"flight_number" : "AS313", "destination" : "Tokyo", "departure_time" : "18:00", "gate" : "A55", "passengers" : 123, "maximum_capacity" : 140, "delay_in_minutes" : 0, "cancelled" : False},
                          {"flight_number" : "AS423", "destination" : "Stockholm", "departure_time" : "17:00", "gate" : "B67", "passengers" : 321, "maximum_capacity" : 400, "delay_in_minutes" : 0, "cancelled" : False},
                          {"flight_number" : "AS414", "destination" : "Helsinki", "departure_time" : "17:30", "gate" : "D10", "passengers" : 421, "maximum_capacity" : 500, "delay_in_minutes" : 0, "cancelled" : False},
                          {"flight_number" : "AS513", "destination" : "Dubai", "departure_time" : "22:00", "gate" : "C33", "passengers" : 111, "maximum_capacity" : 130, "delay_in_minutes" : 0, "cancelled" : False},
                          {"flight_number" : "AS525", "destination" : "Barcelona", "departure_time" : "21:00", "gate" : "B20", "passengers" : 321, "maximum_capacity" : 350, "delay_in_minutes" : 7, "cancelled" : True},
                          {"flight_number" : "BX421", "destination" : "Amsterdam", "departure_time" : "20:45", "gate" : "E14", "passengers" : 153, "maximum_capacity" : 200, "delay_in_minutes" : 50, "cancelled" : False},
                          {"flight_number" : "BX313", "destination" : "New York", "departure_time" : "14:00", "gate" : "D66", "passengers" : 175, "maximum_capacity" : 210, "delay_in_minutes" : 0, "cancelled" : False},
                          {"flight_number" : "BR555", "destination" : "San Fransisco", "departure_time" : "12:30", "gate" : "A67", "passengers" : 56, "maximum_capacity" : 70, "delay_in_minutes" : 0, "cancelled" : True}]
    return list_of_departures

def print_departure_board(departures):
    for departure in departures:
        print(f"{departure["flight_number"]} - {departure["destination"]} - {departure["departure_time"]} - Gate {departure["gate"]}")


departures = create_departure_data()
print_departure_board(departures)