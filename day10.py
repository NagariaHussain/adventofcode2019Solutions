from collections import defaultdict
from math import atan2, sin, cos
puzzle_input = '''.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##'''

# ------------- PART ONE --------------
ast_coord = []
x, y = 0, 0

for row in puzzle_input.splitlines():
    # if y == 25:
    #     x = 0
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
            angle = atan2((y2 - y1), (x2 - x1))
            lines_of_sight.append(angle)
    ast_det.append((len(set(lines_of_sight)), ast))

base_station = max(ast_det, key=lambda x: x[0])
print(f'Answer I: {base_station[0]} at: ', end="")
print(base_station[1])

# ----------- PART TWO -------------
vap_count = 0

def getDistance(p2):
    p1 = base_station[1]
    (x1, y1), (x2, y2) = p1, p2
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

points_on_angle = defaultdict(list)

# -pi / 2 --> 0 --> pi / 2 --> pi

for other_ast in ast_coord:
    if not other_ast == base_station[1]:
        x1, y1 = base_station[1]
        x2, y2 = other_ast
        angle = atan2((y2 - y1), (x2 - x1))
        points_on_angle[angle].append((x2, y2))

for key in points_on_angle.keys():
    points_on_angle[key] = sorted(points_on_angle[key], key=getDistance)

# converting to a normal dict object
points_on_angle = dict(points_on_angle)
sorted_angles = sorted(points_on_angle.keys())

while not vap_count == 200:
    for angle in sorted_angles:
        if vap_count == 200:
            answer = points_on_angle[angle].pop(0)            
        else:
            if len(points_on_angle[angle]) > 0:
                points_on_angle[angle].pop(0)
                vap_count += 1


print(answer)
