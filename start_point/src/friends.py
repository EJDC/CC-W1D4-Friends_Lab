
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
