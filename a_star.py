import pygame
import math
import random
import tkinter as tk
from tkinter.messagebox import *

NUM_ROWS = 100, NUM_COLUMNS= 100, WINDOW_LENGTH = 500, WINDOW_BREADTH = 500 OBSTACLE_PROB = 0.3
pygame.display.set_caption('A* Path Finding Algorithm Visualization')
viz_window = pygame.display.set_mode((NUM_ROWS,NUM_COLUMNS))

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
ORANGE = (255,164.5,0)
GREY = (127.5,127.5,127.5)

WIDTH_X = WINDOOW_LENGTH/NUM_ROWS, WIDTH_Y = WINDOW_BREADTH/NUM_COLUMNS 

class Node:

	def __init__(self,row,column):
		self.row = row
		self.column = column
		self.g_cost = 0
		self.j_cost = 0
		self.f_cost = 0
		self.parent = None
		self.start_node = False
		self.target_node = False
		if random.random() < OBSTACLE_PROB:
			self.colour = BLACK
		else:
			self.colour = WHITE

	def set_h_cost(self,target_coord):
		x,y = target_coord
		self.h_cost = math.sqrt((self.row-x)**2+(self.column-y)**2)
		self.f_cost = self.g_cost + self.h_cost

	def update_node_if_needed(self,parent):
		new_f_cost = parent.g_cost + math.sqrt((self.row-parent.row)**2+(self.column-parent.column)**2) + self.h_cost
		if (self.colour == GREEN and self.f_cost >= new_f_cost) or self.colour == WHITE:
			self.g_cost = parent.g_cost + math.sqrt((self.row-parent.row)**2+(self.column-parent.column)**2)
			self.f_cost = self.g_cost + self.h_cost
			self.parent = new_parent
			self.colour = GREEN

	def update_neighbours(self,env,open_nodes_set):
		if self.row > 0:
			self.update_node_if_needed(env[self.row-1][self.column],self)
			if self.column > 0:
				self.update_node_if_needed(env[self.row][self.column-1],self)
				self.update_node_if_needed(env[self.row-1][self.column-1],self)
			if self.column < NUM_COLUMNS-1:
				self.update_node_if_needed(env[self.row][self.column+1],self)
				self.update_node_if_needed(env[self.row-1][self.column+1],self)
		if self.row < NUM_ROWS-1:
			self.update_node_if_needed(env[self.row+1][self.column],self)
			if self.column > 0:
				self.update_node_if_needed(env[self.row+1][self.column-1],self)
			if self.column < NUM_COLUMNS-1:
				self.update_node_if_needed(env[self.row+1][self.column+1],self)

	def visualize_node(self):
		colour = self.colour
		if self.start_node or self.target_node:
			colour = ORANGE
		pygame.draw.rect(viz_window,colour,(self.row*WIDTH_X,self.column*WIDTH_Y,WIDTH_X,WIDTH_Y))

def set_env_h_costs(env,target_node):
	x = target_node.row, y = target_node.column
	for row in NUM_ROWS:
		for column in NUM_COLUMNS:
			env[row][column].set_h_cost((x,y))

def optimal_node(env):
	lowest_f_cost = 1e7, lowest_h_cost = 1e7, optimal_node = None
	for i in range(len(env)):
		for j in range(len(env[0])):
			if env[i][j].colour == GREEN and (env[i][j].f_cost < lowest_f_cost or (env[i][j].f_cost == lowest_f_cost and env[i][j].h_cost < lowest_h_cost)):
				optimal_node = env[i][j]
				lowest_f_cost = optimal_node.f_cost
				lowest_h_cost = optimal_node.h_cost
	return optimal_node

def initialize_env():
	env = []
	for i in range(NUM_ROWS):
		env.append([])
		for j in range(NUM_COLUMNS):
			env[-1].append(Node(i,j))

def visualize_env_window(viz_window,env):
	viz_window.fill(WHITE)
	for row in range(NUM_ROWS):
		for column in range(NUM_COLUMNS):
			env[row][column].visualize_node()
	for row in range(NUM_ROWS):
		pygame.draw.line(viz_window,GREY,(0,row*WIDTH_X),(WIDTH_X,row*WIDTH_X))
		pygame.draw.line(viz_window,GREY,(row*WIDTH_Y,0),(row*WIDTH_Y,WIDTH_Y))
	pygame.display.update()

def identify_user_clicked_node(coord,env):
	return env[coord[0]//WIDTH_X][coord[1]//WIDTH_Y]

def a_star_algorithm(viz_window,env,start_node,target_node):
	num_iterations = 0
	env = initialize_env()
	found_target = False
	start_node.colour = GREEN
	while optimal_node(env) is not None:
		for event in pygame.event.get():
			if event.type = pygame.QUIT:
				pygame.quit()
		current_node = optimal_node(env)
		if current_node == target_node:
			found_target = True
			trace_a_star_path(start_node,target_node)
			visualize_env_window(viz_window,env)
			break
		current_node.colour = RED
		current_node.update_neighbours(env)
		visualize_env_window(viz_window,env)

def trace_a_star_path(start_node,target_node):
	current_node = target
	while current_node is not source:
		current_node.colour = BLUE
		current_node = current_node.parent
	current_node.colour = BLUE

env = initialize_env()
execute = True
start_node = None, target_node = None

while execute:
	visualize_env_window(env)
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
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and start_node and target_node:
					a_star_algorithm(env,start_node,target_node)
				if event.key == pygame.K_c:
					start_node = None
					target_node = None
					env = initialize_env()








