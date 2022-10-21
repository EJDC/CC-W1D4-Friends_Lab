
from unittest import TextTestRunner


def get_name(dict):
    return dict["name"]
    
def get_favourite_tv_show(dict):
    return dict["favourites"]["tv_show"]

def likes_to_eat(dict, food):
    if food in dict["favourites"]["snacks"]:
        return True
    else:
        return False

def add_friend(dict, name):
     dict.get("friends").append(name)

def remove_friend(dict, name):
    dict.get("friends").remove(name)

def total_money(people):
    total_money = 0
    for person in people:
        total_money += person["monies"]
    return total_money

def lend_money(person1, person2, loan):
    person1["monies"] -= loan
    person2["monies"] += loan

def all_favourite_foods(people):
    food_list = []
    for person in people:
        food_list += person["favourites"]["snacks"]
    return food_list

def find_no_friends(people):
    friendless = []
    for person in people:
        if person["friends"] == []:
            friendless.append(person) #didn't work for += ???
    return friendless

def unique_favourite_tv_shows(people):
    tv_shows = []
    for person in people:
        tv_shows.append(person["favourites"]["tv_show"])
        unique = set(tv_shows)
    return unique
        