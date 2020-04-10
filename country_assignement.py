#!/usr/bin/env python
#Hacky script to assign countries for a game of 
#Diplomacy so that each player gets a new country
#to the last game.

from random import shuffle
import numpy as np
players = ["Pearse", "Mark", "Tim", 
		"Conor", "Niall", "Billy", "Max"]

countries = ["Austria", "Germany", "Turkey", 
			"Russia", "Italy", "France", "Britain"]

disallowed = {"Pearse":"Germany", "Mark":"Austria", "Tim":"Turkey",
			"Conor":"Italy", "Niall":"Russia", "Billy":"Britain",
			"Max":"France"}
shuffle(players)
shuffle(countries)


samsies = np.array([disallowed[player] for player in players]) == np.array(countries)
# i=0
while np.sum(samsies) != 0:
	# print(i)
	shuffle(players)
	shuffle(countries)
	samsies = np.array([disallowed[player] for player in players]) == np.array(countries)
	# i+=1

new_roles = {player:country for player, country in zip(players,countries)}

for key in new_roles.keys():
	print("{} will be playing as: {}".format(key,new_roles[key] ))