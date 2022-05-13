import random
p1 = [] # список улиц первого игрока
p2 = [] # список улиц второго игрока
d1 = [] # список домов на улицах первого игрока
d2 = [] # список домов на улицах второго игрока
t = int
def rand(t): # функция выбора рандомного числа
	a = random.randint(1,6)
	b = random.randint(1,6)
	c = a + b
	return c
a = int
b = int
c = int
s1 = 500 # баланс первого игрока
s2 = 500 # баланс второго игрока
k1 = 0 # координата первого игрока
k2 = 0 # координата второго игрока


streets = ['Start', 'Mediterranean Avenue', 'Baltic Avenue', 'Income Tax', 'Reading Railroad', 'Oriental Avenue', 'Vermont Avenue', 'Connecticut Avenue', 'Visiting Jail', 'St. Charles Place', 'Electric Company', 'States Avenue', 'Virginia Avenuev', 'Pennsylvania Railroad', 'St. James Place', 'Tennessee Avenue', 'New York Avenue', 'Free Parking', 'Kentucky Avenue', 'Indiana Avenue', 'Illinois Avenue', 'B & O Railroad', 'Atlantic Avenue', 'Ventnor Avenue', 'Water Works', 'Marvin Gardens', 'Go To Jail', 'Pacific Avenue', 'North Carolina Avenue', 'Pennsylvania Avenue', 'Short Line', 'Park Place', 'Luxury Tax', 'Boardwalk']
prises = [0, 60, 60, 200, 200, 100, 100, 120, 0, 140, 150, 140, 160, 200, 180, 180, 200, 0, 200, 220, 240, 200, 260, 260, 250, 280, 0, 300, 300, 320, 200, 350, 100, 400]
#print(len(streets), len(prises))
print("Welcome ot Monopoly, let's start!\n")
while s1 > 0 and s2 > 0:





	print("\nThe first player throws cubes(y/n)")
	c1 = input()
	if c1 == 'y':
		c = rand(t)
		print("The numbers on the cubes:", c)
		k1 = k1 + c
		if k1 > 33:
			k1 = k1 - 34
			s1 = s1 + 200
			print("Player 1 passed field Start, recieve 200.")
			print("You budget is", s1)
	else:
		print("ERROR")
	print("Your position is", streets[k1], "( with coordinate", k1, ")")
	if streets[k1] != 'Start' and streets[k1] != 'Income Tax' and streets[k1] != 'Free Parking' and streets[k1] != 'Visiting Jail' and streets[k1] != 'Go To Jail' and streets[k1] != 'Luxury Tax' and streets[k1] not in p1 and streets[k1] not in p2:
		if s1 > prises[k1]:
			print("You budget is", s1,  ". Do you want to buy" , streets[k1],"for the price", prises[k1], "?(y/n)")
			c1 = input()
			if c1 == 'y':
				p1.append(streets[k1])
				s1 = s1 - prises[k1]
				print("You budget after purchase:", s1)
				print("Your collection:", p1, "\n")





				if s1 > 50: 
					print("Your budget is", s1, ". Do you want to build a house on this street(you should pay 50 for one house)?(y/n)")
					c1 = input()
					if c1 == 'y':
						print("How many houses do you want?")
						y1 = int(input())
						if s1 > 1 * 50:
							s1 = s1 - y1 * 50
							d1.append(y1)
					else:
						d1.append(0)
					print("Your budget after building is", s1)
					print("Your collection", p1)
					print("Homes on your streets:", d1, "\n")






			else:
				print("Your collection:", p1)
				print("Homes on your streets:", d1, "\n")
		else:
			print("You haven't got", prises[k1], "for buying this streets, because you have only", s1, "\n")





	elif streets[k1] == 'Start':
		print("You passed the start field, get 200")
		s1 = s1 + 200
		print("You budget is", s1, "\n")



		print("You have:", p1, "and on this streets you have:", d1, "buildings")
		if len(p1) != 0:
			print("Do you want to biuld some houses on your streets?")
			c1 = input()
			if c1 == 'y':
				print("On what streets you wan to build?")
				str_number = input()
				while not str_number.isdigit():
					print("Please, enter the digit")
					str_number = input()
				a = int(str_number) - 1
				print("Okey, and how buildings do you want to build?(price for one house - 50 and you have", s1, ")")
				a1 = int(input())
				if s1 > 50 * a1:
					d1[a] = d1[a] + a1
					print("Okey, now on the", streets[a], "you have", d1[a], "buildings\n")
					s1 = s1 - a * 50
				else:
					print("You haven't got some money for this operation\n")
			



	elif streets[k1] == 'Income Tax':
		print("You hit the field Income Tax, pay 100")
		s1 = s1 - 100
		print("You budget is", s1, "\n")


		print("You have:", p1, "and on this streets you have:", d1, "buildings")
		if len(p1) != 0:
			print("Do you want to biuld some houses on your streets?")
			c1 = input()
			if c1 == 'y':
				print("On what streets you wan to build?")
				str_number = input()
				while not str_number.isdigit():
					print("Please, enter the digit")
					str_number = input()
				a = int(str_number) - 1
				print("Okey, and how buildings do you want to build?(price for one house - 50 and you have", s1, ")")
				a1 = int(input())
				if s1 > 50 * a1:
					d1[a] = d1[a] + a1
					print("Okey, now on the", streets[a], "you have", d1[a], "buildings\n")
					s1 = s1 - a * 50
				else:
					print("You haven't got some money for this operation\n")
			



	elif streets[k1] == 'Free Parking':
		print("You are on the Free Parking", "\n")


		print("You have:", p1, "and on this streets you have:", d1, "buildings")
		if len(p1) != 0:
			print("Do you want to biuld some houses on your streets?")
			c1 = input()
			if c1 == 'y':
				print("On what streets you wan to build?")
				str_number = input()
				while not str_number.isdigit():
					print("Please, enter the digit")
					str_number = input()
				a = int(str_number) - 1
				print("Okey, and how buildings do you want to build?(price for one house - 50 and you have", s1, ")")
				a1 = int(input())
				if s1 > 50 * a1:
					d1[a] = d1[a] + a1
					print("Okey, now on the", streets[a], "you have", d1[a], "buildings\n")
					s1 = s1 - a * 50
				else:
					print("You haven't got some money for this operation\n")
			



	elif streets[k1] == 'Visiting Jail':
		print("You are on the Jail, but only for visiting", "\n")


		print("You have:", p1, "and on this streets you have:", d1, "buildings")
		if len(p1) != 0:
			print("Do you want to biuld some houses on your streets?")
			c1 = input()
			if c1 == 'y':
				print("On what streets you wan to build?")
				str_number = input()
				while not str_number.isdigit():
					print("Please, enter the digit")
					str_number = input()
				a = int(str_number) - 1
				print("Okey, and how buildings do you want to build?(price for one house - 50 and you have", s1, ")")
				a1 = int(input())
				if s1 > 50 * a1:
					d1[a] = d1[a] + a1
					print("Okey, now on the", streets[a], "you have", d1[a], "buildings\n")
					s1 = s1 - a * 50
				else:
					print("You haven't got some money for this operation\n")
			



	elif streets[k1] == 'Go To Jail':
		print("You are going to jail, you should pay 100")
		s1 = s1 - 100
		k1 = 8
		print("You budget is", s1, "\n")
		print("You have:", p1, "and on this streets you have:", d1, "buildings")


	elif streets[k1] == 'Electric Company' and streets[k1] in p2 or streets[k1] == 'Water Warks' and streets[k1] in p2:
		print("You are on the komercial company and you should throw cubes and pay for the second player 10x sum\n")
		print("Throw cubes:(y)\n")
		c3 = input()
		if c3 == 'y':
			c = rand(t)
			print("The numbers on the cubes:", c, "\n")
			print("You should pay", 10 * c, "for the second player\n")
			s1 = s1 - 10 * c
			s2 = s2 + 10 * c
			print("You budget is", s1, "\n")





		print("You have:", p1, "and on this streets you have:", d1, "buildings")
		if len(p1) != 0:
			print("Do you want to biuld some houses on your streets?")
			c1 = input()
			if c1 == 'y':
				print("On what streets you wan to build?")
				str_number = input()
				while not str_number.isdigit():
					print("Please, enter the digit")
					str_number = input()
				a = int(str_number) - 1
				print("Okey, and how buildings do you want to build?(price for one house - 50 and you have", s1, ")")
				a1 = int(input())
				if s1 > 50 * a1:
					d1[a] = d1[a] + a1
					print("Okey, now on the", streets[a], "you have", d1[a], "buildings\n")
					s1 = s1 - a * 50
				else:
					print("You haven't got some money for this operation\n")
			



	elif streets[k1] == 'Luxury Tax':
		print("You hit the field Luxury Tax, pay 200")
		s1 = s1 - 200
		print("You budget is", s1, "\n")





		print("You have:", p1, "and on this streets you have:", d1, "buildings")
		if len(p1) != 0:
			print("Do you want to biuld some houses on your streets?")
			c1 = input()
			if c1 == 'y':
				print("On what streets you wan to build?")
				str_number = input()
				while not str_number.isdigit():
					print("Please, enter the digit")
					str_number = input()
				a = int(str_number) - 1
				print("Okey, and how buildings do you want to build?(price for one house - 50 and you have", s1, ")")
				a1 = int(input())
				if s1 > 50 * a1:
					d1[a] = d1[a] + a1
					print("Okey, now on the", streets[a], "you have", d1[a], "buildings\n")
					s1 = s1 - a * 50
				else:
					print("You haven't got some money for this operation\n")



	elif streets[k1] in p2:
		print(streets[k1], "is property of player 2. You should pay 50 to the second player")
		s2 = s2 + 50
		s1 = s1 - 50
		print("You budget is", s1, "\n")



		print("You have:", p1, "and on this streets you have:", d1, "buildings")
		if len(p1) != 0:
			print("Do you want to biuld some houses on your streets?")
			c1 = input()
			if c1 == 'y':
				print("On what streets you wan to build?")
				str_number = input()
				while not str_number.isdigit():
					print("Please, enter the digit")
					str_number = input()
				a = int(str_number) - 1
				print("Okey, and how buildings do you want to build?(price for one house - 50 and you have", s1, ")")
				a1 = int(input())
				if s1 > 50 * a1:
					d1[a] = d1[a] + a1
					print("Okey, now on the", streets[a], "you have", d1[a], "buildings\n")
					s1 = s1 - a * 50
				else:
					print("You haven't got some money for this operation\n")



	





	print("\nThe second player throws cubes(y/n)")
	c2 = input()
	if c2 == 'y':
		c = rand(t)
		print("The numbers on the cubes:", c)
		k2 = k2 + c
		if k2 > 33:
			k2 = k2 - 34
			s2 = s2 + 200
			print("Player 2 passed field Start, recieve 200.")
			print("You budget is", s2, "\n")
	else:
		print("ERROR")
		
	print("Your position is", streets[k2], "( with coordinate", k2, ")")
	if streets[k2] != 'Start' and streets[k2] != 'Income Tax' and streets[k2] != 'Free Parking' and streets[k2] != 'Visiting Jail' and streets[k2] != 'Go To Jail' and streets[k2] != 'Luxury Tax' and streets[k2] not in p1 and streets[k2] not in p2:
		if s2 > prises[k2]:
			print("You budget is", s2,  ". Do you want to buy" , streets[k2], "for the prise", prises[k2], "?(y/n)")
			c2 = input()
			if c2 == 'y':
				p2.append(streets[k2])
				s2 = s2 - prises[k2]
				print("You budget after purchase:", s2)
				print("Your collection", p2, "\n")





				if s2 > 50: 
					print("Your budget is", s2, ". Do you want to build a house on this street(you should pay 50 for one house)?(y/n)")
					c2 = input()
					if c2 == 'y':
						print("How many houses do you want?")
						y2 = int(input())
						if s2 > y2 * 50:
							s2 = s2 - y2 * 50
							d2.append(y2)
					else:
						d2.append(0)
					print("Your budget after building is", s2)
					print("Your collection", p2)
					print("Homes on your streets:", d2, "\n")








			else:
				print("Your collection:", p2)
				print("Homes on your streets:", d2, "\n")
		else:
			print("You haven't got", prises[k2], "for buying this streets, because you have only", s2, "\n")




	elif streets[k2] == 'Start':
		print("You passed the start field, get 200")
		print("You budget is", s2, "\n")
		s2 = s2 + 200


		print("You have:", p2, "and on this streets you have:", d2, "buildings")
		if len(p1) != 0:
			print("Do you want to biuld some houses on your streets?")
			c2 = input()
			if c2 == 'y':
				print("On what streets you wan to build?")
				str_number = input()
				while not str_number.isdigit():
					print("Please, enter the digit")
					str_number = input()
				a = int(str_number) - 1
				print("Okey, and how many buildings do you want to build?(price for one house - 50 and you have", s2, ")")
				a2 = int(input())
				if s2 > 50 * a2:
					d2[a] = d2[a] + a2
					print("Okey, now on the", streets[a], "you have", d2[a], "buildings\n")
					s2 = s2 - a * 50
				else:
					print("You haven't got some money for this operation\n")


	elif streets[k2] == 'Income Tax':
		print("You hit the field Income Tax, pay 100")
		s2 = s2 - 100
		print("You budget is", s2, "\n")


		print("You have:", p2, "and on this streets you have:", d2, "buildings")
		if len(p2) != 0:
			print("Do you want to biuld some houses on your streets?")
			c2 = input()
			if c2 == 'y':
				print("On what streets you wan to build?")
				str_number = input()
				while not str_number.isdigit():
					print("Please, enter the digit")
					str_number = input()
				a = int(str_number) - 1
				print("Okey, and how many buildings do you want to build?(price for one house - 50 and you have", s2, ")")
				a2 = int(input())
				if s2 > 50 * a2:
					d2[a] = d2[a] + a2
					print("Okey, now on the", streets[a], "you have", d2[a], "buildings\n")
					s2 = s2 - a * 50
				else:
					print("You haven't got some money for this operation\n")
				

	elif streets[k2] == 'Free Parking':
		print("You are on the Free Parking")

		print("You have:", p2, "and on this streets you have:", d2, "buildings")
		if len(p2) != 0:
			print("Do you want to biuld some houses on your streets?")
			c2 = input()
			if c2 == 'y':
				print("On what streets you wan to build?")
				str_number = input()
				while not str_number.isdigit():
					print("Please, enter the digit")
					str_number = input()
				a = int(str_number) - 1
				print("Okey, and how many buildings do you want to build?(price for one house - 50 and you have", s2, ")")
				a2 = int(input())
				if s2 > 50 * a2:
					d2[a] = d2[a] + a2
					print("Okey, now on the", streets[a], "you have", d2[a], "buildings\n")
					s2 = s2 - a * 50
				else:
					print("You haven't got some money for this operation\n")


	elif streets[k2] == 'Visiting Jail':
		print("You are on the Jail, but only for visiting")

		print("You have:", p2, "and on this streets you have:", d2, "buildings")
		if len(p2) != 0:
			print("Do you want to biuld some houses on your streets?")
			c2 = input()
			if c2 == 'y':
				print("On what streets you wan to build?")
				str_number = input()
				while not str_number.isdigit():
					print("Please, enter the digit")
					str_number = input()
				a = int(str_number) - 1
				print("Okey, and how many buildings do you want to build?(price for one house - 50 and you have", s2, ")")
				a2 = int(input())
				if s2 > 50 * a2:
					d2[a] = d2[a] + a2
					print("Okey, now on the", streets[a], "you have", d2[a], "buildings\n")
					s2 = s2 - a * 50
				else:
					print("You haven't got some money for this operation\n")


	elif streets[k2] == 'Go To Jail':
		print("You are going to jail, you should pay 100")
		s2 = s2 -100
		k2 = 8
		print("You budget is", s2, "\n")
		print("You have:", p2, "and on this streets you have:", d2, "buildings")


	elif streets[k2] == 'Electric Company' and streets[k2] in p1 or streets[k2] == 'Water Warks' and streets[k2] in p1:
		print("You are on the komercial company and you should throw cubes and pay for the first player 10x sum\n")
		print("Throw cubes:(y)\n")
		c4 = input()
		if c4 == 'y':
			c = rand(t)
			print("The numbers on the cubes:", c, "\n")
			print("You should pay", 10 * c, "for the first player\n")
			s2 = s2 - 10 * c
			s1 = s1 + 10 * c
			print("You budget is", s2, "\n")


	elif streets[k2] == 'Luxury Tax':
		print("You hit the field Luxury Tax, pay 200")
		s2 = s2 - 200
		print("You budget is", s2, "\n")

		print("You have:", p2, "and on this streets you have:", d2, "buildings")
		if len(p2) != 0:
			print("Do you want to biuld some houses on your streets?")
			c2 = input()
			if c2 == 'y':
				print("On what streets you wan to build?")
				str_number = input()
				while not str_number.isdigit():
					print("Please, enter the digit")
					str_number = input()
				a = int(str_number) - 1
				print("Okey, and how many buildings do you want to build?(price for one house - 50 and you have", s2, ")")
				a2 = int(input())
				if s2 > 50 * a2:
					d2[a] = d2[a] + a2
					print("Okey, now on the", streets[a], "you have", d2[a], "buildings\n")
					s2 = s2 - a * 50
				else:
					print("You haven't got some money for this operation\n")


	elif streets[k2] in p1:
		print(streets[k2], "is property of player 1. You should pay 50 to the first player")
		s1 = s1 + 50
		s2 = s2 = 50
		print("You budget is", s2, "\n")

		print("You have:", p2, "and on this streets you have:", d2, "buildings")
		if len(p2) != 0:
			print("Do you want to biuld some houses on your streets?")
			c2 = input()
			if c2 == 'y':
				print("On what streets you wan to build?")
				str_number = input()
				while not str_number.isdigit():
					print("Please, enter the digit")
					str_number = input()
				a = int(str_number) - 1
				print("Okey, and how many buildings do you want to build?(price for one house - 50 and you have", s2, ")")
				a2 = int(input())
				if s2 > 50 * a2:
					d2[a] = d2[a] + a2
					print("Okey, now on the", streets[a], "you have", d2[a], "buildings\n")
					s2 = s2 - a * 50
				else:
					print("You haven't got some money for this operation\n")






if s1 < 0:
	print("Player 1 lose")
if s2 < 0:
	print("Player 2 lose")