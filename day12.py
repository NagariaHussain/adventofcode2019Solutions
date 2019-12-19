# Code written by Mohammad Hussain Nagaria on 15 December, 2019
# Email: hussainbhaitech@gmail.com
# Instagram: @NagariaHussain

# ------------------- My Puzzle Input ---------------------
# <x=-3, y=10, z=-1>
# <x=-12, y=-10, z=-5>
# <x=-9, y=0, z=10>
# <x=7, y=-5, z=-3>

# ------------------- EXAMPLE ONE ---------------------
# <x=-1, y=0, z=2>
# <x=2, y=-10, z=-7>
# <x=4, y=-8, z=8>
# <x=3, y=5, z=-1>

# ------------------- PART ONE ---------------------
moon1 = {
    "x": -3,
    "y": 10,
    "z": -1
}

moon2 = {
    "x": -12,
    "y": -10,
    "z": -5
}

moon3 = {
    "x": -9,
    "y": 0,
    "z": 10
}

moon4 = {
    "x": 7,
    "y": -5,
    "z": -3
}

moons = [moon1, moon2, moon3, moon4] 

for moon in moons:
    moon['vx'] = 0
    moon['vy'] = 0
    moon['vz'] = 0

# Taking time steps
for i in range(0, 1000):
    for moon in moons:
        for other_moon in moons:
            if not other_moon == moon:
                for coord, velocity in [("x", "vx"), ("y", "vy"), ("z", "vz")]:
                    if moon[coord] > other_moon[coord]:
                        moon[velocity] -= 1
                    elif moon[coord] < other_moon[coord]:
                        moon[velocity] += 1
    for moon in moons:
        moon["x"] += moon["vx"]
        moon["y"] += moon["vy"]
        moon["z"] += moon["vz"]

# Note
# once all moons' velocities have been updated, 
# update the position of every moon by applying velocity

total_energy = 0
for moon in moons:
    sum_of_pot = abs(moon["x"]) + abs(moon["y"]) + abs(moon["z"])
    sum_of_kit = abs(moon["vx"]) + abs(moon["vy"]) + abs(moon["vz"])
    total_energy += sum_of_kit * sum_of_pot

print(f"Answer: {total_energy}")

# ------------------- PART TWO ---------------------
moon1 = {
    "x": -3,
    "y": 10,
    "z": -1
}

moon2 = {
    "x": -12,
    "y": -10,
    "z": -5
}

moon3 = {
    "x": -9,
    "y": 0,
    "z": 10
}

moon4 = {
    "x": 7,
    "y": -5,
    "z": -3
}
moons = [moon1, moon2, moon3, moon4] 

for moon in moons:
    moon['vx'] = 0
    moon['vy'] = 0
    moon['vz'] = 0

# !!!!! BRUTE FORCE - CAN TAKE YEARS !!!!!

# print("working...")
# while True:
#     step += 1
#     for moon in moons:
#         for other_moon in moons:
#             if not other_moon == moon:
#                 for coord, velocity in [("x", "vx"), ("y", "vy"), ("z", "vz")]:
#                     if moon[coord] > other_moon[coord]:
#                         moon[velocity] -= 1
#                     elif moon[coord] < other_moon[coord]:
#                         moon[velocity] += 1
#     for moon in moons:
#         moon["x"] += moon["vx"]
#         moon["y"] += moon["vy"]
#         moon["z"] += moon["vz"]
#     current_state = [{**moon1}, {**moon2}, {**moon3}]
#     if current_state in moon_states:
#         print(f"Found in step {step}")
#         break
#     else:
#         moon_states.append(current_state)

# HINT: Components are independent of each other
moon_states_x = []
x_steps = 0

moon_states_x.append([moon1["x"], moon1["vx"], moon2["x"], moon2["vx"], moon3["x"], moon3["vx"]])

while True:
    x_steps += 1
    for moon in moons:
        for other_moon in moons:
            if not other_moon == moon:
                if moon["x"] > other_moon["x"]:
                    moon["vx"] -= 1
                elif moon["x"] < other_moon["x"]:
                    moon["vx"] += 1
    for moon in moons:
        moon["x"] += moon["vx"]
    current_state = [moon1["x"], moon1["vx"], moon2["x"], moon2["vx"], moon3["x"], moon3["vx"]]
    if current_state in moon_states_x:
        break
    else:
        moon_states_x.append(current_state)

print(f"x steps: {x_steps}")

moon_states_y = []
y_steps = 0

moon_states_y.append([moon1["y"], moon1["vy"], moon2["y"], moon2["vy"], moon3["y"], moon3["vy"]])

while True:
    y_steps += 1
    for moon in moons:
        for other_moon in moons:
            if not other_moon == moon:
                if moon["y"] > other_moon["y"]:
                    moon["vy"] -= 1
                elif moon["y"] < other_moon["y"]:
                    moon["vy"] += 1
    for moon in moons:
        moon["y"] += moon["vy"]
    current_state = [moon1["y"], moon1["vy"], moon2["y"], moon2["vy"], moon3["y"], moon3["vy"]]
    if current_state in moon_states_y:
        break
    else:
        moon_states_y.append(current_state)

print(f"y steps: {y_steps}")

moon_states_z = []
z_steps = 0

moon_states_z.append([moon1["z"], moon1["vz"], moon2["z"], moon2["vz"], moon3["z"], moon3["vz"]])

while True:
    z_steps += 1
    for moon in moons:
        for other_moon in moons:
            if not other_moon == moon:
                if moon["z"] > other_moon["z"]:
                    moon["vz"] -= 1
                elif moon["z"] < other_moon["z"]:
                    moon["vz"] += 1
    for moon in moons:
        moon["z"] += moon["vz"]
    current_state = [moon1["z"], moon1["vz"], moon2["z"], moon2["vz"], moon3["z"], moon3["vz"]]
    if current_state in moon_states_z:
        break
    else:
        moon_states_z.append(current_state)

print(f"z steps: {z_steps}")

# Now taking L.C.M of the above three steps - TAKES AGES
# def getLCM(a, b, c):
#     num = 1
#     while True:
#         if (num % a == 0) and (num % b == 0) and (num % c == 0):
#             return num
#         num += 1
#         print(num)

from math import gcd
def getLCM(x, y, z):
    gcd2 = gcd(y, z)
    lcm2 = y * z // gcd2
    lcm3 = x * lcm2 // gcd(x, lcm2)
    return lcm3

print(getLCM(x_steps, y_steps, z_steps))
