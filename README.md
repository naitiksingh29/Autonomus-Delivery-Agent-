# Autonomus-Delivery-Agent-Autonomous Delivery Agent: Pathfinding Simulator

This project simulates an autonomous delivery agent navigating a city grid to find the most efficient route from a start point to a destination. It demonstrates how different pathfinding algorithms solve the same problem, with a focus on fuel optimization using A* search.

Features
A Search*: Finds the most efficient path using a heuristic based on Manhattan distance. Minimizes total steps (fuel).
Breadth-First Search (BFS): Explores the grid layer by layer and guarantees the shortest path in an unweighted grid.
Depth-First Search (DFS): Explores deeply along paths before backtracking. Finds a valid path but not necessarily the shortest.
Interactive Command-Line Interface: Lets you choose which algorithm to run or compare all at once.
Grid Visualization: Shows a text-based grid highlighting the path found.
Getting Started
Prerequisites
Python 3.x
Installation
Download or clone the repository.
Save the main file as autonom.py.
Running the Program

Open a terminal, navigate to the folder containing autonom.py, and run:

python autonom.py

Follow the on-screen menu to select an algorithm and see the path results.

How the Algorithms Work
A Search*: Uses a heuristic to guide the search. Finds the optimal path with the least cost.
Breadth-First Search (BFS): Explores nodes level by level. Guarantees the shortest path in terms of steps.
Depth-First Search (DFS): Explores one path fully before backtracking. Does not guarantee the shortest path.
Algorithm Comparison
Algorithm	Optimal Path	Notes
A*	Yes	Efficient, guided by heuristic. Best overall.
BFS	Yes	Guarantees shortest path but less efficient in large grids.
DFS	No	Finds a path but may be longer or inefficient.
Future Improvements
Support for weighted grids with varying fuel costs.
Add obstacles or dynamic environments.
Implement a graphical interface for visualization.
Add diagonal movement support.
License

This project is open-source and free to use for educational purposes.
