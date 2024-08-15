class SokobanState:
    def __init__(self, player_pos, box_positions, goal_positions, grid):
        self.player_pos = player_pos  # (x, y) tuple for the player's position
        self.box_positions = frozenset(box_positions)  # Set of (x, y) tuples for boxes
        self.goal_positions = frozenset(goal_positions)  # Set of (x, y) tuples for goals
        self.grid = grid  # 2D list representing the grid layout

    def is_goal_state(self):
        # Check if all boxes are on the goals
        return self.box_positions == self.goal_positions

    def __eq__(self, other):
        return (self.player_pos == other.player_pos and
                self.box_positions == other.box_positions)

    def __hash__(self):
        return hash((self.player_pos, self.box_positions))

    def possible_moves(self):
        # Returns a list of possible moves (new states)
        # Implement the logic for checking valid moves
        pass
