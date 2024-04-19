for file in range(1, 6):
    in_file = open(f"inputs/level2_{file}.in", "r")
    out_file = open(f"outputs/mbh_level2_{file}.out", "w")

    paths = int(in_file.readline())
    for i in range(paths):
        x, y = 0, 0
        minx = maxx = maxy = miny = 0
        path = in_file.readline()
        for dir in path:
            if dir == 'W':
                y += 1
            elif dir == 'A':
                x -= 1
            elif dir == 'S':
                y += 1
            else:
                x += 1

            minx = min(minx, x)
            maxx = max(maxx, x)
            miny = min(miny, y)
            maxy = max(maxy, y)

    out_file.write(f"{abs(minx - maxx)} {abs(miny-maxy)}\n")
