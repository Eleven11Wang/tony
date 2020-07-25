
import src.common.lib as lib
unstack647="../planecsv/647_face_plane408_176.csv"
stack647="../planecsv/245.180.b.csv"

def read_file(filename):
    frameLs=[]
    with open(filename) as f:
        lines = [line.rstrip() for line in f]
    for line in lines:
        frame,event=line.split(",")
        if event=='1':
            frameLs.append(int(frame))
    return frameLs


unstack647_all_frame=read_file(unstack647)
stack647_all_frame=read_file(stack647)




def on_state_length_occurance(lx):
    return_dict={}
    for x in lx:
        if x in return_dict:
            return_dict[x] += 1
        else:
            return_dict[x] = 1
    return return_dict


start_and_len_ls_647_unstack=lib.findContinuityPlanes(unstack647_all_frame)
on_state_len_647_unstack=start_and_len_ls_647_unstack[1::2]
on_state_length_unstack_647_dict=on_state_length_occurance(on_state_len_647_unstack)



start_and_len_ls_647_stack=lib.findContinuityPlanes(stack647_all_frame)
on_state_len_647_stack=start_and_len_ls_647_stack[1::2]
on_state_length_stack_647_dict=on_state_length_occurance(on_state_len_647_stack)


print("number of on state for unstack 647: {}".format(len(on_state_len_647_unstack)))
print("average on state length for unstack 647: {}".format(len(unstack647_all_frame)/len(on_state_len_647_unstack)))

print("number of on state for stack 647: {}".format(len(on_state_len_647_stack)))
print("average on state length for stack 647: {}".format(len(stack647_all_frame)/len(on_state_len_647_stack)))
print(on_state_length_unstack_647_dict)
print(on_state_length_stack_647_dict)
