import matplotlib.pyplot as plt
import src.common.file_io as PlainFileIo
import src.common.lib as lib
import numpy as np
import cv2
import lib
import image_pipline
import visualization_functions
import utils
import seaborn as sns

ix3b=PlainFileIo.FileIo("/Users/wangjiahui/work/Figure3/1 stream 561 20ms corrected.WT/1 stream 561 20ms corrected_Localization.txt")
ix3b.import_file(stopPlane=30000) #
planeCount3b=ix3b.planeCount
intensity_pos_array3b=ix3b.intensity_pos_array
posDict3b=ix3b.posDict
pointId_to_position_dict3b=lib.intensity_pos_array_to_pointId_to_position_dict(intensity_pos_array3b)
reconstrcuted_image_raw=lib.reconstructImgFromPosDict(intensity_pos_array3b,posDict3b)
binary_img=lib.image_to_binaryImg(reconstrcuted_image_raw)


bead_position_ls,stuck_position_ls=image_pipline.find_bead_and_stuck_localiztions(intensity_pos_array3b,posDict3b)
#visualization_functions.reconstructImgFromHeatmap(intensity_pos_array3b,posDict3b)

"""
use bead for testing
"""
# merged_bead_position_ls,center_beads_ls=image_pipline.merge_localization_into_puncta(bead_position_ls)
# beads_cluster_localiztions=image_pipline.cluster_into_puncta(merged_bead_position_ls,intensity_pos_array3b)
# remove_beads_img=visualization_functions.visualiza_labeled_postion(binary_img, beads_cluster_localiztions)
# # beads_locations=[y for x in beads_cluster_localiztions for y in x]
# # visualization_functions.visualiza_centers_ls(binary_img,[y for x in beads_cluster_localiztions for y in x])
# plt.imshow(remove_beads_img)
# plt.show()




punctas_position_dict, punctas_center_dict=image_pipline.merge_localization_into_puncta(stuck_position_ls)
all_cluster_dict=image_pipline.cluster_into_puncta(punctas_position_dict,intensity_pos_array3b)
series_analysis_for_each_puncta=image_pipline.make_appendage(posDict3b,intensity_pos_array3b,all_cluster_dict)

start_and_len_dict,peak_index_id=image_pipline.find_start_and_len(series_analysis_for_each_puncta)
crop_dict=image_pipline.find_crop_series(start_and_len_dict,100)
posDict3b_new=image_pipline.crop_series(crop_dict, all_cluster_dict, posDict3b, intensity_pos_array3b)
visualization_functions.reconstructImg(intensity_pos_array3b,posDict3b_new,"reconstruct_100",uselog=False)
# visualization_functions.visualiza_centers_ls(binary_img,[punctas_center_dict[x] for x in peak_index_id])
# plt.imshow(binary_img)
# plt.show()



#
# sample_area_idx=image_pipline.cheak_image_region(center_stuck_ls)
# center_stuck_ls=[center_stuck_ls[idx] for idx in sample_area_idx]
# center_stuck_ls=utils.tuple_float_to_int(center_stuck_ls)
# merged_stuck_position_ls=[merged_stuck_position_ls[idx] for idx in sample_area_idx]
# # print(len(merged_stuck_position_ls))
# stuck_cluster_localiztions=image_pipline.cluster_into_puncta(merged_stuck_position_ls,intensity_pos_array3b)
# # print(len(stuck_cluster_localiztions))
# # print(len([y for x in stuck_cluster_localiztions for y in x]))
# series_analysis_for_each_puncta=image_pipline.make_appendage(posDict3b,intensity_pos_array3b,stuck_cluster_localiztions)

#
# used_center=[]
# intensity_ls=[]
#
# for idx,series in enumerate(series_analysis_for_each_puncta):
#
#     start_and_len_ls = image_pipline.findContinuityPlanes(series)
#     start_and_len_ls=lib.linkPointLs(start_and_len_ls,5)
#     if(max(start_and_len_ls[1::2])>=100):
#         series=image_pipline.filter_stuck(start_and_len_ls,500)
#
#         intensity_ls.append(len(series))
#         visualization_functions.stemPlot(series, center_stuck_ls[idx], 'n')
#         croped_planes=image_pipline.filter_stuck(start_and_len_ls,50)
#         #visualization_functions.stemPlot(croped_planes, center_stuck_ls[idx], 'c')
#         used_center.append(center_stuck_ls[idx])
#         utils.to_csv("{}_{}.csv".format(center_stuck_ls[idx][0],center_stuck_ls[idx][1]),series )
#         countLs=lib.make_bar(start_and_len_ls[1::2])
#         #visualization_functions.bar_plot(countLs,"{}_{}".format(center_stuck_ls[idx][0],center_stuck_ls[idx][1]))
# print(used_center)
# print(np.argsort(np.array(intensity_ls)))
# print(intensity_ls)
#
#
# visualization_functions.visualiza_centers_ls(binary_img,used_center)
#
# #visualization_functions.visualiza_centers_ls(binary_img,[y for x in stuck_cluster_localiztions for y in x])
# plt.imshow(binary_img)
# plt.show()
#
#
#
#


#






# mean+ 3td
