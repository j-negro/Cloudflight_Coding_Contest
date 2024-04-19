def get_dimensions(input: str):
    cur_height = 0
    cur_width = 0

    max_height = 0
    max_width = 0

    min_height = 0
    min_width = 0

    # Count the number of each direction
    for direction in input:
        if direction == "W":
            cur_height += 1
            max_height = max(max_height, cur_height)
        elif direction == "D":
            cur_width += 1
            max_width = max(max_width, cur_width)
        elif direction == "S":
            cur_height -= 1
            min_height = min(min_height, cur_height)
        elif direction == "A":
            cur_width -= 1
            min_width = min(min_width, cur_width)

    return max_width - min_width + 1, max_height - min_height + 1


def parse_input_file(file_path: str):
    with open(file_path, "r") as file:

        # Grab first line
        input_count = file.readline().strip()

        # Grab rest as list
        inputs = file.readlines()

        return inputs


if __name__ == "__main__":
    inputs_dir = "inputs"
    outputs_dir = "outputs"

    for i in range(1, 6):
        input_file = f"{inputs_dir}/level2_{i}.in"
        input_str = parse_input_file(input_file)

        output_file = f"{outputs_dir}/level2_{i}.out"

        results = []

        for input in input_str:
            results.append(get_dimensions(input))

        with open(output_file, "w") as file:
            for result in results:
                file.write(" ".join(map(str, result)) + "\n")
