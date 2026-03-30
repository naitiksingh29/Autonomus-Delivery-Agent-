Autonomous Delivery Agent Simulation

This project simulates an autonomous delivery agent navigating a city grid to find the most efficient route from a start point to a destination. It demonstrates how different pathfinding algorithms tackle the same problem, with a focus on fuel optimization using A* search.

Features
A Search*
Finds the most efficient path using a heuristic based on Manhattan distance.
Minimizes total steps (fuel).
Breadth-First Search (BFS)
Explores the grid layer by layer.
Guarantees the shortest path in an unweighted grid.
Depth-First Search (DFS)
Explores deeply along paths before backtracking.
Finds a valid path, but not necessarily the shortest.
Interactive Command-Line Interface
Choose which algorithm to run or compare all at once.
Grid Visualization
Displays a text-based grid highlighting the path found.
Getting Started
Prerequisites
Python 3.x
Installation
Download or clone the repository.
Save the main file as autonom.py.
Running the Program
Open a terminal.
Navigate to the folder containing autonom.py.
Run the program:
python autonom.py
Follow the on-screen menu to select an algorithm and see the path results.
How the Algorithms Work
Algorithm	Description	Guarantees Optimal Path?
A*	Uses a heuristic to guide the search. Finds the path with the least total cost.	✅ Yes
BFS	Explores nodes level by level. Guarantees the shortest path in terms of steps.	✅ Yes
DFS	Explores one path fully before backtracking. Does not guarantee the shortest path.	❌ No

Notes:

A* is the most efficient for fuel optimization due to its heuristic guidance.
BFS is simple and reliable for unweighted grids.
DFS can find paths quickly in small grids but may be inefficient.
Future Improvements
Support for weighted grids with varying fuel costs.
Add obstacles or dynamic environments.
Implement a graphical interface for visualization.
Support diagonal movement.
License

This project is open-source and free to use for educational purposes.
