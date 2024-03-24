import random

#List of friends:
friend_list = ["Juan", "Joaquin", "Eduardo"]
print(f"Name of the friends: {friend_list}")
list_length = len(friend_list)
print(f"friends in the game: {list_length}")

random_choice = random.randint(0, list_length-1)
print(f"{friend_list[random_choice]}" + " is going to buy the meal today!")

