# TODO length of each word in sentences
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
list1 = sentence.split()
result = {key : len(key) for key in list1}

print(result)

# TODO Coverting temp celsius to farenheit
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {key : (value* 9/5) + 32 for (key,value) in weather_c.items()}
print(weather_f)
