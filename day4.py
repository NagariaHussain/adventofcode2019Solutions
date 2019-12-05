# Code written by Mohammad Hussain Nagaria on 05 December, 2019
# Email: hussainbhaitech@gmail.com
# Instagram: @NagariaHussain

# Given range
n1 = 145852
n2 = 616942
# -------------------- PART ONE -----------------
possible_pass = []

def isDoublePresent(arr):
    double_present = False
    for i in range(0, len(arr) - 1):
        if arr[i] == arr[i + 1]:
            double_present = True
    return double_present

for n in range(n1, n2):
    digits = [int(x) for x in list(str(n))]
    if isDoublePresent(digits):
        sorted_digits = sorted(digits)
        if digits == sorted_digits:
            possible_pass.append(n)

# print(possible_pass)

# The answer 
print(f"The number of possible passwords: {len(possible_pass)}")

# -------------------- PART TWO -----------------
possible_pass = []

def isExclusiveDouble(arr):
    is_double = False
    stack = []
    for digit in arr:
        if not stack or stack[0] == digit:
            stack.insert(0, digit) # or stack.append(digit)
        else:
            if len(stack) == 2:
                is_double = True
            stack.clear()
            stack.append(digit)
    if len(stack) == 2:
        is_double = True    

    return is_double


for n in range(n1, n2):
    digits = [int(x) for x in list(str(n))]
    if isExclusiveDouble(digits):
        sorted_digits = sorted(digits)
        if digits == sorted_digits:
            possible_pass.append(n)
    
# print(possible_pass)
print(f"The number of possible passwords: {len(possible_pass)}")

