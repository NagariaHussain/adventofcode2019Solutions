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

def getParents(star):
    parents = []
    while star in relations:
        star = relations[star]
        parents.append(star)
    return parents

you_parents = getParents('YOU')
san_parents = getParents('SAN')

for p in you_parents:
    if p in san_parents:
        intersection = p
        break

orbits_jump = you_parents.index(intersection) + san_parents.index(intersection)

print(f'ORBITS TO JUMP: {orbits_jump}')
