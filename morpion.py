# Importation des classes pour le Morpion
from morpion_class import *

# Importation de la fonction qui permet de choisir un joueur aléatoirement
from random import choice
import os

# Initialisation du jeu
new_game = True

# Initialisation d'une nouvelle partie
partie_en_cours = game()

# Départ d'une nouvelle partie
while new_game == True :
	
	# Boucle permettant d'enchainer plusieurs parties, et de remettre le board a Zero

	partie_en_cours.restart()

	partie_en_cours.plateau_aide()

	partie_en_cours.tour_de_jeu()	


	
