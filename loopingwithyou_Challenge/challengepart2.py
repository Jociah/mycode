#!/usr/bin/env python3

user_input = input("Choose a farm (NE Farm, W Farm, SE Farm): ")

for farm in farms:
    if farm["name"] == user_input:
        for item in farm["agriculture"]:
            print(item)

