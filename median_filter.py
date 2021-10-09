import numpy as np

def filter(img, size, width, height, SWF):
    print("median")
    padded_img = np.zeros((height + size - 1, width + size - 1), np.uint8)
    total = size*size
    mid = total >> 1
    radius = (size - 1) >> 1
    sort_array = np.zeros(total, np.uint8)
    padded_img[radius:height + radius, radius:width + radius] = img
    if SWF==0:
        for r in range(height):
            for c in range(width):
                for i in range(size):
                    for j in range(size):
                        sort_array[(i + 1) * (j + 1) - 1] = padded_img[r + i, c + j]
                img[r, c] = np.sort(sort_array)[mid]
    else:
        area_r = size * (radius + 1)
        area_0 = (radius + 1) * (radius + 1)
        for r in range(height):
            for c in range(width):
                swf = np.zeros(8)
                min_error = 256
                min_index = -1
                target = img[r, c]
                #p=r
                L_array = np.zeros(area_r)
                R_array = np.zeros(area_r)
                U_array = np.zeros(area_r)
                D_array = np.zeros(area_r)
                for i in range(size):
                    for j in range(radius + 1):
                        L_array[(i + 1) * (j + 1) - 1] = padded_img[r + i, c + j]
                        R_array[(i + 1) * (j + 1) - 1] = padded_img[r + i, c + radius + j]
                        U_array[(i + 1) * (j + 1) - 1] = padded_img[r + j, c + i]
                        D_array[(i + 1) * (j + 1) - 1] = padded_img[r + radius + j, c + i]
                swf[0] = np.sort(L_array)[area_r >> 1]
                swf[1] = np.sort(R_array)[area_r >> 1]
                swf[2] = np.sort(U_array)[area_r >> 1]
                swf[3] = np.sort(D_array)[area_r >> 1]
                #p=0
                NW_array = np.zeros(area_0)
                NE_array = np.zeros(area_0)
                SW_array = np.zeros(area_0)
                SE_array = np.zeros(area_0)
                for i in range(radius + 1):
                    for j in range(radius + 1):
                        NW_array[(i + 1) * (j + 1) - 1] = padded_img[r + i, c + j]
                        NE_array[(i + 1) * (j + 1) - 1] = padded_img[r + i, c + radius + j]
                        SW_array[(i + 1) * (j + 1) - 1] = padded_img[r + radius + i, c + j]
                        SE_array[(i + 1) * (j + 1) - 1] = padded_img[r + radius + i, c + radius + j]
                swf[4] = np.sort(NW_array)[area_0 >> 1]
                swf[5] = np.sort(NE_array)[area_0 >> 1]
                swf[6] = np.sort(SW_array)[area_0 >> 1]
                swf[7] = np.sort(SE_array)[area_0 >> 1]
                for i in range(8):
                    if np.uint8(swf[i]) == target:
                        min_index = i
                        break
                    elif (abs(swf[i] - target) < min_error):
                        min_error = abs(swf[i] - target)
                        min_index = i
                img[r, c] = np.uint8(swf[min_index])