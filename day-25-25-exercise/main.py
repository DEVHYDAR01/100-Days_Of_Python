import pandas
# data = pandas.read_csv("./weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)
#
# data_temp = data["temp"].tolist()
# print(data_temp)
#
# print(data["temp"].mean())
# print(data["temp"].max())

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp[0])
#
# convert_to_Fahrenheit = (monday_temp * 9 / 5) + 32
# print(f"Monday's temp in Fahrenheit is {convert_to_Fahrenheit}")

# create a dataframe from scratch
# data_dict = {
#     "student": ["Hydar", "nana", "Angela"],
#     "scores": [55, 24, 70]
# }
#
# tb = pandas.DataFrame(data_dict)
# tb.to_csv("new_data.csv")

data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241023.csv")
Gray_color = []
Black_color = []
Cinnamon_color = []
Fur_colors = data["Primary Fur Color"].to_list()
for color in Fur_colors:
    if color == "Gray":
        Gray_color.append(color)
    elif color == "Black":
        Black_color.append(color)
    elif color == "Cinnamon":
        Cinnamon_color.append(color)

# creating dict and then from it a dataframe
primary_fur_colors_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [len(Gray_color), len(Cinnamon_color), len(Black_color)]
}
df = pandas.DataFrame(primary_fur_colors_dict)
df.to_csv("squirrel_count.csv")



