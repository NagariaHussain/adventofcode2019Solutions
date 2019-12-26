# Code written by Mohammad Hussain Nagaria on 23 December, 2019
# Email: hussainbhaitech@gmail.com
# Instagram: @NagariaHussain

from pprint import pprint
from collections import defaultdict
from math import ceil

# Loading puzzle input
with open('input14.txt', 'r') as f:
    reactions = {}
    for reaction in f.readlines():
        # Structuring the reactions into reactants and products
        reactants = {product.split(' ')[1]: int(product.split(' ')[0]) for product in reaction.rstrip('\n').split(' => ')[0].split(', ')}
        product  = reaction.rstrip('\n').split(' => ')[1].split(' ')
        product_qty = int(product[0])
        product_name = product[1]
        reactions[product_name] = (product_qty, reactants)
    pprint(reactions)

# ------------------- PART ONE ---------------------

# To store number of `ORE`
ore_count = 0
chemical_counts = defaultdict(lambda: 0)
remanats = defaultdict(lambda : 0)


def getCount(chemical, amount):
    global ore_count
    if chemical == 'ORE':
        ore_count += amount
        return 
    for reactant, qty in reactions[chemical][1].items():
        times = ceil(amount / reactions[chemical][0])
        remanats[chemical] = reactions[chemical][0] * times - amount
        forward = (qty * times) - remanats[reactant]
        getCount(reactant, forward)
getCount('FUEL', 1)
print(ore_count)

# ------------------- PART TWO ---------------------

total_ore = 1000000000000    # 1 Trillion

# One approach would be brute force  
# Trying fuels until we get the required total number of ores
# Took nearly 10 hours on my computer

i = 1
# while True:
#     ore_count = 0
#     getCount('FUEL', i)
#     if ore_count > total_ore:
#         print(f'FUEL: {i - 1}')
#         break
#     elif ore_count == total_ore:
#         print(f'FUEL: {i}')
#         break
#     if i % 1000 == 0:
#         print(ore_count)
#     i += 1

# USING BINARY SEARCH

while True:
    ore_count = 0
    getCount('FUEL', i)
    print(f"{i} FUEL requires {ore_count} ORE")
    if ore_count > total_ore:
        break
    mintry = i
    i *= 2
    maxtry = i

print('STEP 2')

while maxtry - mintry > 1:
    print(f"answer is between {mintry} and {maxtry}")
    newtry = (mintry + maxtry) // 2
    ore_count = 0
    getCount('FUEL', newtry)
    print(f"{newtry} FUEL requires {ore_count} ORE")
    if ore_count > total_ore:
        maxtry = newtry
    else:
        mintry = newtry

print(mintry)