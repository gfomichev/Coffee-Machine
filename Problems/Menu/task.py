menu = ["pizza", "salad", "soup"]
offers = [
    "Margarita, Four Seasons, Neapoletana, Vegetarian, Spicy",
    "Caesar salad, Green salad, Tuna salad, Fruit salad",
    "Chicken soup, Ramen, Tomato soup, Mushroom cream soup"
]

dish = input()
if dish not in menu:
    print("Sorry, we don't have it in the menu")
else:
    print(offers[menu.index(dish)])
