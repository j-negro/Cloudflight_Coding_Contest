import numpy as np


def get_paths(shape, lawn, input):
    paths = []
    shape = (shape[1], shape[0])
    for i in range(shape[0]):
        for j in range(shape[1]):
            path = np.array(lawn)
            pos = [i, j]
            if path[pos[0]][pos[1]] == 1:
                continue
            path[pos[0]][pos[1]] = 1
            flag = True
            # Count the number of each direction
            for direction in input:
                if direction == "W":
                    pos[0] -= 1
                elif direction == "D":
                    pos[1] -= 1
                elif direction == "S":
                    pos[0] += 1
                elif direction == "A":
                    pos[1] += 1
                if (
                    pos[0] < 0
                    or pos[0] >= shape[0]
                    or pos[1] < 0
                    or pos[1] >= shape[1]
                    or path[pos[0]][pos[1]] == 1
                ):
                    flag = False
                    break
                path[pos[0]][pos[1]] = 1
            if flag:
                if np.all(path == 1):
                    return True  # paths.append(path)

    return paths


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

        output_file = f"{outputs_dir}/level3be_{i}.out"

        results = []

        for input in inputs_list:

            dimensions, matrix, path = input

            is_valid = get_paths(dimensions, matrix, path)

            if is_valid:
                results.append("VALID")
            else:
                results.append("INVALID")

        with open(output_file, "w") as file:
            for result in results:
                file.write(result + "\n")
