import pandas

data = pandas.read_csv("data.csv")
fur_color_list = data["Primary Fur Color"]
gray = 0
red = 0
black = 0
for i in fur_color_list:
    if i == "Gray":
        gray += 1
    elif i == "Cinnamon":
        red += 1
    elif i == "Black":
        black += 1
dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [gray, red, black]
}

new = pandas.DataFrame.from_dict(dict)
new.to_csv("squirelsData.csv")


