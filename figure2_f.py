import src.common.file_io as PlainFileIo
import src.common.lib as lib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


ix647=PlainFileIo.FileIo("/Users/wangjiahui/work/Figure2/647/1 stream 647 20ms corrected crop_Localization.txt")
ix647.import_file(stopPlane=30000) #
planeCount647=ix647.planeCount
intensity_pos_array647=ix647.intensity_pos_array
posDict647=ix647.posDict


ix3b=PlainFileIo.FileIo("/Users/wangjiahui/work/Figure2/Cy3B/3 stream 561 20ms corrected crop_Localization.txt")
ix3b.import_file(stopPlane=30000) #
planeCount3b=ix3b.planeCount
intensity_pos_array3b=ix3b.intensity_pos_array
posDict3b=ix3b.posDict


def intensity_pos_array_to_pointId_to_position_dict(intensity_pos_array):
    heigth,width=intensity_pos_array.shape
    pointId_to_position_dict={}
    for h in range(heigth):
        for w in range(width):
            pid=intensity_pos_array[h,w]
            if pid!=0:
                pointId_to_position_dict[pid]=(h,w)
    return pointId_to_position_dict

pointId_to_position_dict647=intensity_pos_array_to_pointId_to_position_dict(intensity_pos_array647)
pointId_to_position_dict3b=intensity_pos_array_to_pointId_to_position_dict(intensity_pos_array3b)


posDict647=lib.make_pos_appendage(posDict647,intensity_pos_array647,pointId_to_position_dict647)
posDict3b=lib.make_pos_appendage(posDict3b,intensity_pos_array3b,pointId_to_position_dict3b)


frame_count_for_on_state647=[]
frame_count_for_sum_state647=[]

for pointId, pointLs in posDict647.items():
    start_and_len_ls=lib.findContinuityPlanes(pointLs)
    start_and_len_ls=lib.linkPointLs(start_and_len_ls,5)
    on_state_len=start_and_len_ls[1::2]
    frame_count_for_sum_state647.append(sum(on_state_len)/len(on_state_len))
    for cnt in on_state_len:
        frame_count_for_on_state647.append(cnt)


frame_count_for_on_state3b=[]
frame_count_for_sum_state3b=[]

for pointId, pointLs in posDict3b.items():
    start_and_len_ls=lib.findContinuityPlanes(pointLs)
    start_and_len_ls = lib.linkPointLs(start_and_len_ls, 5)
    on_state_len=start_and_len_ls[1::2]
    frame_count_for_sum_state3b.append(sum(on_state_len)/len(on_state_len))

    for cnt in on_state_len:
        frame_count_for_on_state3b.append(cnt)

#sns.kdeplot(frame_count_for_on_state647)

# sns.distplot(frame_count_for_on_state3b, color="g", label="Cy3B")
# sns.distplot(frame_count_for_on_state647 , color="m", label="AF647")

#
sns.distplot(frame_count_for_on_state3b, color="g", label="Cy3B", kde=False)
sns.distplot(frame_count_for_on_state647 , color="m", label="AF647", kde=False)

#
# plt.hist(frame_count_for_on_state647 , color="m", label="AF647",alpha=0.5)
# plt.hist(frame_count_for_on_state3b, color="g", label="Cy3B",alpha=0.5)

# sns.distplot( frame_count_for_sum_state647 , color="m", label="AF647",bins=100)
# sns.distplot( frame_count_for_sum_state3b, color="g", label="Cy3B",bins=100)


#
# plt.hist( frame_count_for_sum_state647 , color="m", label="AF647",alpha=0.5,bins=100)
# plt.hist( frame_count_for_sum_state3b, color="g", label="Cy3B",alpha=0.5,bins=100)



countDict647={}
for x in frame_count_for_on_state647:
    if x not in countDict647:
        countDict647[x]=1
    else:
        countDict647[x]+=1

countDictCy3b={}
for x in frame_count_for_on_state3b:
    if x not in countDictCy3b:
        countDictCy3b[x]=1
    else:
        countDictCy3b[x]+=1

key647=[]
val647=[]
for k,v in countDict647.items():
    key647.append(k)
    val647.append(v)


key3b=[]
val3b=[]
for k,v in countDictCy3b.items():
    key3b.append(k)
    val3b.append(v)

# plt.plot(key647,val647,'.-',color='m',label="AF647",)
# plt.plot(key3b,val3b,'.-',color='g',label="Cy3b")

plt.legend()
plt.semilogy()
#plt.show()
plt.savefig("figure2f.pdf")