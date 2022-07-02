import pygame
import math
import random

WINDOW_LENGTH = 1000					# Length of the grid world along the X-axis
WINDOW_BREADTH = 1000					# Length of the grid world along the Y-axis
NODE_RADIUS = 1
GOAL_RADIUS = 3
EPISOLON = 5

OBSTACLES = [{"rectangles":[(300,700,150,600),(700,500,250,100)],"circles":[(850,850,100)]},{"rectangles":[(700,850,100,900)],"circles"=[(350,350,200),(900,700,50)]}]
MAP_TYPE = 0

# Defining colour values across the RGB Scale
WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
ORANGE = (255,164.5,0)

# Initializing the grid world as a pygame display window,
pygame.display.set_caption('RRT Path Finding Algorithm Visualization')
viz_window = pygame.display.set_mode((WINDOW_LENGTH,WINDOW_BREADTH))

class Node:

	def __init__(self,coord,parent,start_node=False,target_node=False):
		self.x = coord[0]
		self.y = coord[1]
		self.parent = parent
		self.start_node = start_node
		self.target_node = target_node

	def visualize_node(self,viz_window):
		colour = RED
		if self.start_node or self.target_node:
			colour = ORANGE
		pygame.draw.circle(viz_window,colour,(self.x,self.y),NODE_RADIUS,width=0)

def target_reached(node,goal):
	node_x, node_y = node.x, node.y
	goal_x, goal_y = goal.x, goal.y
	if math.sqrt((node_x-goal_x)**2+(node_y-goal_y)) < GOAL_RADIUS:
		return True
	return False

def obstacle_collision(point,obstacle_list):
	for rect in obstacle_list["rectangles"]:
		if rect.collidepoint(point):
			return True
	for circle in obstacle_list["circles"]:
		if math.sqrt((point[0]-circle[0])**2+(point[1]-circle[1])**2) < circle[2]:
			return True
	return False

def add_new_node(viz_window,node_list,obstacle_list):
	while True:
		point = (random.random()*WINDOW_LENGTH,random.random()*WINDOW_BREADTH)//1
		nearest_node_dist = 1e7
		nearest_node = None
		for node in node_list:
			dist = math.sqrt((point[0]-node[0])**2+(point[1]-node[1])**2)
			if dist < nearest_node_dist:
				nearest_node_dist = dist
				nearest_node = node
		theta = math.atan2((point[1]-nearest_node[1])/(point[0]-nearest_node[0]))
		new_pos = (nearest_node.x+EPSILON*math.cos(theta),nearest_node.y+EPSILON*math.sin(theta))
		if not obstacle_collision(new_pos,obstacle_list):
			new_node = Node(new_pos,False,False)
			new_node.parent = nearest_node
			node_list.append(new_node)
			pygame.draw.line(viz_window,BLUE,(new_node.x,new_node.y),(new_node.parent.x,new_node.parent.y))
			return new_node,node_list

def initialize_obstacles(viz_window):
	obstacle_list = {"rectangles":[],"circles":[]}
	for rect in OBSTACLES[int(MAP_TYPE)]["rectangles"]:
		obtsacle_list["rectangles"].append(pygame.rect(rect)) 
		pygame.draw.rect(viz_window,BLACK,pygame.rect(rect))
	for circle in OBSTACLES[int(MAP_TYPE)]["circles"]:
		obstacle_list["circles"].append(circle)
		pygame.draw.circle(viz_window,BLACK,(circle[0],circle[1]),circle[2],width=0)
	return obstacle_list

def add_start_and_goal(viz_window,start_point,target_point):
	start_node = Node((start_point),True,False)
	start_node.visualize_node()
	target_node = Node((target_point),False,True)
	target_node.visualize_node()
	return start_node, target_node

def display_final_path(viz_window,goal_node):
	current_node = goal_node
	while not current_node.start_node:
		pygame.draw.line(viz_window,GREEN,(current_node.x,current_node.y),(current_node.parent.x,current_node.parent.y))

def rrt_algorithm(viz_window,start_node,goal_node,obstacle_list):
	node_list = []
	node_list.add(start_node)
	while True:
		new_node, node_list = add_new_node(viz_window,node_list,obstacle_list)
		if target_reached(new_node,goal_node):
			goal_node.parent = new_node
			nodes_list.add(goal_node)
			break
	display_final_path(viz_window,goal_node)
	pygame.display.update()

execute = True
start_node_found, target_node_found = False, False
start_pos, goal_pos = None, None
start_node, goal_node = None, None
obstacle_list = initiaize_obstacles(viz_window)
while execute:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			execute = False
		elif pygame.mouse.get_pressed()[0]:
			pos = pygame.mouse.get_pos()
			if not start_node_found:
				start_pos = pos
			elif not target_node_found:
				target_pos = pos
				start_node, goal_node = add_start_and_goal(viz_window,start_pos,target_pos)
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE and start_node and target_node:
				rrt_algorithm(viz_window,start_node,target_node)
			if event.key == pygame.K_c:
				start_node = None
				goal_node_node = None











