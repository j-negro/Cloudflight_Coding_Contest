def parse_validity(dimensions, matrix, path):

    width, height = dimensions

    for starting_x in range(0, width):
        for starting_y in range(0, height):

            matrix_copy = [row[:] for row in matrix]

            cur_x = starting_x
            cur_y = starting_y

            if matrix_copy[cur_y][cur_x] == 1:
                continue
            matrix_copy[cur_y][cur_x] = 1

            broken = False

            for direction in path:
                if direction == "W":
                    cur_y -= 1
                elif direction == "D":
                    cur_x += 1
                elif direction == "S":
                    cur_y += 1
                elif direction == "A":
                    cur_x -= 1

                if cur_x < 0 or cur_x >= width or cur_y < 0 or cur_y >= height:
                    broken = True
                    break

                if matrix_copy[cur_y][cur_x] == 1:
                    broken = True
                    break
                matrix_copy[cur_y][cur_x] = 1

            if not broken and all(
                all(cell == 1 for cell in row) for row in matrix_copy
            ):
                return True
    return False


def parse_input_file(
    file_path: str,
) -> list[tuple[tuple[int, int], list[list[int]], str]]:
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

        output_file = f"{outputs_dir}/level3a_{i}.out"

        results = []

        for input in inputs_list:

            dimensions, matrix, path = input

            is_valid = parse_validity(dimensions, matrix, path)

            if is_valid:
                results.append("VALID")
            else:
                results.append("INVALID")

        with open(output_file, "w") as file:
            for result in results:
                file.write(result + "\n")
