import matplotlib.pyplot as plt
import src.common.file_io as PlainFileIo
import src.common.lib as lib
import numpy as np
import cv2
def stemPlot(lx,center,name=None):
    planes=24000
    data=[0]*planes
    for x in lx:
        data[x-1] = 1

    f, ax = plt.subplots(figsize=(6, 1))
    markerline, stemlines, baseline = plt.stem(data, markerfmt=" ", use_line_collection=True)
    plt.setp(stemlines, linestyle="-", color="grey", linewidth=0.1)
    stemlines.set_color("gray")
    stemlines.set_linewidth(1)
    baseline.set_color('none')
    plt.xlim([0,10000])
    plt.tight_layout()
    plt.savefig("stemplot/stemplot_{}_{}_{}.png".format(name,center[0],center[1])) # ,format='svg'
    plt.close(f)


def intensity_pos_array_to_pointId_to_position_dict(intensity_pos_array):
    heigth,width=intensity_pos_array.shape
    pointId_to_position_dict={}
    for h in range(heigth):
        for w in range(width):
            pid=intensity_pos_array[h,w]
            if pid!=0:
                pointId_to_position_dict[pid]=(h,w)
    return pointId_to_position_dict

ix3b=PlainFileIo.FileIo("/Users/wangjiahui/work/Figure3/1 stream 561 20ms corrected.WT/1 stream 561 20ms corrected_Localization.txt")
ix3b.import_file(stopPlane=30000) #
planeCount3b=ix3b.planeCount
intensity_pos_array3b=ix3b.intensity_pos_array
posDict3b=ix3b.posDict



pointId_to_position_dict3b=intensity_pos_array_to_pointId_to_position_dict(intensity_pos_array3b)
posDict3b=lib.make_pos_appendage(posDict3b,intensity_pos_array3b,pointId_to_position_dict3b)


intensity_pos_array=intensity_pos_array3b
heigth,width=intensity_pos_array.shape
binary_img=np.zeros([heigth,width,3])
for h in range(heigth):
    for w in range(width):
        if intensity_pos_array[h,w] !=0:
           binary_img[h,w,:]=255



for pointId, pointLs in posDict3b.items():
    start_and_len_ls=lib.findContinuityPlanes(pointLs)
    start_and_len_ls = lib.linkPointLs(start_and_len_ls, 6)
    start_pos=start_and_len_ls[::2]
    on_state_len=start_and_len_ls[1::2]


    if max(on_state_len)>=50:
        croped_ls=[]
        for idx,str_pos in enumerate(start_pos):
            continueLens=on_state_len[idx]
            if continueLens < 50:
                croped_ls.extend(list(range(str_pos,str_pos+continueLens,1)))



        #print(pointId)
        center=pointId_to_position_dict3b[pointId]
        if center[0] > 800 and 700< center[1] < 1500:
            print(center)
            stemPlot(pointLs, center, name="crop0")
            stemPlot(croped_ls, center, name="crop50")

            #cv2.rectangle(binary_img, (center[1] - 10, center[0] - 10), (center[1] + 10, center[0] + 10), (255, 0, 0), 2)
#

# plt.imshow(binary_img)
# plt.show()



