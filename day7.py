from itertools import permutations

pi = [3,8,1001,8,10,8,105,1,0,0,21,30,51,72,81,94,175,256,337,418,99999,3,9,101,5,9,9,4,9,99,3,9,1001,9,3,9,1002,9,2,9,1001,9,2,9,1002,9,5,9,4,9,99,3,9,1002,9,4,9,101,4,9,9,102,5,9,9,101,3,9,9,4,9,99,3,9,1002,9,4,9,4,9,99,3,9,102,3,9,9,1001,9,4,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,99]

def getAmplifierOutput(phase_setting, amp_input): 
    '''The intcode computer'''
    puzzle_input = pi[:]    
    i = 0
    phase_set = True
    while i < len(puzzle_input):
        inst = [int(x) for x in str(puzzle_input[i])]
        inst.reverse()
        opcode = inst[0]

        if opcode == 3:
            if phase_set:
                puzzle_input[puzzle_input[i + 1]] = phase_setting
                phase_set = False
            else:
                puzzle_input[puzzle_input[i + 1]] = amp_input
            i += 2

        elif opcode == 4:
            mode = inst[2] if len(inst) > 2 else 0
            output = puzzle_input[i + 1] if mode == 1 else puzzle_input[puzzle_input[i + 1]]
            return output

        elif opcode == 1 or opcode == 2:
            para1 = puzzle_input[i + 1]
            para2 = puzzle_input[i + 2]
            para3 = puzzle_input[i + 3]

            para1mode = inst[2] if len(inst) > 2 else 0
            para2mode = inst[3] if len(inst) > 3 else 0

            input1 = para1 if para1mode == 1 else puzzle_input[para1]
            input2 = para2 if para2mode == 1 else puzzle_input[para2]

            output = input1 + input2 if opcode == 1 else input1 * input2
            puzzle_input[para3] = output
            i += 4
        
        elif opcode == 5 or opcode == 6:
            # jump-if-true/false
            para1mode = inst[2] if len(inst) > 2 else 0
            para1 = puzzle_input[i + 1] if para1mode == 1 else puzzle_input[puzzle_input[i + 1]]
            
            para2mode = inst[3] if len(inst) > 3 else 0
            para2 = puzzle_input[i + 2] if para2mode == 1 else puzzle_input[puzzle_input[i + 2]]

            if ((not para1 == 0) and opcode == 5) or (para1 == 0 and opcode == 6):
                i = para2
            else:
                i += 3
        
        elif opcode == 7 or opcode == 8:
            # less than
            print('OPCODE 7 or 8')
            para1mode = inst[2] if len(inst) > 2 else 0
            para1 = puzzle_input[i + 1] if para1mode == 1 else puzzle_input[puzzle_input[i + 1]]
            
            para2mode = inst[3] if len(inst) > 3 else 0
            para2 = puzzle_input[i + 2] if para2mode == 1 else puzzle_input[puzzle_input[i + 2]]

            para3 = puzzle_input[i + 3]
            
            if (para1 < para2 and opcode == 7) or (para1 == para2 and opcode == 8):
                puzzle_input[para3] = 1
            else:
                puzzle_input[para3] = 0
            i += 4
        else:
            break

possible_outputs = []

# integer 0 - 4 as input
# Generating random sequence

for seq in permutations([0, 1, 2, 3, 4]):
    a = getAmplifierOutput(seq[0], 0)
    b = getAmplifierOutput(seq[1], a)
    c = getAmplifierOutput(seq[2], b)
    d = getAmplifierOutput(seq[3], c)
    e = getAmplifierOutput(seq[4], d)
    possible_outputs.append(e)

# Answer to part one
print(max(possible_outputs))

# --------------- PART TWO ----------------
# Feedback loop mode
phase_setting_options = [5, 6, 7, 8, 9]

possible_outputs = []

class Amplifier:
    '''The class implementation of the int code amplifier'''
    def __init__(self, phase_setting):
        self.pointer = 0
        self.program_input = pi[:]
        self.phase_set = True
        self.phase_setting = phase_setting

    def runInstruction(self, inst_input):
        i = self.pointer
        while i < len(self.program_input):
            inst = [int(x) for x in str(self.program_input[i])]
            inst.reverse()
            opcode = inst[0]

            if opcode == 3:
                if self.phase_set:
                    self.program_input[self.program_input[i + 1]] = self.phase_setting
                    self.phase_set = False
                else:
                    self.program_input[self.program_input[i + 1]] = inst_input
                
                i += 2
            elif opcode == 4:
                mode = inst[2] if len(inst) > 2 else 0
                output = self.program_input[i + 1] if mode == 1 else self.program_input[self.program_input[i + 1]]
                self.pointer = i + 2
                return output

            elif opcode == 1 or opcode == 2:
                para1 = self.program_input[i + 1]
                para2 = self.program_input[i + 2]
                para3 = self.program_input[i + 3]

                para1mode = inst[2] if len(inst) > 2 else 0
                para2mode = inst[3] if len(inst) > 3 else 0

                input1 = para1 if para1mode == 1 else self.program_input[para1]
                input2 = para2 if para2mode == 1 else self.program_input[para2]

                output = input1 + input2 if opcode == 1 else input1 * input2
                self.program_input[para3] = output
                i += 4
            
            elif opcode == 5 or opcode == 6:
                # jump-if-true/false
                para1mode = inst[2] if len(inst) > 2 else 0
                para1 = self.program_input[i + 1] if para1mode == 1 else self.program_input[self.program_input[i + 1]]
                
                para2mode = inst[3] if len(inst) > 3 else 0
                para2 = self.program_input[i + 2] if para2mode == 1 else self.program_input[self.program_input[i + 2]]

                if ((not para1 == 0) and opcode == 5) or (para1 == 0 and opcode == 6):
                    i = para2
                else:
                    i += 3
            
            elif opcode == 7 or opcode == 8:
                # less than
                print('OPCODE 7 or 8')
                para1mode = inst[2] if len(inst) > 2 else 0
                para1 = self.program_input[i + 1] if para1mode == 1 else self.program_input[self.program_input[i + 1]]
                
                para2mode = inst[3] if len(inst) > 3 else 0
                para2 = self.program_input[i + 2] if para2mode == 1 else self.program_input[self.program_input[i + 2]]

                para3 = self.program_input[i + 3]
                
                if (para1 < para2 and opcode == 7) or (para1 == para2 and opcode == 8):
                    self.program_input[para3] = 1
                else:
                    self.program_input[para3] = 0
                i += 4
            else:
                break 
        self.pointer = i 

for seq in permutations(phase_setting_options):
    print(seq)
    a = Amplifier(seq[0])
    b = Amplifier(seq[1])
    c = Amplifier(seq[2])
    d = Amplifier(seq[3])
    e = Amplifier(seq[4])

    inn = 0

    while True:
        output_a = a.runInstruction(inn) 
        if not output_a:
            possible_outputs.append(inn)
            break
        inn = e.runInstruction(d.runInstruction(c.runInstruction(b.runInstruction(output_a))))

# Answer to part two
print(f'{max(possible_outputs)} is the max output')