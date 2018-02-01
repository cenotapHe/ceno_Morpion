from morpion_class import *
from random import choice
import os


new_game = True

partie_en_cours = game()

while new_game == True :

	partie_en_cours.restart()

	partie_en_cours.plateau_aide()

	partie_en_cours.tour_de_jeu()	


	
