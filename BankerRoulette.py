the_names = input("Enter a list of names: ")
names = the_names.split(", ")
  
import random

names_list = len(names)

banker = random.randint(0, names_list - 1)
paying = names[banker]
print(f"{paying} is going to buy the meal today!")