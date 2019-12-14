from collections import defaultdict
# ---------------------- PART ONE -----------------
# Notes
# All of the panels are currently black.
# provide 0 if the robot is over a black panel or 1 if the robot is over a white panel
pi = [3,8,1005,8,319,1106,0,11,0,0,0,104,1,104,0,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,1001,8,0,28,2,1008,7,10,2,4,17,10,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,1002,8,1,59,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,1001,8,0,81,1006,0,24,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,102,1,8,105,2,6,13,10,1006,0,5,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,1002,8,1,134,2,1007,0,10,2,1102,20,10,2,1106,4,10,1,3,1,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,1002,8,1,172,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,101,0,8,194,1,103,7,10,1006,0,3,1,4,0,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,101,0,8,228,2,109,0,10,1,101,17,10,1006,0,79,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,1002,8,1,260,2,1008,16,10,1,1105,20,10,1,3,17,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1002,8,1,295,1,1002,16,10,101,1,9,9,1007,9,1081,10,1005,10,15,99,109,641,104,0,104,1,21101,387365733012,0,1,21102,1,336,0,1105,1,440,21102,937263735552,1,1,21101,0,347,0,1106,0,440,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,3451034715,1,1,21101,0,394,0,1105,1,440,21102,3224595675,1,1,21101,0,405,0,1106,0,440,3,10,104,0,104,0,3,10,104,0,104,0,21101,0,838337454440,1,21102,428,1,0,1105,1,440,21101,0,825460798308,1,21101,439,0,0,1105,1,440,99,109,2,22101,0,-1,1,21102,1,40,2,21101,0,471,3,21101,461,0,0,1106,0,504,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,466,467,482,4,0,1001,466,1,466,108,4,466,10,1006,10,498,1102,1,0,466,109,-2,2105,1,0,0,109,4,2101,0,-1,503,1207,-3,0,10,1006,10,521,21101,0,0,-3,21202,-3,1,1,22102,1,-2,2,21101,1,0,3,21102,540,1,0,1105,1,545,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,568,2207,-4,-2,10,1006,10,568,22102,1,-4,-4,1106,0,636,22102,1,-4,1,21201,-3,-1,2,21202,-2,2,3,21102,587,1,0,1105,1,545,21201,1,0,-4,21101,0,1,-1,2207,-4,-2,10,1006,10,606,21102,0,1,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,628,22102,1,-1,1,21102,1,628,0,105,1,503,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0]

for i in range(0, 9999999):
    pi.append(0)


class PaintingRobot:
    def __init__(self):
        # Intcode program config
        self.pointer = 0
        self.program_input = pi[:]
        self.relative_base = 0
        self.first_out = None
        self.second_out = None
        # Robot state config
        self.current_position = 0, 0
        self.current_direction = '^'
        self.current_panel_color = 0
        
        # Panel config
        self.color_config = defaultdict(lambda : 0)
        self.painted_panels = []

    def getUniquePanels(self):
        # print(self.color_config)
        # print(self.painted_panels)
        return len(set(self.painted_panels))
    
    def move(self, towards):
        if towards == None:
            print('OOOOOOOOOOOOOOOOOOOOOO')

        dy, dx = 0, 0
        if self.current_direction == '^':
            if towards == 0:
                # turn left
                self.current_direction = '<'
                dx = -1
            else:
                # turn right
                self.current_direction = '>'
                dx = 1
        elif self.current_direction == 'v':
            if towards == 0:
                # turn left
                self.current_direction = '>'
                dx = 1
            else:
                # turn right
                self.current_direction = '<'
                dx = -1
        elif self.current_direction == '>':
            if towards == 0:
                # turn left
                self.current_direction = '^'
                dy = 1
            else:
                # turn right
                self.current_direction = 'v'
                dy = -1
        else:
            if towards == 0:
                # turn left
                self.current_direction = 'v'
                dy = -1
            else:
                # turn right
                self.current_direction = '^'
                dy = 1 

        x, y = self.current_position
        x += dx
        y += dy
        # print(self.current_position)
        self.current_position = x, y
        # print(self.current_position)
        # print(dx, dy)
        # print(self.current_position)
        self.current_panel_color = self.color_config[self.current_position]      
 
    def paint(self, color):
        if color == None:
            print('OOOOOOOOOOOOOOOOOOOOOO')
        self.color_config[self.current_position] = color
        self.painted_panels.append(self.current_position)
        # print(self.color_config)

    def runInstruction(self):
        i = self.pointer
        while i < len(self.program_input):
            inst = [int(x) for x in str(self.program_input[i])]
            inst.reverse()
            opcode = inst[0]
            mode = inst[2] if len(inst) > 2 else 0
            
            if opcode == 3:
                ui = self.current_panel_color
                if mode == 0:
                    self.program_input[self.program_input[i + 1]] = ui
                else:
                    self.program_input[self.program_input[i + 1] + self.relative_base] = ui
                i += 2

            elif opcode == 4: 
                if mode == 0:
                    output = self.program_input[self.program_input[i + 1]]
                elif mode == 1:
                    output = self.program_input[i + 1]
                else:
                    output = self.program_input[self.program_input[i + 2] + self.relative_base]
                # print(f'Before: {self.first_out, self.second_out}')
                # print(output)
                
                if self.first_out:
                    self.second_out = output
                    self.move(self.second_out)
                    self.first_out, self.second_out = None, None               
                else:
                    self.first_out = output 
                    self.paint(self.first_out)
                    # print(f'After: {self.first_out, self.second_out}')

                
                
                
                i += 2
                
            elif opcode == 1 or opcode == 2:
                para1 = self.program_input[i + 1]
                para2 = self.program_input[i + 2]
                para3 = self.program_input[i + 3]

                para1mode = mode
                para2mode = inst[3] if len(inst) > 3 else 0
                para3mode = inst[4] if len(inst) > 4 else 0
                
                if para1mode == 0:
                    input1 = self.program_input[para1]
                elif para1mode == 1:
                    input1 = para1
                else:
                    input1 = self.program_input[para1 + self.relative_base]

                if para2mode == 0:
                    input2 = self.program_input[para2]
                elif para2mode == 1:
                    input2 = para2
                else:
                    input2 = self.program_input[para2 + self.relative_base]

                output = input1 + input2 if opcode == 1 else input1 * input2
                
                if para3mode == 0:
                    self.program_input[para3] = output
                else:
                    self.program_input[para3 + self.relative_base] = output
                i += 4
            
            # --- PART TWO ---
            elif opcode == 5 or opcode == 6:
                # jump-if-true/false
                para1mode = mode
                if para1mode == 0:
                    para1 = self.program_input[self.program_input[i + 1]]
                elif para1mode == 1:
                    para1 = self.program_input[i + 1]
                else:
                    para1 = self.program_input[self.program_input[i + 1] + self.relative_base]

                para2mode = inst[3] if len(inst) > 3 else 0
                if para2mode == 0:
                    para2 = self.program_input[self.program_input[i + 2]]
                elif para2mode == 1:
                    para2 = self.program_input[i + 2]
                else:
                    para2 = self.program_input[self.program_input[i + 2] + self.relative_base]

                if ((not para1 == 0) and opcode == 5) or (para1 == 0 and opcode == 6):
                    i = para2
                else:
                    i += 3
            
            elif opcode == 7 or opcode == 8:
                # less than
                para1mode = mode
                if para1mode == 0:
                    para1 = self.program_input[self.program_input[i + 1]]
                elif para1mode == 1:
                    para1 = self.program_input[i + 1]
                else:
                    para1 = self.program_input[self.program_input[i + 1] + self.relative_base]
                
                para2mode = inst[3] if len(inst) > 3 else 0
                if para2mode == 0:
                    para2 = self.program_input[self.program_input[i + 2]]
                elif para2mode == 1:
                    para2 = self.program_input[i + 2]
                else:
                    para2 = self.program_input[self.program_input[i + 2] + self.relative_base]

                para3mode = inst[4] if len(inst) > 4 else 0
            
                para3 = self.program_input[i + 3] if para3mode == 0 else (self.program_input[i + 3] + self.relative_base)
                
                if (para1 < para2 and opcode == 7) or (para1 == para2 and opcode == 8):
                    self.program_input[para3] = 1
                else:
                    self.program_input[para3] = 0
                i += 4
            
            elif (opcode == 9):
                sec = inst[1] if len(inst) > 1 else 0
                if not sec == 9: 
                    para1mode = mode
                    para1 = self.program_input[i + 1] if para1mode == 1 else self.program_input[self.program_input[i + 1]]
                    if para1mode == 0:
                        para1 = self.program_input[self.program_input[i + 1]]
                    elif para1mode == 1:
                        para1 = self.program_input[i + 1]
                    else:
                        para1 = self.program_input[self.program_input[i + 1] + self.relative_base]
                    self.relative_base += para1
                    i += 2
                else:
                    break
            else:
                break
        self.pointer = i 


robot = PaintingRobot()
robot.runInstruction()

# answer
print(robot.getUniquePanels())