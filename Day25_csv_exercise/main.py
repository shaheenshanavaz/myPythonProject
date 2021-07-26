# TODO Reading data normally using files

# with open(file="weather_data.csv") as data:
#     my_weather_data = data.readlines()
#     print(my_weather_data)

# TODO reading data from a .csv file

# import csv
# with open(file="weather_data.csv") as data:
#     my_csv_data = csv.reader(data)
#     temperature = []
#     print(my_csv_data) # object gets printed
#     for row in my_csv_data:# looping through that object and printing neatly
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

# TODO Using Pandas

import pandas
my_weather_data = pandas.read_csv(filepath_or_buffer="weather_data.csv")
print(my_weather_data)
print(my_weather_data["temp"])

my_dict = my_weather_data.to_dict()
print(my_dict)

my_raw_temp = my_weather_data["temp"].to_dict()
print(my_raw_temp)
avg_temp = sum(my_raw_temp)/len(my_raw_temp)
print(f"ang temp: {avg_temp}")

# Print the row of data with Highest temperature in it
d = my_weather_data[my_weather_data["temp"] == my_weather_data["temp"].max()]
print(d)

# Print the condition of Mondoy
mon_cond = my_weather_data[my_weather_data.day == "Monday"]
print(mon_cond.condition)

# Convert Monday temperature to faherheit
mon_row = my_weather_data[my_weather_data.day == "Monday"]
mon_temp = mon_row.temp
# (9/5 × °C) + 32
mon_temp_farenheit = (9/5 * mon_temp) + 32
print(mon_temp_farenheit)