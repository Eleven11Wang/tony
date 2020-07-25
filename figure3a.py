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
UPPER_LEFT=(850,600)
LOWER_RIGHT=(2350,1400)
ABSOLUTE_PATH="/Users/wangjiahui/work/Figure3/1 stream 561 20ms corrected.WT/1 stream 561 20ms corrected_Localization.txt"

ix3b=PlainFileIo.FileIo(ABSOLUTE_PATH)
ix3b.import_file(stopPlane=30000) #
planeCount3b=ix3b.planeCount
intensity_pos_array3b=ix3b.intensity_pos_array
posDict3b=ix3b.posDict
pointId_to_position_dict3b=lib.intensity_pos_array_to_pointId_to_position_dict(intensity_pos_array3b)
reconstrcuted_image_raw=lib.reconstructImgFromPosDict(intensity_pos_array3b,posDict3b)
binary_img=lib.image_to_binaryImg(reconstrcuted_image_raw)



#
# def crop_sample_area():
#
# def paste_sample_area():