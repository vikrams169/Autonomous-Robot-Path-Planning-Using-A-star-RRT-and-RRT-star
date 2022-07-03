# Autonomous-Robot-Path-Planning-Using-A-star-RRT-and-RRT-star
A Demonstration with Visualisation/GUI for Robot Path Planning Algorithms like A*, RRT, &amp; RRT*
<br><br>
Here, I implement and simulate/visualize the A*, RRT, and RRT* algorithms using Python and Pygame. To be able to run, execute and visualize the output of the code, you would need to have an installation of Python 3 (>= 3.8) and Pygame (>= 2.1) on your system.
<br><br>
<h3>The A* Algorithm</h3>
The A* Algorithm is a search algorithm to give optimal paths from a known starting position to a known goal. It uses two heuristic costs, the g-cost (cost/distance of a point/node from the starting point) and the h-cost (estimated cost/distance to the goal from the current node), which sum up to give the f-cost. The idea is to choose trajectory nodes which minimise the f-cost throughout. To estimate the h-cost, I used the Euclidean/L2 distance from the current node to goal (though Manhattan/L1 distance can also be used in some cases). An example of an instance for using A* to find the optimal trajectory can be seen in the animation below (other similar animations can be produced by running my code).
<br><br>
![A-star](https://github.com/vikrams169/Autonomous-Robot-Path-Planning-Using-A-star-RRT-and-RRT-star/blob/main/animations/a_star.mp4)
<br><br>
For an exact background for my implmentation, you can take a look at the pseudocode given in <a href="https://www.youtube.com/watch?v=-L-WgKMFuhE">this</a> video by Sebastian Lague.
