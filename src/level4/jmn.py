def parse_validity(dimensions, matrix, path, starting_x, starting_y):

    width, height = dimensions

    matrix_copy = [row[:] for row in matrix]

    cur_x = starting_x
    cur_y = starting_y

    if matrix_copy[cur_y][cur_x] == 1:
        return False
    matrix_copy[cur_y][cur_x] = 1

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
            return False

        if matrix_copy[cur_y][cur_x] == 1:
            return False
        matrix_copy[cur_y][cur_x] = 1

    if all(all(cell == 1 for cell in row) for row in matrix_copy):
        return True
    return False


def parse_input_file(
    file_path: str,
) -> list[tuple[tuple[int, int], list[list[int]]]]:
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
                    # Check both x and X
                    if input_line[char] == "x" or input_line[char] == "X":
                        matrix[line][char] = 1

            inputs.append(((width, height), matrix))

        return inputs


if __name__ == "__main__":
    inputs_dir = "inputs"
    outputs_dir = "outputs"

    for i in range(0, 1):
        input_file = f"{inputs_dir}/level4_{i}.in"
        inputs_list = parse_input_file(input_file)

        output_file = f"{outputs_dir}/level4_{i}.out"

        results = []

        for input in inputs_list:

            dimensions, matrix = input

            print(
                parse_validity(
                    dimensions,
                    matrix,
                    "AAASDDDSAAASDDSAASDDSAASDDDWWWDSSSDWWWDSSSDWWWWAAAWDDDWAAAWDDD",
                    3,
                    0,
                )
            )

            # is_valid = parse_validity(dimensions, matrix)

            # if is_valid:
            #     results.append("VALID")
            # else:
            #     results.append("INVALID")

        # with open(output_file, "w") as file:
        #     for result in results:
        #         file.write(result + "\n")
