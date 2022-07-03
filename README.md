# Autonomous-Robot-Path-Planning-Using-A-star-RRT-and-RRT-star
A Demonstration with Visualisation/GUI for Robot Path Planning Algorithms like A*, RRT, &amp; RRT*
<br><br>
Here, I implement and simulate/visualize the A*, RRT, and RRT* algorithms using Python and Pygame. To be able to run, execute and visualize the output of the code, you would need to have an installation of Python 3 (>= 3.8) and Pygame (>= 2.1) on your system.
<br><br>
<h3>The A* Algorithm</h3>
The A* Algorithm is a search algorithm to give optimal paths from a known starting position to a known goal. It uses two heuristic costs, the g-cost (cost/distance of a point/node from the starting point) and the h-cost (estimated cost/distance to the goal from the current node), which sum up to give the f-cost. The idea is to choose trajectory nodes which minimises the f-cost for each node throughout the path. To estimate the h-cost, I used the Euclidean/L2 distance from the current node to goal (though Manhattan/L1 distance can also be used in some cases). An example of an instance for using A* to find the optimal trajectory can be seen in the animation below (other similar animations can be produced by running my code).
![a_star](https://user-images.githubusercontent.com/56220919/177034638-0c80da2a-630d-4da1-94ef-a43d3845e7e9.gif)
The colour coding can be understood as:
<ul><li>White: Empty/unoccupied grid cells (and) unexplored areas
<li>Black: Obstacles in the grid world
<li>Orange: Start node (or) target/goal node
<li>Green: Open Nodes which have been partially explored
<li>Red: Closed nodes which have completely been explored
<li>Blue: Nodes which are a part of the final and optimal trajectory</ul>
To exexute the code, run the following command

    python3 a_star.py
Once the animation window opens, do the following:
<ul><li> Click any grid cell (except obstacles) to mark the start node
<li>Click on another grid cell (except obstacles) to mark the target/goal node
<li>Click on the space key to start the A* Simulation.</ul>
For an exact background for my implmentation, you can take a look at the pseudocode given in <a href="https://www.youtube.com/watch?v=-L-WgKMFuhE">this</a> video by Sebastian Lague.
<h3>The RRT Algorithm</h3>
The RRT Algorithm is a sampling based algorithm that finds sub-optimal trajectories/paths from a known starting position to an unknown goal position in a computationally efficient way (at least compared to A*). The below visualization shows the use of RRT to navigate from a user-specified start position to a user-specified goal in a pre-developed continous map with rectangular and circular obstacles. Note that this implementation runs only till an intial ![rrt](https://user-images.githubusercontent.com/56220919/177034782-a5f09cb5-8fc5-4214-a39f-dd2ce7eeb5c9.gif)
path is found (i.e. just to demonstrate the algorithm).
![rrt](https://user-images.githubusercontent.com/56220919/177034700-9821c1d5-0413-497b-a032-525e6f73c7f6.gif)
The colour coding can be understood as:
<ul><li>White: Empty/Non-obstacle areas which are unexplored
<li>Black: Rectangular and circular obstacles
<li>Orange: Start node (or) target/goal node
<li>Green: Trajectory indicating path found by RRT
<li>Red: Nodes added to the world
<li>Blue: Connection between parent and child nodes</ul>
To exexute the code, run the following command

    python3 rrt.py
Once the animation window opens, do the following:
<ul><li> Click any area (except obstacles) to mark the start node
<li>Click on another point (except obstacles) to mark the target/goal node
<li>Click on the space key to start the RRT Simulation.</ul>
Note that when running the RRT* code, you can change the map being used by changing the <i>MAP_TYPE</i> variable in <i>rrt.py</i> from 0 to 1 or vice-versa.
<h3>The RRT* Algorithm</h3>
The RRT* Algorithm which I have implemented is very similar to the RRT algorithm except for two changes. They include:
<ul><li>Choosing a proximal node with reduced distance based cost as the parent of a newly added node (over the nearest node as the parent).
<li>Rewiring nodes (parent-children connections) in a fixed vicinity of a newly added node to reduce the cost of each node in that neighbourhood.</ul>
Exact details regarding changes made on top of RRT to get RRT* can be found in <a href="https://theclassytim.medium.com/robotic-path-planning-rrt-and-rrt-212319121378">this</a> Medium article by Tim Chinenov. The RRT* Algorithm is simulated below. Note that even once a path is found, it keeps funning, looking for more optimal paths (can be seen with another green line appearing towards the end of the animation).
![rrt_star](https://user-images.githubusercontent.com/56220919/177034717-7f660756-4450-42ae-a049-f0f8ef793302.gif)
The colour coding can be understood as:
<ul><li>White: Empty/Non-obstacle areas which are unexplored
<li>Black: Rectangular and circular obstacles
<li>Orange: Start node (or) target/goal node
<li>Green: Trajectory indicating path found by RRT*
<li>Red: Nodes added to the world
<li>Blue: Connection between parent and child nodes</ul>
To exexute the code, run the following command

    python3 rrt_star.py
Once the animation window opens, do the following:
<ul><li> Click any area (except obstacles) to mark the start node
<li>Click on another point (except obstacles) to mark the target/goal node
<li>Click on the space key to start the RRT* Simulation.</ul>
Note that when running the RRT* code, you can change the map being used by changing the <i>MAP_TYPE</i> variable in <i>rrt_star</i> from 0 to 1 or vice-versa.
<h4>Key Observations and Thoughts</h4>
<ul>
<li>Even though A* produces optimal paths, it is computationally expensive to run, especially for higher dimenional spaces. For a 2D grid world though, it runs fast and well.
<li>RRT searches a majority of the entire world pretty fast, but struggles to quickly reach within the goal radius to complete running. A compbination of RRT with a heuristic/estimate of where the goal could be could attempt to solve this issue.
<li>RRT* produces much straighter paths (and thus eventually more optimal) than RRT. However, it takes longer to run because of steps like the rewiring of nodes.
</ul>
