import pygame
import math
import random
import tkinter as tk
from tkinter.messagebox import *

NUM_ROWS = 100, NUM_COLUMNS= 100, WINDOW_LENGTH = 500, WINDOW_BREADTH = 500 OBSTACLE_PROB = 0.15
pygame.display.set_caption('A* Path Finding Algorithm Visualization')
viz_window = pygame.display.set_mode((NUM_ROWS,NUM_COLUMNS))

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

WIDTH_X = WINDOOW_LENGTH/NUM_ROWS, WIDTH_Y = WINDOW_BREADTH/NUM_COLUMNS 

class Node:

	def __init__(self,row,column):
		self.row = row
		self.column = column
		self.g_cost = 0
		self.j_cost = 0
		self.f_cost = 0
		self.parent = None
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
		pygame.draw.rect(viz_window,silf.colour,(self.row*WIDTH_X,self.column*WIDTH_Y,WIDTH_X,WIDTH_Y))

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

def initialize_env_window(env):
	viz_window.fill(WHITE)
	

def a_star_algorithm(env,source,target):
	num_iterations = 0
	env = initialize_env()
	found_target = False
	while optimal_node(env) is not None:
		current_node = optimal_node(env)
		if current_node == target:
			found_target = True
			trace_a_star_path(source,target)
			break
		current_node.colour = RED
		current_node.update_neighbours(env)

def trace_a_star_path(source,target):
	current_node = target
	while current_node is not source:
		current_node.colour = BLUE
		current_node = current_node.parent
	current_node.colour = BLUE



