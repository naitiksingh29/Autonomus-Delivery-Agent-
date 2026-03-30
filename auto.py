import heapq
from collections import deque

def manhattan_distance(a, b):
    """
    Calculates the Manhattan distance between two points on a grid.
    This serves as the heuristic for A* search.
    :param a: Tuple (row, col) of the first point.
    :param b: Tuple (row, col) of the second point.
    :return: The Manhattan distance.
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# =================================================================
# Breadth-First Search (BFS) Implementation
# =================================================================
def bfs(grid, start, goal):
    """
    Finds the shortest path from start to goal in a grid using BFS.
    :param grid: 2D list representing the map (0: path, 1: obstacle).
    :param start: Tuple (row, col) of the start position.
    :param goal: Tuple (row, col) of the goal position.
    :return: List of coordinates representing the path, or None.
    """
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start, [start])])
    visited = {start}
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        (r, c), path = queue.popleft()
        if (r, c) == goal:
            return path
        
        for dr, dc in movements:
            nr, nc = r + dr, c + dc
            neighbor = (nr, nc)
            
            if 0 <= nr < rows and 0 <= nc < cols and \
               grid[nr][nc] == 0 and neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))
    
    return None

def dfs(grid, start, goal):
    """
    Finds a path from start to goal in a grid using DFS.
    :param grid: 2D list representing the map (0: path, 1: obstacle).
    :param start: Tuple (row, col) of the start position.
    :param goal: Tuple (row, col) of the goal position.
    :return: List of coordinates representing the path, or None.
    """
    rows, cols = len(grid), len(grid[0])
    stack = [(start, [start])]
    visited = {start}
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while stack:
        (r, c), path = stack.pop()
        
        if (r, c) == goal:
            return path
        
        for dr, dc in reversed(movements):
            nr, nc = r + dr, c + dc
            neighbor = (nr, nc)
            
            if 0 <= nr < rows and 0 <= nc < cols and \
               grid[nr][nc] == 0 and neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                stack.append((neighbor, new_path))
    
    return None


def a_star_search(grid, start, goal):
    """
    Finds the optimal path (least fuel) from start to goal using A* search.
    The cost (g_score) is the fuel consumed, with each step costing 1 unit.
    """
    rows, cols = len(grid), len(grid[0])
    
    
    open_list = [(manhattan_distance(start, goal), 0, start, [start])]
    
   
    min_fuel_consumed = {start: 0}
    
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while open_list:
        
        _, current_fuel, current_node, path = heapq.heappop(open_list)
        
        if current_node == goal:
            return path

        for dr, dc in movements:
            neighbor = (current_node[0] + dr, current_node[1] + dc)
            
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and \
               grid[neighbor[0]][neighbor[1]] == 0:
                
               
                tentative_fuel = current_fuel + 1
                
              
                if tentative_fuel < min_fuel_consumed.get(neighbor, float('inf')):
                    min_fuel_consumed[neighbor] = tentative_fuel
                    
                 
                    f_score = tentative_fuel + manhattan_distance(neighbor, goal)
                    
                    new_path = path + [neighbor]
                    heapq.heappush(open_list, (f_score, tentative_fuel, neighbor, new_path))
    
    return None
def visualize_path(grid, path, start, goal, algorithm_name):
    """Prints the grid with the path highlighted."""
    if not path:
        print(f"\n--- {algorithm_name} Result ---")
        print("❌ No path could be found.")
        return

    display_grid = [list(row) for row in grid]
    
 
    for r, c in path:
        display_grid[r][c] = '.'
    
    display_grid[start[0]][start[1]] = 'S'
    display_grid[goal[0]][goal[1]] = 'G'
    
    print(f"\n--- {algorithm_name} Result ---")
    print("S: Start, G: Goal, #: Obstacle, .: Path")
    for row in display_grid:
        print(" ".join(str(cell).replace('1', '#').replace('0', ' ') for cell in row))
    
    fuel_consumed = len(path) - 1
    print(f"Path Length: {fuel_consumed} steps")
    print(f"Fuel Consumed: {fuel_consumed} units")

def main_menu():
    """
    Presents an interactive menu for the user to run pathfinding algorithms.
    """
    city_grid = [
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]

    start_point = (0, 0)
    goal_point = (4, 7)
    
    print("Welcome to the Autonomous Delivery Agent Pathfinding Simulator!")
    
    while True:
        print("\n--- Main Menu ---")
        print("1. Run A* Search (Finds least fuel path)")
        print("2. Run Breadth-First Search (BFS)")
        print("3. Run Depth-First Search (DFS)")
        print("4. Run All Algorithms")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            a_star_path = a_star_search(city_grid, start_point, goal_point)
            visualize_path(city_grid, a_star_path, start_point, goal_point, "A* Search (Fuel Optimized)")
        elif choice == '2':
            bfs_path = bfs(city_grid, start_point, goal_point)
            visualize_path(city_grid, bfs_path, start_point, goal_point, "Breadth-First Search (BFS)")
        elif choice == '3':
            dfs_path = dfs(city_grid, start_point, goal_point)
            visualize_path(city_grid, dfs_path, start_point, goal_point, "Depth-First Search (DFS)")
        elif choice == '4':
            a_star_path = a_star_search(city_grid, start_point, goal_point)
            visualize_path(city_grid, a_star_path, start_point, goal_point, "A* Search (Fuel Optimized)")
            
            bfs_path = bfs(city_grid, start_point, goal_point)
            visualize_path(city_grid, bfs_path, start_point, goal_point, "Breadth-First Search (BFS)")
            
            dfs_path = dfs(city_grid, start_point, goal_point)
            visualize_path(city_grid, dfs_path, start_point, goal_point, "Depth-First Search (DFS)")
            
            print("\nComparison Summary:")
            print("A* and BFS both find the shortest path in terms of steps, which corresponds to the least fuel consumption in this scenario.")
            print("DFS finds a valid path, but it is not guaranteed to be the shortest or most fuel-efficient.")
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main_menu()
