# Code written by Mohammad Hussain Nagaria on 02 December, 2019
# Email: hussainbhaitech@gmail.com
# Instagram: @NagariaHussain

init_list = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,19,6,23,2,23,6,27,2,6,27,31,2,13,31,35,1,9,35,39,2,10,39,43,1,6,43,47,1,13,47,51,2,6,51,55,2,55,6,59,1,59,5,63,2,9,63,67,1,5,67,71,2,10,71,75,1,6,75,79,1,79,5,83,2,83,10,87,1,9,87,91,1,5,91,95,1,95,6,99,2,10,99,103,1,5,103,107,1,107,6,111,1,5,111,115,2,115,6,119,1,119,6,123,1,123,10,127,1,127,13,131,1,131,2,135,1,135,5,0,99,2,14,0,0]
# for i in range(0, len(init_list), 4):
#     process_list = init_list[i:i+4]
#     print(process_list)
#     if process_list[0] == 1:
#         init_list[process_list[3]] = init_list[process_list[1]] + init_list[process_list[2]]
#     elif process_list[0] == 2:
#         init_list[process_list[3]] = init_list[process_list[1]] * init_list[process_list[2]]
#     else:
#         break

# print(init_list)

output = 19690720
exp_list = init_list[:]


for k in range(0, 100):
    for j in range(0,100):
        print(k, j)
        exp_list[1] =  k
        exp_list[2] = j
        for i in range(0, len(exp_list), 4):
            process_list = exp_list[i:i+4]
            # print(process_list)
            if process_list[0] == 1:
                exp_list[process_list[3]] = exp_list[process_list[1]] + exp_list[process_list[2]]
            elif process_list[0] == 2:
                exp_list[process_list[3]] = exp_list[process_list[1]] * exp_list[process_list[2]]
            else:
                break
        if exp_list[0] == output:
            print(f"got it: {k}, {j}")
            print(exp_list)
            exit(0)
        else:
            exp_list = init_list[:]
            