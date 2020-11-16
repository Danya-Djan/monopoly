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