import src.common.file_io as PlainFileIo
import src.common.lib as lib
import matplotlib.pyplot as plt
import numpy as np


want647=True
if want647:
    ix=PlainFileIo.FileIo("/Users/wangjiahui/work/Figure2/647/1 stream 647 20ms corrected crop_Localization.txt")
else:
    ix=PlainFileIo.FileIo("/Users/wangjiahui/work/Figure2/Cy3B/3 stream 561 20ms corrected crop_Localization.txt")
ix.import_file(stopPlane=30000) #
planeCount=ix.planeCount
intensity_pos_array=ix.intensity_pos_array

heigth,width=intensity_pos_array.shape
pointId_to_position_dict={}
for h in range(heigth):
    for w in range(width):
        pid=intensity_pos_array[h,w]
        if pid!=0:
            pointId_to_position_dict[pid]=(h,w)

posDict=ix.posDict
posDict=lib.make_pos_appendage(posDict,intensity_pos_array,pointId_to_position_dict)

frame_count_for_sum_detection={x:0 for x in range(102)}
frame_count_for_on_state={x:0 for x in range(102)}
frame_count_for_num_of_gap={x:0 for x in range(102)}
frame_count_for_off_state={x:0 for x in range(30000)}



all_frame_count=0
all_on_state_count=0
on_length_over_5=0
for pointId, pointLs in posDict.items():
    start_and_len_ls=lib.findContinuityPlanes(pointLs)
    on_state_len=start_and_len_ls[1::2]
    sum_frame_count=sum(on_state_len)
    all_frame_count+=sum_frame_count
    all_on_state_count+=len(on_state_len)
    """
    find sum detection Number 
    """
    if sum_frame_count > 90:
        continue

    frame_count_for_sum_detection[sum_frame_count] += 1

    """
    find number of gap 
    """
    frame_count_for_num_of_gap[len(on_state_len)]+=1

    """
    find number of on state
    """
    for cnt in on_state_len:
        frame_count_for_on_state[cnt]+=1
    """
    find number of off state
    """


    off_len_ls=lib.find_off_length(start_and_len_ls)
    for cnt in off_len_ls:
        frame_count_for_off_state[cnt]+=1


sum_frame_count=0
for count, count_nums in frame_count_for_sum_detection.items():
    sum_frame_count += count_nums * count
mean_frame_count=sum_frame_count/ len(posDict)
print("mean frame count of 647 is {}".format(str(mean_frame_count/planeCount*10000)))
print("mean on state length of 647 is {}".format(str(all_frame_count/all_on_state_count)))
#lib.write_k_v_dict(frame_count_dict,"frame_count_dict.txt")
pivoted_bar_sum=lib.pivot_table(frame_count_for_sum_detection)
print(pivoted_bar_sum[1])
pivoted_bar_on=lib.pivot_table(frame_count_for_on_state)
pivoted_bar_gap=lib.pivot_table(frame_count_for_num_of_gap)
pivoted_bar_off=lib.pivot_table(frame_count_for_off_state)


number_of_off=0
max_gap_num=0
for k,v in frame_count_for_off_state.items():
    number_of_off+=v
    if k> max_gap_num:
        max_gap_num=k
print("number of gap length==1: {}".format(str(frame_count_for_off_state[1]/number_of_off)))
print("max_gap_number:{}".format(str(max_gap_num)))





def bar_plot(pivoted_bar_ls,want647=True):
    sum_num=sum(pivoted_bar_ls)
    pivoted_bar_ls=[x/sum_num for x in pivoted_bar_ls]
    plt.figure(figsize=(8,4))
    if want647:
        cmp='m'
    else:
        cmp="c"
    plt.bar(range(12),pivoted_bar_ls,color=cmp)
    xtick_txt=["<1","2-10","11-20","21-30","31-40","41-50","51-60","61-70","71-80","81-90","91-100",">100"]
    plt.xticks(range(len(xtick_txt)),xtick_txt)
    plt.yscale("log")
    #plt.savefig("apple_distribution.pdf")
    plt.show()

# bar_plot(pivoted_bar_sum,want647)
# bar_plot(pivoted_bar_on,want647)
# bar_plot(pivoted_bar_gap,want647)
# bar_plot(pivoted_bar_off,want647)