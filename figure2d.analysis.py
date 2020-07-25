
import src.common.lib as lib
stack5611="../planecsv/face_plane91_232.csv"
stack5612="../planecsv/face_plane355_63.csv"
unstack561="../planecsv/face_plane359_164.csv"

def read_file(filename):
    frameLs=[]
    with open(filename) as f:
        lines = [line.rstrip() for line in f]
    for line in lines:
        frame,event=line.split(",")
        if event=='1':
            frameLs.append(int(frame))
    return frameLs


stack1_all_frame=read_file(stack5611)
stack2_all_frame=read_file(stack5612)
unstack_all_frame=read_file(unstack561)



def on_state_length_occurance(lx):
    return_dict={}
    for x in lx:
        if x in return_dict:
            return_dict[x] += 1
        else:
            return_dict[x] = 1
    return return_dict


start_and_len_ls_unstack=lib.findContinuityPlanes(unstack_all_frame)
on_state_len_unstack= start_and_len_ls_unstack[1::2]
on_state_length_unstack_dict=on_state_length_occurance(on_state_len_unstack)



start_and_len_ls_stack=lib.findContinuityPlanes(stack1_all_frame)
on_state_len_stack= start_and_len_ls_stack[1::2]
on_state_length_stack_dict=on_state_length_occurance(on_state_len_stack)


start_and_len_ls_stack_2=lib.findContinuityPlanes(stack2_all_frame)
on_state_len_stack_2= start_and_len_ls_stack_2[1::2]
on_state_length_stack_dict_2=on_state_length_occurance(on_state_len_stack_2)



print("number of on state for unstack : {}".format(len(on_state_len_unstack)))
print("average on state length for unstack 647: {}".format(len(unstack_all_frame) / len(on_state_len_unstack)))

for x in sorted(on_state_length_unstack_dict.keys()):
    print(x,on_state_length_unstack_dict[x],end=" ")
print("\n")
#print(on_state_length_unstack_dict)

print("number of on state for stack _1 : {}".format(len(on_state_len_stack)))
print("average on state length for unstack 647: {}".format(len(stack1_all_frame) / len(on_state_len_stack)))
#print(on_state_length_stack_dict)


for x in sorted(on_state_length_stack_dict.keys()):
    print(x,on_state_length_stack_dict[x],end=" ")
print("\n")

frame_count_for_off_state={}
off_len_ls=lib.find_off_length(start_and_len_ls_stack)
for cnt in off_len_ls:
    if cnt not in frame_count_for_off_state:
        frame_count_for_off_state[cnt]=1
    else:
        frame_count_for_off_state[cnt]+=1

for x in sorted(frame_count_for_off_state.keys()):
    print(x,frame_count_for_off_state[x],frame_count_for_off_state[x]/len(off_len_ls)*100,end=" ")
print("\n")



print("number of on state for stack _2 : {}".format(len(on_state_len_stack_2)))
print("average on state length for unstack 647: {}".format(len(stack2_all_frame) / len(on_state_len_stack_2)))
#print(on_state_length_stack_dict_2)

for x in sorted(on_state_length_stack_dict_2.keys()):
    print(x,on_state_length_stack_dict_2[x] , end=" ")