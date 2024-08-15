from sokoban_state import SokobanState  # Import the SokobanState class
import os



def main():
    initial_player_pos = (2, 3)
    initial_box_positions = {(2, 2), (3, 4)}
    goal_positions = {(1, 1), (3, 3)}
    grid = [
        ['#', '#', '#', '#', '#'],
        ['#', '.', '.', 'G', '#'],
        ['#', '.', 'B', '.', '#'],
        ['#', '.', '.', 'B', '#'],
        ['#', '#', '#', '#', '#'],
    ]

    # Initialize the state
    initial_state = SokobanState(initial_player_pos, initial_box_positions, goal_positions, grid)

    # Here, you could pass `initial_state` to a search algorithm
    # result = search_algorithm(initial_state)

    # For now, just print the initial state
    print("Initial State:")
    print(initial_state)


if __name__ == "__main__":
    main()

