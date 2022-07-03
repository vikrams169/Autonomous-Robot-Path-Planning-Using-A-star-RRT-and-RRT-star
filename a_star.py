# Demonstration and Visualization of the A* Algorithm a 2D Grid World
# Compatible with Python 3.8.1 and pygame 2.1.2

# Importing the Required Libraries
import pygame
import math
import random

# Information for saving the animation frames
dir_name = "a_star_frames"
frame_number = 0

# Initializing variables defining the grid world
# Can be varied as per convenience and grid world specifications
NUM_ROWS = 100							# Number of rows in the grid world
NUM_COLUMNS = 100						# Number of columns in the grid world
WINDOW_LENGTH = 1000					# Length of the grid world along the X-axis
WINDOW_BREADTH = 1000					# Length of the grid world along the Y-axis
WIDTH_X = WINDOW_LENGTH/NUM_ROWS  		# Length of an individual cell along the X-axis
WIDTH_Y = WINDOW_BREADTH/NUM_COLUMNS  	# Length of an individual cell along the Y-axis
OBSTACLE_PROB = 0.3						# Setting a threshold to control the obstacle density in the grid world

# Defining colour values across the RGB Scale
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
ORANGE = (255,164.5,0)

# A class to define the characteristics of each grid cell (generalized to each discrete data point in a robotic configuration space)
class Node:

	def __init__(self,row,column):
		self.row = row
		self.column = column
		self.g_cost = 0
		self.h_cost = 0
		self.f_cost = 0
		self.parent = None
		self.start_node = False
		self.target_node = False
		if random.random() < OBSTACLE_PROB:
			self.colour = BLACK
		else:
			self.colour = WHITE

	# Initilaizing the h cost (won't change throughout the algorithm) for the node based on L2 distance from the target node
	def set_h_cost(self,target_coord):
		x,y = target_coord
		self.h_cost = math.sqrt((self.row-x)**2+(self.column-y)**2)
		self.f_cost = self.g_cost + self.h_cost

	# Updating the g cost & f cost of a node only if it meets the criteria of the A* Algorithm
	def update_node_if_needed(self,parent):
		new_f_cost = parent.g_cost + math.sqrt((self.row-parent.row)**2+(self.column-parent.column)**2) + self.h_cost
		if (self.colour == GREEN and self.f_cost >= new_f_cost) or self.colour == WHITE:
			self.g_cost = parent.g_cost + math.sqrt((self.row-parent.row)**2+(self.column-parent.column)**2)
			self.f_cost = self.g_cost + self.h_cost
			self.parent = parent
			self.colour = GREEN

	# Updating the g & f cost values of the neighbours of a current node being processed
	def update_neighbours(self,env):
		if self.row > 0:
			env[self.row-1][self.column].update_node_if_needed(self)
			if self.column > 0:
				env[self.row][self.column-1].update_node_if_needed(self)
				env[self.row-1][self.column-1].update_node_if_needed(self)
			if self.column < NUM_COLUMNS-1:
				env[self.row][self.column+1].update_node_if_needed(self)
				env[self.row-1][self.column+1].update_node_if_needed(self)
		if self.row < NUM_ROWS-1:
			env[self.row+1][self.column].update_node_if_needed(self)
			if self.column > 0:
				env[self.row+1][self.column-1].update_node_if_needed(self)
			if self.column < NUM_COLUMNS-1:
				env[self.row+1][self.column+1].update_node_if_needed(self)

	# Colouring a node for visualization processes in pygame
	def visualize_node(self):
		colour = self.colour
		if self.start_node or self.target_node:
			colour = ORANGE
		pygame.draw.rect(viz_window,colour,(self.row*WIDTH_X,self.column*WIDTH_Y,WIDTH_X,WIDTH_Y))

# Initializing the environment/grid world
def initialize_env():
	env = []
	for i in range(NUM_ROWS):
		env.append([])
		for j in range(NUM_COLUMNS):
			env[-1].append(Node(i,j))
	return env

# A function to update the displayed grid world after each iteration of the A* Algorithm
def visualize_env_window(viz_window,env):
	global frame_number
	viz_window.fill(WHITE)
	for row in range(NUM_ROWS):
		for column in range(NUM_COLUMNS):
			env[row][column].visualize_node()
	pygame.display.update()
	pygame.image.save(viz_window,dir_name+"/frame"+str(frame_number)+".jpg")
	frame_number += 1

# Identifying the node/grid cell that the user clicks on (as either the source or target)
def identify_user_clicked_node(coord,env):
	return env[int(coord[0]//WIDTH_X)][int(coord[1]//WIDTH_Y)]

# Setting the initial h costs for all the cells in the grid
def set_env_h_costs(env,target_node):
	x = target_node.row
	y = target_node.column
	for row in range(NUM_ROWS):
		for column in range(NUM_COLUMNS):
			env[row][column].set_h_cost((x,y))

# Returning the node with lowest f cost (and lowest h cost in case of multiple such nodes) from the open set (of green colour)
def optimal_node(env):
	lowest_f_cost = 1e7
	lowest_h_cost = 1e7
	optimal_node = None
	for i in range(len(env)):
		for j in range(len(env[0])):
			if env[i][j].colour == GREEN and (env[i][j].f_cost < lowest_f_cost or (env[i][j].f_cost == lowest_f_cost and env[i][j].h_cost < lowest_h_cost)):
				optimal_node = env[i][j]
				lowest_f_cost = optimal_node.f_cost
				lowest_h_cost = optimal_node.h_cost
	return optimal_node

# Tracing the final shortest and optimal path in blue after A* completes running
def trace_a_star_path(start_node,target_node):
	current_node = target_node
	while current_node is not start_node:
		current_node.colour = BLUE
		current_node = current_node.parent
	current_node.colour = BLUE

# A* Algorithm
def a_star_algorithm(viz_window,env,start_node,target_node):
	num_iterations = 0
	found_target = False
	start_node.colour = GREEN
	while optimal_node(env) is not None:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
		current_node = optimal_node(env)
		if current_node == target_node:
			found_target = True
			trace_a_star_path(start_node,target_node)
			visualize_env_window(viz_window,env)
			break
		current_node.colour = RED
		current_node.update_neighbours(env)
		num_iterations += 1
		visualize_env_window(viz_window,env)

# Initializing the grid world as a pygame display window
pygame.display.set_caption('A* Path Finding Algorithm Visualization')
viz_window = pygame.display.set_mode((WINDOW_LENGTH,WINDOW_BREADTH))

# Initializing the environment/grid world, and setting conditions/breaks
env = initialize_env()
execute = True
start_node = None
target_node = None

# Running the algorithm from user clicking till completion
while execute:
	visualize_env_window(viz_window,env)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			execute = False
		elif pygame.mouse.get_pressed()[0]:
			node = identify_user_clicked_node(pygame.mouse.get_pos(),env)
			if not start_node and node!=target_node:
				node.start_node =True
				start_node = node
				node.visualize_node()
			elif not target_node and node!=start_node:
				node.target_node =True
				target_node = node
				set_env_h_costs(env,target_node)
				node.visualize_node()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE and start_node and target_node:
				a_star_algorithm(viz_window,env,start_node,target_node)
			if event.key == pygame.K_c:
				start_node = None
				target_node = None
				env = initialize_env()