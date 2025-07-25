from collections import deque
import itertools

def solve_bridge_crossing():
    # Define people and their crossing times
    people = {
        'Amogh': 5,
        'Ameya': 10,
        'Grandmother': 20,
        'Grandfather': 25
    }
    
    initial_state = (frozenset(people.keys()), frozenset(), True, 0)  # (left_side, right_side, is_umbrella_left, total_time)
    goal_condition = (frozenset(), frozenset(people.keys()))
    
    # Generate all possible pairs for crossing
    def generate_moves(group):
        return list(itertools.combinations(group, 2)) + list(itertools.combinations(group, 1))
    
    # BFS implementation
    def bfs():
        queue = deque()
        queue.append((initial_state, []))
        visited = set()
        visited.add(initial_state)
        
        while queue:
            current_state, path = queue.popleft()
            left_side, right_side, is_umbrella_left, total_time = current_state
            
            # Check if we've reached the goal
            if not left_side:
                return path + [current_state]
            
            # Determine which side has the umbrella
            if is_umbrella_left:
                from_side = left_side
                to_side = right_side
            else:
                from_side = right_side
                to_side = left_side
            
            # Generate all possible crossing moves
            for movers in generate_moves(from_side):
                movers = set(movers)
                if not movers:
                    continue
                
                # Calculate crossing time (slowest person)
                crossing_time = max(people[p] for p in movers)
                new_total_time = total_time + crossing_time
                
                if new_total_time > 60:
                    continue  # Skip if over time limit
                
                # Update sides
                new_left = left_side - movers if is_umbrella_left else left_side.union(movers)
                new_right = right_side.union(movers) if is_umbrella_left else right_side - movers
                
                # The umbrella moves with the people
                new_umbrella_pos = not is_umbrella_left
                
                new_state = (new_left, new_right, new_umbrella_pos, new_total_time)
                
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + [current_state]))
        
        return None
    
    # Find solution
    solution_path = bfs()
    
    print("Bridge Crossing Solution:")
    prev_time = 0
    for i, state in enumerate(solution_path):
        left, right, umbrella_left, time = state
        action = ""
        if i < len(solution_path) - 1:
            next_state = solution_path[i+1]
            moved = (state[0] - next_state[0]) or (state[1] - next_state[1])
            direction = "left to right" if umbrella_left else "right to left"
            action = f" - {', '.join(moved)} move {direction} ({max(people[p] for p in moved)} minutes)"
        print(f"Step {i}: Time {prev_time}-{time} minutes: Left: {', '.join(left) if left else 'empty'}, Right: {', '.join(right) if right else 'empty'}, Umbrella: {'left' if umbrella_left else 'right'}{action}")
        prev_time = time

solve_bridge_crossing()
