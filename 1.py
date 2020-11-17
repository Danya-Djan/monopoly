import random
p1 = []
p2 = []
t = int
def rand(t): #функция выбора рандомного числа
	a = random.randint(1,6)
	b = random.randint(1,6)
	c = a + b
	return c
a = int
b = int
c = int
s1 = 500 #баланс первого игрока
s2 = 500 #баланс второго игрока
k1 = 0 #координата первого игрока
k2 = 0 #координата второго игрока
streets = ['Start', 'Mediterranean Avenue', 'Baltic Avenue', 'Income Tax', 'Reading Railroad', 'Oriental Avenue', 'Vermont Avenue', 'Connecticut Avenue', 'Visiting Jail', 'St. Charles Place', 'Electric Company', 'States Avenue', 'Virginia Avenuev', 'Pennsylvania Railroad', 'St. James Place', 'Tennessee Avenue', 'New York Avenue', 'Free Parking', 'Kentucky Avenue', 'Indiana Avenue', 'Illinois Avenue', 'B & O Railroad', 'Atlantic Avenue', 'Ventnor Avenue', 'Water Works', 'Marvin Gardens', 'Go To Jail', 'Pacific Avenue', 'North Carolina Avenue', 'Pennsylvania Avenue', 'Short Line', 'Park Place', 'Luxury Tax', 'Boardwalk']
prises = [0, 60, 60, 200, 200, 100, 100, 120, 0, 140, 150, 140, 160, 200, 180, 180, 200, 0, 200, 220, 240, 200, 260, 260, 250, 280, 0, 300, 300, 320, 200, 350, 100, 400]
#print(len(streets), len(prises))
print("Welcome ot Monopoly, let's start!")
while s1 > 0 and s2 > 0:
	if k1 > 33:
		k1 = k1 - 34
	if k2 > 33:
		k2 = k2 - 34





	print("The first player throws cube(y/n)")
	c1 = input()
	if c1 == 'y':
		c = rand(t)
		k1 = k1 + c
		if k1 > 33:
			k1 = k1 - 34
			s1 = s1 + 200
	else:
		print("ERROR")
	print("Your position is", k1)
	if streets[k1] != 'Start' and streets[k1] != 'Income Tax' and streets[k1] != 'Free Parking' and streets[k1] != 'Visiting Jail' and streets[k1] != 'Go To Jail' and streets[k1] != 'Luxury Tax' and streets[k1] not in p1 and streets[k1] not in p2:
		if s1 > prises[k1]:
			print("You budget is", s1,  ". Do you want to buy" , streets[k1],"?(y/n)")
			c1 = input()
			if c1 == 'y':
				p1.append(streets[k1])
				s1 = s1 - prises[k1]
				print("You budget after purchase:", s1)
				print("Your collection:", p1)
			else:
				print("Your collection:", p1)





	elif streets[k1] == 'Start':
		print("You passed the start field, get 200")
		s1 = s1 + 200
	elif streets[k1] == 'Income Tax':
		print("You hit the field Income Tax, pay 100")
		s1 = s1 - 100
	elif streets[k1] == 'Free Parking':
		print("You are on the Free Parking")
	elif streets[k1] == 'Visiting Jail':
		print("You are on the Jail, but only for visiting")
	elif streets[k1] == 'Go To Jail':
		print("You are going to jail")
		k1 = 8
	elif streets[k1] == 'Luxury Tax':
		print("You hit the field Luxury Tax, pay 200")
		s1 = s1 - 200
	elif streets[k1] in p2:
		print("You should pay 50 to the second player")
		s2 = s2 + 50
		s1 = s1 - 50



	





	print("The second player throws cube(y/n)")
	c2 = input()
	if c2 == 'y':
		c = rand(t)
		k2 = k2 + c
		if k2 > 33:
			k2 = k2 - 34
			s2 = s2 + 200
	else:
		print("ERROR")
		
	print("Your position is", k2)
	if streets[k2] != 'Start' and streets[k2] != 'Income Tax' and streets[k2] != 'Free Parking' and streets[k2] != 'Visiting Jail' and streets[k2] != 'Go To Jail' and streets[k2] != 'Luxury Tax' and streets[k1] not in p1 and streets[k1] not in p2:
		if s2 > prises[k2]:
			print("You budget is", s2,  ". Do you want to buy" , streets[k2],"?(y/n)")
			c2 = input()
			if c2 == 'y':
				p2.append(streets[k2])
				s2 = s2 - prises[k2]
				print("You budget after purchase:", s2)
				print("Your collection", p2)
			else:
				print("Your collection:", p2)




	elif streets[k2] == 'Start':
		print("You passed the start field, get 200")
		s2 = s2 + 200
	elif streets[k2] == 'Income Tax':
		print("You hit the field Income Tax, pay 100")
		s2 = s2 - 100
	elif streets[k2] == 'Free Parking':
		print("You are on the Free Parking")
	elif streets[k2] == 'Visiting Jail':
		print("You are on the Jail, but only for visiting")
	elif streets[k2] == 'Go To Jail':
		print("You are going to jail")
		k2 = 8
	elif streets[k2] == 'Luxury Tax':
		print("You hit the field Luxury Tax, pay 200")
		s2 = s2 - 200
	elif streets[k2] in p1:
		print("You should pay 50 to the first player")
		s1 = s1 + 50
		s2 = s2 = 50