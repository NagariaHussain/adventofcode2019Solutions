p_input = []

with open('input6.txt', 'r') as f:
    for line in f.readlines():
        data = line.rstrip('\n')
        p_input.append(tuple(data.split(')')))

# --------------- PART ONE --------------
orbit_checksum = 0

relations = {}

for parent, child in p_input:
    relations[child] = parent

print(relations)

# Counting the orbit checksum
for star in relations.keys():
    root = star
    while root in relations:
        root = relations[root]
        orbit_checksum += 1

print(f'ORBIT CHECKSUM: {orbit_checksum}')

# ------------- PART TWO ----------------
