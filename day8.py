with open('input8.txt', 'r') as f:
    puzzle_input = f.readline().rstrip('\n')

def getDigitsInfo(digits):
    freq = {x:0 for x in set(digits)}

    for digit in digits:
        freq[digit] += 1
    
    return freq

image_layers_freq = []

#  150 = 25 * 6 pixels image
for i in range(0, len(puzzle_input), 150):
    digits = [int(x) for x in puzzle_input[i:i + 150]]
    image_layers_freq.append(getDigitsInfo(digits))

index = 0

least_zero = image_layers_freq[0][0] 

for layer in image_layers_freq:
    if layer[0] < least_zero:
        least_zero = layer[0]
        least_index = index
    index += 1

# Answer
print(f"{least_zero} and answer: {image_layers_freq[least_index][1] * image_layers_freq[least_index][2]}")


# ------------- PART TWO -----------------
top_to_bottom = []

for i in range(0, 150):
    digited = [int(x) for x in puzzle_input[i::150]]
    print(i, digited)
    top_to_bottom.append(digited)

decoded_image = []

for pixel_layer in top_to_bottom:
    for pixel_color in pixel_layer:
        if pixel_color == 1 or pixel_color == 0:
            decoded_image.append(pixel_color)
            break

# Printing the image so we can see its message
image = '''1111000110111000110011100
1000000010100101001010010
1110000010100101000010010
1000000010111001011011100
1000010010101001001010000
1111001100100100111010000'''
image = image.replace('0', '⬛️').replace('1', '⬜️')
print(image)

# Another way to print the image
# requires numpy
# np.set_printoptions(formatter={'all':lambda x: ' ' if x==0 else 'x'})