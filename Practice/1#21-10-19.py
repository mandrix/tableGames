from random import shuffle

class Card(object):
	"""
	Card handling class
	"""
	def __init__(self, number, pille):
		self.number = number
		self.pille = pille
		self.valor = number

	def solvingValor(self):
		"""
		method for handling the final value of each card
		"""
		if self.number == "A":
			self.valor = 0
		elif type(self.number) != int:
			self.valor = 11



class Player(object):
	def __init__(self, roll):		
		self.roll = roll
		self.blackJack = []
		self.sum = 0
		self.win = True
		self.A = False


	def playCard(self, cards):
		
		Quest = "Player: {} wants one more card? Y/N. ".format(self.roll)
		if cards == 1:
			new = pille[-1]
			self.blackJack.append(new)
			self.showCards()
			pille.remove(new)
			self.sum += new.valor
			if new.number == "A":
				self.A = True
			self.playerState()
			
			if self.win:
				want = input(Quest)
				if want == "Y":
					self.playCard(1)
				else:
					self.playerState(True)
			else:
				print("Jugador ", self.roll , ": eliminado.")
		elif not cards:
			if self.win:
					want = input(Quest)
					if want == "Y": 
						self.playCard(1)
					else:
						self.playerState(True)
			else:
				print("Jugador ", self.roll , ": eliminado.")
		else:
			while cards:
				cards-=1
				new = pille[-1]
				pille.remove(new)
				self.blackJack.append(new)
				self.playerState()
				self.sum += new.valor
				if new.number == "A":
					self.A = True
		self.playerState()

	def playerState(self, final=False):
		if len(self.blackJack) > 5:
				self.win = False
		elif not self.A:
			if self.sum > 21:
				self.win = False
		else:
			if len(self.blackJack) == 5 or final:
				howManyA = self.blackJack.count("A")
				while self.sum < 21 and howManyA:
					howManyA-=1
					if self.sum + 11 > 21:
						self.sum += 1
					else:
						self.sum+=11
				if howManyA or self.sum > 21:
					self.win = False
	def showCards(self):
		for i in self.blackJack:
			print("Player {}: {} {}".format(self.roll, i.number, i.pille)  )


numbersTotals = ["A","J", "Q", "K"]
for i in range(2,10):
	numbersTotals.append(i)

pilleTotal = ["D", "H", "T", "P"]

pille = []

for i in numbersTotals:
	for j in pilleTotal:
		pille.append(Card(i,j))
		pille[-1].solvingValor()

shuffle(pille)
players = 4
playersTotal = []
while players <= 2:
	players = int(input("Playing with friends is much better !! \nNumber of player: "))

for i in range(players):
	playersTotal.append(Player(i+1))
	playersTotal[-1].playCard(2)

for i in playersTotal:
	i.showCards()
	i.playCard(0)
wins= []
for i in playersTotal:
	if i.win:
		wins.append(i)
maxi= 0
playerWin = []
for i in wins:
	if i.sum > maxi:
		maxi = i.sum
		playerWin.append(i.roll)
	elif i.sum == maxi: 
		playerWin.append(i.roll)
	elif i.sum == 21:
		playwin = [i.roll]
		break 
wins = "Player(s):"
if playerWin:
	for i in playerWin:
		wins+= str(i) + " ."

	wins+=" wins."

	print(wins)
else:
	print("This game had no winner")		





