# def parse_validity(input: str):
#     cur_height = 0
#     cur_width = 0

#     max_height = 0
#     max_width = 0

#     min_height = 0
#     min_width = 0

#     # Count the number of each direction
#     for direction in input:
#         if direction == "W":
#             cur_height += 1
#             max_height = max(max_height, cur_height)
#         elif direction == "D":
#             cur_width += 1
#             max_width = max(max_width, cur_width)
#         elif direction == "S":
#             cur_height -= 1
#             min_height = min(min_height, cur_height)
#         elif direction == "A":
#             cur_width -= 1
#             min_width = min(min_width, cur_width)

#     return max_width - min_width + 1, max_height - min_height + 1


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

        return inputs


if __name__ == "__main__":
    inputs_dir = "inputs"
    outputs_dir = "outputs"

    for i in range(1, 2):
        input_file = f"{inputs_dir}/level3_{i}.in"
        input_str = parse_input_file(input_file)

        print(input_str)

        # output_file = f"{outputs_dir}/level2_{i}.out"

        # results = []

        # for input in input_str:
        #     results.append(parse_validity(input))

        # with open(output_file, "w") as file:
        #     for result in results:
        #         file.write(" ".join(map(str, result)) + "\n")
