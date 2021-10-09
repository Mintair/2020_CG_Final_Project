import numpy as np
from scipy import signal


def filter(img, size, width, height, SWF):
    integral = np.zeros((height + size, width + size))
    area = size * size
    radius = (size - 1) >> 1
    for r in range(height):
        sum = 0
        for c in range(width):
            sum += img[r, c]
            integral[r + radius + 1, c + radius + 1] = integral[r + radius, c + radius + 1] + sum
    for r in range(radius + 1, height + size):
        integral[r, width + radius + 1:width + size] = integral[r, width + radius]
    for c in range(radius + 1, width + size):
        integral[height + radius + 1:height + size, c] = integral[height + radius, c]
    #Mean_Filter
    if SWF==0:
        for r in range(radius + 1, height + radius + 1):
            for c in range(radius + 1, width + radius + 1):
                sum = integral[r+radius, c+radius] + integral[r-radius-1, c-radius-1] - integral[r-radius-1, c+radius] - integral[r+radius, c-radius-1]
                mean = sum / area
                img[r - radius - 1, c - radius - 1] = np.uint8(mean)
    #SWF_Mean_Filter
    else:
        area_r = size * (radius + 1)
        area_0 = (radius + 1) * (radius + 1)
        for r in range(radius + 1, height + radius + 1):
            for c in range(radius + 1, width + radius + 1):
                swf = np.zeros(8)
                min_error = 256
                min_index = -1
                target = img[r - radius - 1, c - radius - 1]
                #p=r
                #L
                swf[0] = (integral[r+radius, c] + integral[r-radius-1, c-radius-1] - integral[r-radius-1, c] - integral[r+radius, c-radius-1]) / area_r
                #R
                swf[1] = (integral[r+radius, c+radius] + integral[r-radius-1, c-1] - integral[r-radius-1, c+radius] - integral[r+radius, c-1]) / area_r
                #U
                swf[2] = (integral[r, c+radius] + integral[r-radius-1, c-radius-1] - integral[r-radius-1, c+radius] - integral[r, c-radius-1]) / area_r
                #D
                swf[3] = (integral[r+radius, c+radius] + integral[r-1, c-radius-1] - integral[r-1, c+radius] - integral[r+radius, c-radius-1]) / area_r
                #p=0
                #NW
                swf[4] = (integral[r, c] + integral[r-radius-1, c-radius-1] - integral[r-radius-1, c] - integral[r, c-radius-1]) / area_0
                #NE
                swf[5] = (integral[r, c+radius] + integral[r-radius-1, c-1] - integral[r-radius-1, c+radius] - integral[r, c-1]) / area_0
                #SW
                swf[6] = (integral[r+radius, c] + integral[r-1, c-radius-1] - integral[r-1, c] - integral[r+radius, c-radius-1]) / area_0
                #SE
                swf[7] = (integral[r+radius, c+radius] + integral[r-1, c-1] - integral[r-1, c+radius] - integral[r+radius, c-1]) / area_0
                for i in range(8):
                    if ((abs(swf[i] - target)) < min_error):
                        min_error = abs(swf[i] - target)
                        min_index = i
                img[r - radius - 1, c - radius - 1] = np.uint8(swf[min_index])
