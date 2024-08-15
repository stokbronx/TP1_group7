from collections import deque

class SokobanState:
    def __init__(self, player_pos, box_positions, goal_positions, grid):
        self.player_pos = player_pos
        self.box_positions = frozenset(box_positions)
        self.goal_positions = frozenset(goal_positions)
        self.grid = grid

    def is_goal_state(self):
        return self.box_positions == self.goal_positions

    def possible_moves(self):
        # Placeholder for logic to return a list of possible moves (new states)
        pass

    def __eq__(self, other):
        return (self.player_pos == other.player_pos and
                self.box_positions == other.box_positions and
                self.goal_positions == other.goal_positions and
                self.grid == other.grid)

    def __hash__(self):
        return hash((self.player_pos, self.box_positions, self.goal_positions, tuple(map(tuple, self.grid))))

def bfs(initial_state):
    queue = deque([initial_state])
    visited = set()
    visited.add(initial_state)

    while queue:
        current_state = queue.popleft()

        if current_state.is_goal_state():
            return current_state  # or return the path to the goal state

        for move in current_state.possible_moves():
            if move not in visited:
                visited.add(move)
                queue.append(move)

    return None  # No solution found