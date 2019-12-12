from math import atan2, sin, cos
puzzle_input = '''#.#.###.#.#....#..##.#....
.....#..#..#..#.#..#.....#
.##.##.##.##.##..#...#...#
#.#...#.#####...###.#.#.#.
.#####.###.#.#.####.#####.
#.#.#.##.#.##...####.#.##.
##....###..#.#..#..#..###.
..##....#.#...##.#.#...###
#.....#.#######..##.##.#..
#.###.#..###.#.#..##.....#
##.#.#.##.#......#####..##
#..##.#.##..###.##.###..##
#..#.###...#.#...#..#.##.#
.#..#.#....###.#.#..##.#.#
#.##.#####..###...#.###.##
#...##..#..##.##.#.##..###
#.#.###.###.....####.##..#
######....#.##....###.#..#
..##.#.####.....###..##.#.
#..#..#...#.####..######..
#####.##...#.#....#....#.#
.#####.##.#.#####..##.#...
#..##..##.#.##.##.####..##
.##..####..#..####.#######
#.#..#.##.#.######....##..
.#.##.##.####......#.##.##'''

# ------------- PART ONE --------------
ast_coord = []
x, y = 0, 0

for row in puzzle_input.splitlines():
    for point in row:
        if point == '#':
            ast_coord.append((x, y))
        x += 1
    y += 1

ast_det = []

# Calculation the distinct equations of lines of sight
for ast in ast_coord:
    lines_of_sight = []
    for other_ast in ast_coord:
        if not other_ast == ast:
            x1, y1 = ast
            x2, y2 = other_ast
            slope = (y2 - y1) / (x2 - x1)
            intercept = y1 - (slope * x1)
            angle = atan2((y2 - y1), (x2 - x1))
            lines_of_sight.append((angle, intercept))
    ast_det.append(len(set(lines_of_sight)))


print(max(ast_det))
