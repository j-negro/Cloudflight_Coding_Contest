def count_directions(input: str):
    # Result in the form of 'W', 'D', 'S', 'A'
    result = [0, 0, 0, 0]

    # Count the number of each direction
    for direction in input:
        if direction == "W":
            result[0] += 1
        elif direction == "D":
            result[1] += 1
        elif direction == "S":
            result[2] += 1
        elif direction == "A":
            result[3] += 1

    return result


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
        input_file = f"{inputs_dir}/level1_{i}.in"
        input_str = parse_input_file(input_file)

        output_file = f"{outputs_dir}/level1_{i}.out"

        results = []

        for input in input_str:
            results.append(count_directions(input))

        with open(output_file, "w") as file:
            for result in results:
                file.write(" ".join(map(str, result)) + "\n")
