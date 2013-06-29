import numpy
import random

test_mat = [[0,6,0,5,9,3,0,0,0],[9,0,1,0,0,0,5,0,0],[0,3,0,4,0,0,0,9,0],
[1,0,8,0,2,0,0,0,4],[4,0,0,3,0,9,0,0,1],[2,0,0,0,1,0,6,0,9],[0,8,0,0,0,6,0,2,0],
[0,0,4,0,0,0,8,0,7],[0,0,0,7,8,5,0,1,0]]

aim_mat = [[8,0,0,0,0,0,0,0,0],[0,0,3,6,0,0,0,0,0],[0,7,0,0,9,0,2,0,0],
[0,5,0,0,0,7,0,0,0],[0,0,0,0,4,5,7,0,0],[0,0,0,1,0,0,0,3,0],[0,0,1,0,0,0,0,6,8],
[0,0,8,5,0,0,0,1,0],[0,9,0,0,0,0,4,0,0]]

test_mat2 = [[0,0,0,2,0,0,9,8,0],[9,8,1,3,0,6,0,5,0],[0,4,7,0,0,5,0,3,0],
[7,0,8,0,0,9,2,0,0],[0,0,0,0,2,0,0,0,0],[0,0,5,4,0,0,6,0,1],[0,3,0,7,0,0,8,6,0],
[0,7,0,8,0,1,4,2,5],[0,5,2,0,0,4,0,0,0]]

hard_mat = [[1,0,0,0,0,0,0,0,8],[0,0,7,8,0,6,4,0,0],[0,8,0,3,0,0,0,1,0],
[0,1,9,0,0,2,0,0,6],[0,0,8,0,0,0,2,0,0],[0,2,4,0,0,3,7,0,1],[0,9,0,0,0,0,0,6,0],
[7,0,0,0,6,0,0,0,4],[0,0,2,0,5,4,1,0,0]]


def cube_remove(smat,i,j,index_i,index_j):
	"""
	performing the cube section of the sudoku transform
	"""
	for x in range(i-3, i):
		for y in range(j-3, j):
			if smat[x][y] in smat[index_i][index_j]:
				smat[index_i][index_j].remove(smat[x][y])

def sudoku_trans(smat):
	"""
	transforms the smat
	"""
	
	s_num = [1,2,3,4,5,6,7,8,9]
	v_num = [1,2,3,4,5,6,7,8,9]
	for i in range(9):
		for j in range(9):
			if smat[i][j] == 0:
				smat[i][j] = [1,2,3,4,5,6,7,8,9]
				
	low = [0,1,2]
	mid = [3,4,5]
	high = [6,7,8]

	for i in range(9):
		for j in range(9):
			if smat[i][j] not in s_num:
				for ii in range(9):
					if smat[ii][j] in smat[i][j]:
						smat[i][j].remove(smat[ii][j])
				for jj in range(9):
					if smat[i][jj] in smat[i][j]:
						smat[i][j].remove(smat[i][jj])
	
				if i in low:
					if j in low:
						cube_remove(smat,3,3,i,j)
					if j in mid:
						cube_remove(smat,3,6,i,j)
					if j in high:
						cube_remove(smat,3,9,i,j)
				if i in mid:
					if j in low:
						cube_remove(smat,6,3,i,j)
					if j in mid:
						cube_remove(smat,6,6,i,j)
					if j in high:
						cube_remove(smat,6,9,i,j)
				if i in high:
					if j in low:
						cube_remove(smat,9,3,i,j)
					if j in mid:
						cube_remove(smat,9,6,i,j)
					if j in high:
						cube_remove(smat,9,9,i,j)


	
def sol_dict(smat):
	cells = {}
	# Creating cells with keys as matrix index, values as the possible solution at the cell.
	for i in range(9):
		for j in range(9):
			if type(smat[i][j]) is list:
				cells[(i,j)] = len(smat[i][j])				
	return cells

def sudoku_cross(smat):
	"""
	Crosshatching method
	"""
	# Horizontal cross-hatching
	for i in range(9):
		whole_list = []
		for element in smat[i]:
			if type(element) is list:
				whole_list += element
		certain_num = [elem for elem in whole_list if whole_list.count(elem) == 1]
		for num in certain_num:
			for j in range(9):
				if type(smat[i][j]) is list:
					if num in smat[i][j]:
						smat[i][j] = num
						sudoku_trans(smat)
	### print "horizontal cross-hatching"
					
	# Vertical cross-hatching
	for j in range(9):
		whole_list = []
		for i in range(9):
			if type(smat[i][j]) is list:
				whole_list += smat[i][j]
		certain_num = [elem for elem in whole_list if whole_list.count(elem) == 1]
		for num in certain_num:
			for i in range(9):
				if type(smat[i][j]) is list:
					if num in smat[i][j]:
						smat[i][j] = num
						sudoku_trans(smat)
	### print "vertical cross-hatching"
				
	# Cube cross-hatching
	# low-low
	whole_list = []
	for i in range(0,3):
		for j in range(0,3):
			if type(smat[i][j]) is list:
				whole_list += smat[i][j]
	certain_num = [elem for elem in whole_list if whole_list.count(elem) == 1]
	for num in certain_num:
		for i in range(0,3):
			for j in range(0,3):
				if type(smat[i][j]) is list:
					if num in smat[i][j]:
						smat[i][j] = num
						sudoku_trans(smat)
	
	# low-mid
	whole_list = []
	for i in range(0,3):
		for j in range(3,6):
			if type(smat[i][j]) is list:
				whole_list += smat[i][j]
	certain_num = [elem for elem in whole_list if whole_list.count(elem) == 1]
	for num in certain_num:
		for i in range(0,3):
			for j in range(3,6):
				if type(smat[i][j]) is list:
					if num in smat[i][j]:
						smat[i][j] = num
						sudoku_trans(smat)
	# low-high
	whole_list = []
	for i in range(0,3):
		for j in range(6,9):
			if type(smat[i][j]) is list:
				whole_list += smat[i][j]
	certain_num = [elem for elem in whole_list if whole_list.count(elem) == 1]
	for num in certain_num:
		for i in range(0,3):
			for j in range(6,9):
				if type(smat[i][j]) is list:
					if num in smat[i][j]:
						smat[i][j] = num
						sudoku_trans(smat)
	# mid-low
	whole_list = []
	for i in range(3,6):
		for j in range(0,3):
			if type(smat[i][j]) is list:
				whole_list += smat[i][j]
	certain_num = [elem for elem in whole_list if whole_list.count(elem) == 1]
	for num in certain_num:
		for i in range(3,6):
			for j in range(0,3):
				if type(smat[i][j]) is list:
					if num in smat[i][j]:
						smat[i][j] = num
						sudoku_trans(smat)
	# mid-mid
	whole_list = []
	for i in range(3,6):
		for j in range(3,6):
			if type(smat[i][j]) is list:
				whole_list += smat[i][j]
	certain_num = [elem for elem in whole_list if whole_list.count(elem) == 1]
	for num in certain_num:
		for i in range(3,6):
			for j in range(3,6):
				if type(smat[i][j]) is list:
					if num in smat[i][j]:
						smat[i][j] = num
						sudoku_trans(smat)
	# mid-high
	whole_list = []
	for i in range(3,6):
		for j in range(6,9):
			if type(smat[i][j]) is list:
				whole_list += smat[i][j]
	certain_num = [elem for elem in whole_list if whole_list.count(elem) == 1]
	for num in certain_num:
		for i in range(3,6):
			for j in range(6,9):
				if type(smat[i][j]) is list:
					if num in smat[i][j]:
						smat[i][j] = num
						sudoku_trans(smat)
	# high-low
	whole_list = []
	for i in range(6,9):
		for j in range(0,3):
			if type(smat[i][j]) is list:
				whole_list += smat[i][j]
	certain_num = [elem for elem in whole_list if whole_list.count(elem) == 1]
	for num in certain_num:
		for i in range(6,9):
			for j in range(0,3):
				if type(smat[i][j]) is list:
					if num in smat[i][j]:
						smat[i][j] = num
						sudoku_trans(smat)
	# high-mid
	whole_list = []
	for i in range(6,9):
		for j in range(3,6):
			if type(smat[i][j]) is list:
				whole_list += smat[i][j]
	certain_num = [elem for elem in whole_list if whole_list.count(elem) == 1]
	for num in certain_num:
		for i in range(6,9):
			for j in range(3,6):
				if type(smat[i][j]) is list:
					if num in smat[i][j]:
						smat[i][j] = num
						sudoku_trans(smat)
	# high-high
	whole_list = []
	for i in range(6,9):
		for j in range(6,9):
			if type(smat[i][j]) is list:
				whole_list += smat[i][j]
	certain_num = [elem for elem in whole_list if whole_list.count(elem) == 1]
	for num in certain_num:
		for i in range(6,9):
			for j in range(6,9):
				if type(smat[i][j]) is list:
					if num in smat[i][j]:
						smat[i][j] = num
						sudoku_trans(smat)

def sudoku_filling(smat):
	"""
	Solves the sudoku using transformed sudoku
	"""
	
	cells = sol_dict(smat)	
	
	while len(cells) > 0:
		if min(cells.values()) > 1:
			break
		cur_index = min(cells, key = cells.get)
		sudoku_fill(smat, cur_index)
		del cells[cur_index]
		sudoku_trans(smat)
		cells = sol_dict(smat)
	
	num_of_cells = len(cells)
	
	return num_of_cells	
	
def sudoku_fill(smat, index):
	"""
	fills the smat at the location pointed to by the input index
	ALTHOUGH I USED RANDOM.CHOICE, THIS METHOD DOES NOT INCLUDE GUESSING
	"""
	value = random.choice(smat[index[0]][index[1]])
	smat[index[0]][index[1]] = value

def sudoku_solver(smat):
	"""
	solves the input sudoku
	"""
	uncertain_cells = 0
	while True:
		sudoku_trans(smat)
		sudoku_cross(smat)
		cur_uncertain_cells = sudoku_filling(smat)
		if uncertain_cells == cur_uncertain_cells:
			break
		elif uncertain_cells != cur_uncertain_cells:
			uncertain_cells = cur_uncertain_cells
	
	if cur_uncertain_cells != 0:
		print "warning:", "There are %s unfilled cells left." % cur_uncertain_cells
	
	return smat

