for file in range(0, 6):
    in_file = open(f"inputs/level1_{file}.in", "r")
    out_file = open(f"outputs/mbh_level1_{file}.out", "w")

    paths = int(in_file.readline())
    for i in range(paths):
        path = in_file.readline()
        out_file.write(f"{path.count('W')} {path.count('D')} {path.count('S')} {path.count('A')}\n")
