import numpy as np


def is_valid_path(lawn, path_directions):
    # Get the dimensions of the lawn
    num_rows, num_cols = lawn.shape

    # Initialize a list of starting points (excluding the 'X' position)
    starting_points = [(i, j) for i in range(num_rows) for j in range(num_cols) if lawn[i, j] == 0]

    # Define the movements for each direction
    moves = {
        'A': (0, -1),  # Left
        'D': (0, 1),  # Right
        'W': (-1, 0),  # Up
        'S': (1, 0)  # Down
    }

    # Iterate through each starting point
    for start in starting_points:
        # Current position
        pos = list(start)

        # Initialize a set to keep track of visited cells
        visited = set()

        # Simulate the path directions
        for direction in path_directions:
            move = moves[direction]
            # Update the current position based on the movement
            pos[0] += move[0]
            pos[1] += move[1]

            # Check if the current position is within the bounds of the lawn
            if not (0 <= pos[0] < num_rows and 0 <= pos[1] < num_cols):
                break

            # Check if the current position is on the 'X' position or if it has been visited before
            if lawn[pos[0], pos[1]] == 1 or tuple(pos) in visited:
                return False

            # Mark the current position as visited
            visited.add(tuple(pos))

        # Check if all cells in the lawn have been visited
        if len(visited) != num_rows * num_cols - 1:
            return False

    # If a valid path was found starting from any starting point, return True
    return True


def parse_input_file(file_path: str):
    with open(file_path, "r") as file:

        inputs = []

        # Grab first line
        input_count = file.readline().strip()

        for i in range(0, int(input_count)):
            # Grab first line
            dimensions = file.readline().strip()

            width, height = map(int, dimensions.split())

            # Create a matrix of the given dimensions
            matrix = [[0 for _ in range(width)] for _ in range(height)]

            for line in range(0, height):
                # Grab a line
                input_line = file.readline().strip()
                for char in range(0, width):
                    if input_line[char] == "X":
                        matrix[line][char] = 1

            # Get path
            path = file.readline().strip()

            inputs.append(((width, height), matrix, path))

        return inputs


if __name__ == "__main__":
    inputs_dir = "inputs"
    outputs_dir = "outputs"

    for i in range(0, 6):
        input_file = f"{inputs_dir}/level3_{i}.in"
        inputs_list = parse_input_file(input_file)

        output_file = f"{outputs_dir}/level3_{i}.out"

        results = []

        for input in inputs_list:

            dimensions, matrix, path = input

            is_valid = is_valid_path(np.array(matrix), path)

            if is_valid:
                results.append("VALID")
            else:
                results.append("INVALID")

        with open(output_file, "w") as file:
            for result in results:
                file.write(result + "\n")
