import numpy as np
import pandas as pd
import os

def read_file(filename : str):
	with open(filename) as file: 
		data = file.readlines() 

		max_slices = data[0].replace('\n','').split(' ')[0]
		nb_diff_pizzas = data[0].replace('\n','').split(' ')[1]

		pizza_slices = data[1].replace('\n','').split(' ')

		pizza_slices_per_type = []
		for nb_slices in pizza_slices:
			pizza_slices_per_type.append(nb_slices)

		print(max_slices)
		print(nb_diff_pizzas)
		print(pizza_slices_per_type)

	return max_slices, nb_diff_pizzas, pizza_slices_per_type

def solve(max_slices : int, nb_diff_pizzas : int, pizza_slices_per_type : list):
	pass

def create_submission(nb_pizzas : int, pizza_nb_list : list, directory : str, output_file : str) -> None :
	filepath = os.path.join(directory, output_file)
	with open(filepath, 'w') as file:
		file.write("{}\n".format(nb_pizzas))
		for pizza_nb in pizza_nb_list:
			file.write("{} ".format(pizza_nb))	
		file.write("\n")
	pass


if __name__=='__main__':
	directory = "/home/tom/Desktop/hashcode/TestStatement"

	filename="a_example.in"

	max_slices, nb_diff_pizzas, pizza_slices_per_type = read_file(os.path.join(directory, filename))

	solve(max_slices, nb_diff_pizzas, pizza_slices_per_type)
	output_file = "submit_1.txt"

	create_submission(3, [0, 2, 3], directory = directory, output_file = output_file)
