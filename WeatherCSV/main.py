# NOTES:::::::


# with open("./weather_data.csv", mode="r") as weather_data:
#     data = weather_data.readlines()
#
# print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     count = 0
#     for row in data:
#         count += 1
#         if count != 1:
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)
#
# max_temp = data["temp"].max()
# print(data[data.temp == max_temp])

monday = data[data.day == "Monday"]
monday_temp = monday.temp * 9/5 + 32
print(monday_temp)