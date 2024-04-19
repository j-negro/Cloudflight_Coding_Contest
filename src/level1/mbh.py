for file in range(1, 6):
    in_file = open(f"inputs/level2_{file}.in", "r")
    out_file = open(f"outputs/mbh_level2_{file}.out", "w")

    paths = int(in_file.readline())
    for i in range(paths):
        path = in_file.readline()
        out_file.write(
            f"{path.count('W')} {path.count('D')} {path.count('S')} {path.count('A')}\n"
        )
