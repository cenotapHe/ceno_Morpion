from random import choice
import os
import sys

class case():
	
	def __init__(self, x_case, y_case):
		self.x_case = x_case
		self.y_case = y_case
		self.affichage_case = " "

	def write_case(self, caractere):
		self.affichage_case = caractere

### class tqblequdejeu()

class game():

	def __init__(self):
		
		###self.tqblequ = tqblequdejeu()

		self.tableau = []

		i = 0
		j = 0

		while i < 3 :
			while j < 3 :
				self.tableau.append(case(j, i))
				j += 1
			j = 0
			i += 1


		player1 = self.init_player(1)
		player2 = self.init_player(2)

		self.joueur_en_cours = choice([player1, player2])

		if self.joueur_en_cours == player1:
			self.joueur_pas_en_cours = player2
		else :
			self.joueur_pas_en_cours = player1


	def restart(self):

		q = input("Q pour Quitter la partie. Sinon n'importe quelle autre touche.")
		q = str(q)
		q = q.upper()
		if q == "Q" :
			sys.exit(0)

		print("MORPION\nNOUVELLE PARTIE !\n")

		self.plateau_aide()

		self.tableau = []

		i = 0
		j = 0

		while i < 3 :
			while j < 3 :
				self.tableau.append(case(j, i))
				j += 1
			j = 0
			i += 1

		print("{} VERSUS {}\nLet's fight to the death !!!".format(self.joueur_pas_en_cours, self.joueur_en_cours))

		self.joueur_en_cours, self.joueur_pas_en_cours = self.joueur_pas_en_cours, self.joueur_en_cours		

		input("C'est {} qui debutera le Combat !!!".format(self.joueur_en_cours))	



	def plateau_aide(self):
		os.system("clear")
		print("              \n    1 | 2 | 3 ")
		print("   ___|___|___\n    4 | 5 | 6 ")
		print("   ___|___|___\n    7 | 8 | 9 ")
		print("      |   |   \n")


	def affichage_plateau(self):

		os.system("clear")
		print("              \n    {} | {} | {} ".format(self.tableau[0].affichage_case, self.tableau[1].affichage_case, self.tableau[2].affichage_case))
		print("   ___|___|___\n    {} | {} | {} ".format(self.tableau[3].affichage_case, self.tableau[4].affichage_case, self.tableau[5].affichage_case))
		print("   ___|___|___\n    {} | {} | {} ".format(self.tableau[6].affichage_case, self.tableau[7].affichage_case, self.tableau[8].affichage_case))
		print("      |   |   \n")


	def init_player(self, numero_du_joueur):

		i = False
		while i == False :
			player = input("Tapez le nom du joueur {}: ".format(numero_du_joueur))
			player = player.capitalize()
			if not player.isalnum() or len(player)<4 or len(player)>8:
				print("Stop faire le con tidesuite et donnes un vrai nom !")
			else:
				i = True
		return player


	def tour_de_jeu(self):

		i = 0

		case_deja_played = []
		case_played = 0

		self.symbole = "X"
		self.autre_symbole = "O"

		while i == 0 :

			while (case_played != "1") and (case_played != "2") and (case_played != "3") and (case_played != "4") and (case_played != "5") and (case_played != "6") and (case_played != "7") and (case_played != "8") and (case_played != "9") :
				case_played = input("C'est au tour de {} de jouer. Sur quelle case veux-tu jouer ?\n".format(self.joueur_en_cours))
				if case_played in case_deja_played :
					print("Cette case a deja ete jouee !!!")
					case_played = 0

			case_deja_played.append(case_played)
			case_played = int(case_played)
			self.tableau[case_played - 1].write_case(self.symbole)

		
			self.affichage_plateau()

			if (self.tableau[0].affichage_case == self.tableau[1].affichage_case == self.tableau[2].affichage_case != ' ') \
			or (self.tableau[3].affichage_case == self.tableau[4].affichage_case == self.tableau[5].affichage_case != ' ') \
			or (self.tableau[6].affichage_case == self.tableau[7].affichage_case == self.tableau[8].affichage_case != ' ') \
			or (self.tableau[0].affichage_case == self.tableau[3].affichage_case == self.tableau[6].affichage_case != ' ') \
			or (self.tableau[1].affichage_case == self.tableau[4].affichage_case == self.tableau[7].affichage_case != ' ') \
			or (self.tableau[2].affichage_case == self.tableau[5].affichage_case == self.tableau[8].affichage_case != ' ') \
			or (self.tableau[0].affichage_case == self.tableau[4].affichage_case == self.tableau[8].affichage_case != ' ') \
			or (self.tableau[2].affichage_case == self.tableau[4].affichage_case == self.tableau[6].affichage_case != ' ') :
				choice_case_1 = 2
				choice_case_2 = 2
				input("{} WIN THE GAME !\n".format(self.joueur_en_cours.upper()))
				break

			self.joueur_en_cours, self.joueur_pas_en_cours = self.joueur_pas_en_cours, self.joueur_en_cours
			self.symbole, self.autre_symbole = self.autre_symbole, self.symbole

			if len(case_deja_played) == 9 :
				input("DRAW !\n")
				break
