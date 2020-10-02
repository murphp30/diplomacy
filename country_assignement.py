#!/usr/bin/env python
#Hacky script to assign countries for a game of 
#Diplomacy so that each player gets a new country
#to all previous games.
#Personal info, emails, passwords etc. have been omitted

import smtplib

from random import shuffle
import numpy as np

def email_players(name, email, country):
	#send email to all players. Takes player name, player email and player country
	sender_email="" #sender email
	to = [email]
	subject = "Diplomacy Times January 1901"
	text = """Breaking news.\n The leader of """ + country + """ has resigned and """ + name + """ has been named as their replacement.
Will they escalate tensions in Europe or strive for peace?  
For this game Diplomacy, you will be taking the role of the leader of """ + country + """.
You will need to set up an account on vdiplomacy.net and join the game Pearse will tell you to. Be sure to pick your designated country!
There is a quick guide to the rules here https://vdiplomacy.net/intro.php but we'll try and give a comprehensive overview before we start.
Good luck and have fun!"""+"""\nPearse"""

	message = "\From: %s\nTo: %s\nSubject: %s\n\n%s" % (sender_email, ", ".join(to), subject, text) 

	with smtplib.SMTP("", 587) as server: #mail server
		server.ehlo()
		server.starttls()
		server.login("", "") #user name, password (plain text, yuk!)
		server.sendmail(sender_email, to, message)

#Dictionary with player name and player email
players = {
		"P1":"",
		"P2":"",
		"P3":"", 
		"P4":"",
		"P5":"",
		"P6":"",
		"P7":""}

countries = ["Austria", "Germany", "Turkey", 
			"Russia", "Italy", "France", "Britain"]

#Previous games with friends
# disallowed = {"P":["Germany","France"],
# 				"MC":["Austria","Russia"], 
# 				"T":["Turkey","Britain"],
# 				"C":["Italy","Germany"],
# 				"N":["Russia","Austria"],
# 				"B":["Britain","Italy"],
# 				"MF":["France","Turkey"]}
disallowed = {
				"P1":[""],
				"P2":[""], 
				"P3":[""],
				"P4":[""],
				"P5":[""],
				"P6":[""],
				"P7":[""]}
player_names = list(players.keys())
shuffle(player_names)
shuffle(countries)

dis = np.array([disallowed[player] for player in player_names])
samsies = np.sum([dis[:,i] == np.array(countries) for i in range(dis.shape[1])])
while np.sum(samsies) != 0:
	#loop to make sure you haven't played that country before
	shuffle(player_names)
	shuffle(countries)
	dis = np.array([disallowed[player] for player in player_names])
	samsies = np.sum([dis[:,i] == np.array(countries) for i in range(dis.shape[1])])


new_roles = {player:country for player, country in zip(player_names,countries)}

for key in new_roles.keys():
	#Send email and print who's playing which country. 
	#Comment print statment for anonymous game
	print("{} will be playing as: {}".format(key,new_roles[key] ))
	email_players(key, players[key], new_roles[key])