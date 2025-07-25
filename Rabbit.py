from collections import deque

def solve_rabbit_leap():
    # Represent state as a string: 'E' for east-bound, 'W' for west-bound, '_' for empty
    initial_state = "EEE_WWW"
    goal_state = "WWW_EEE"
    
    # Define possible moves (positions a rabbit can move to)
    def get_moves(state):
        moves = []
        empty_pos = state.index('_')
        
        # Check possible jumps to the left (west-bound rabbits moving right)
        for i in [empty_pos - 1, empty_pos - 2]:
            if i >= 0 and state[i] == 'W':
                new_state = list(state)
                new_state[i], new_state[empty_pos] = new_state[empty_pos], new_state[i]
                moves.append(''.join(new_state))
        
        # Check possible jumps to the right (east-bound rabbits moving left)
        for i in [empty_pos + 1, empty_pos + 2]:
            if i < len(state) and state[i] == 'E':
                new_state = list(state)
                new_state[i], new_state[empty_pos] = new_state[empty_pos], new_state[i]
                moves.append(''.join(new_state))
        
        return moves
    
    # BFS implementation
    def bfs():
        queue = deque()
        queue.append((initial_state, []))
        visited = set()
        visited.add(initial_state)
        
        while queue:
            current_state, path = queue.popleft()
            
            if current_state == goal_state:
                return path + [current_state]
            
            for move in get_moves(current_state):
                if move not in visited:
                    visited.add(move)
                    queue.append((move, path + [current_state]))
        
        return None
    
    # DFS implementation
    def dfs():
        stack = [(initial_state, [])]
        visited = set()
        visited.add(initial_state)
        
        while stack:
            current_state, path = stack.pop()
            
            if current_state == goal_state:
                return path + [current_state]
            
            for move in get_moves(current_state):
                if move not in visited:
                    visited.add(move)
                    stack.append((move, path + [current_state]))
        
        return None
    
    print("BFS Solution:")
    bfs_path = bfs()
    for i, state in enumerate(bfs_path):
        print(f"Step {i}: {state}")
    
    print("\nDFS Solution:")
    dfs_path = dfs()
    for i, state in enumerate(dfs_path):
        print(f"Step {i}: {state}")

solve_rabbit_leap()
