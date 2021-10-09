import numpy as np
from scipy import signal

#Table for pascal triangle's value
pascal = [[1],
         [1, 1],
         [1, 2, 1],
         [1, 3, 3, 1],
         [1, 4, 6, 4, 1],#5x5
         [1, 5, 10, 10, 5, 1],
         [1, 6, 15, 20, 15, 6, 1],#7x7
         [1, 7, 21, 35, 35, 21, 7, 1],
         [1, 8, 28, 56, 70, 56, 28, 8, 1],
         [1, 9, 36, 84, 126, 126, 84, 36, 9, 1],
         [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1],
         ]

SWF_5x5_binomial = np.array([[
                    [1, 4, 6, 0, 0],
                    [4, 16, 24, 0, 0],
                    [6, 24, 36, 0, 0],
                    [4, 16, 24, 0, 0],
                    [1, 4, 6, 0, 0]
                    ],
                    [
                    [0, 0, 6, 4, 1],
                    [0, 0, 24, 16, 4],
                    [0, 0, 36, 24, 6],
                    [0, 0, 24, 16, 4],
                    [0, 0, 6, 4, 1]
                    ],
                    [
                    [1, 4, 6, 4, 1],
                    [4, 16, 24, 16, 4],
                    [6, 24, 36, 24, 6],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]
                    ],
                    [
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [6, 24, 36, 24, 6],
                    [4, 16, 24, 16, 4],
                    [1, 4, 6, 4, 1]
                    ],
                    [
                    [1, 4, 6, 0, 0],
                    [4, 16, 24, 0, 0],
                    [6, 24, 36, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]
                    ],
                    [
                    [0, 0, 6, 4, 1],
                    [0, 0, 24, 16, 4],
                    [0, 0, 36, 24, 6],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]
                    ],
                    [
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [6, 24, 36, 0, 0],
                    [4, 16, 24, 0, 0],
                    [1, 4, 6, 0, 0]
                    ],
                    [
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 36, 24, 6],
                    [0, 0, 24, 16, 4],
                    [0, 0, 6, 4, 1]
                    ],
                    ])

SWF_7x7_binomial = [[
                    [1, 6, 15, 20, 0, 0, 0],
                    [6, 36, 90, 120, 0, 0, 0],
                    [15, 90, 225, 300, 0, 0, 0],
                    [20, 120, 300, 400, 0, 0, 0],
                    [15, 90, 225, 300, 0, 0 ,0],
                    [6, 36, 90, 120, 0, 0, 0],
                    [1, 6, 15, 20, 0, 0, 0]
                    ],
                    [
                    [0, 0, 0, 20, 15, 6, 1],
                    [0, 0, 0, 120, 90, 36, 6],
                    [0, 0, 0, 300, 225, 90, 15],
                    [0, 0, 0, 400, 300, 120, 20],
                    [0, 0, 0, 300, 225, 90, 15],
                    [0, 0, 0, 120, 90, 36, 6],
                    [0, 0, 0, 20, 20, 15, 1]
                    ],
                    [
                    [1, 6, 15, 20, 15, 6, 1],
                    [6, 36, 90, 120, 90, 36, 6],
                    [15, 90, 225, 300, 225, 90, 15],
                    [20, 120, 300, 400, 300, 120, 20],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]
                    ],
                    [
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [20, 120, 300, 400, 300, 120, 20],
                    [15, 90, 225, 300, 225, 90, 15],
                    [6, 36, 90, 120, 90, 36, 6],
                    [1, 6, 15, 20, 20, 15, 1]
                    ],
                    [
                    [1, 6, 15, 20, 0, 0, 0],
                    [6, 36, 90, 120, 0, 0, 0],
                    [15, 90, 225, 300, 0, 0, 0],
                    [20, 120, 300, 400, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]
                    ],
                    [
                    [0, 0, 0, 20, 15, 6, 1],
                    [0, 0, 0, 120, 90, 36, 6],
                    [0, 0, 0, 300, 225, 90, 15],
                    [0, 0, 0, 400, 300, 120, 20],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]
                    ],
                    [
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [20, 120, 300, 400, 0, 0, 0],
                    [15, 90, 225, 300, 0, 0, 0],
                    [6, 36, 90, 120, 0, 0, 0],
                    [1, 6, 15, 20, 0, 0, 0]
                    ],
                    [
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 400, 300, 120, 20],
                    [0, 0, 0, 300, 225, 90, 15],
                    [0, 0, 0, 120, 90, 36, 6],
                    [0, 0, 0, 20, 20, 15, 1]
                    ],
                    ]

def filter(img, size, width, height, SWF):
    #Kernel which is separate to 1xsize and sizex1 matrix
    kernel_1d = np.array(pascal[size-1])
    #Let image padded with some zero pixels, so filter can directly convolve with image
    padded_img = np.zeros((height + size - 1, width + size - 1), np.uint8)
    #temp_img is used to store the value of kernel_1d convolve with padded_img
    all_temp_img = np.zeros((height + size - 1, width), np.float32)
    radius = (size - 1) // 2
    padded_img[radius:height+radius, radius:width+radius] = img
    if SWF==0:
        weight = (1 << (size-1))
        #column
        for r in range(height + size - 1):
            for c in range(radius, width + radius):
                for i in range(-radius, radius + 1):
                    all_temp_img[r, c - radius] += padded_img[r, c + i] * kernel_1d[i + radius] / weight
        # row
        for r in range(radius, height + radius):
            for c in range(width):
                pixel = 0
                for i in range(-radius, radius + 1):
                    pixel += all_temp_img[r + i, c] * kernel_1d[i + radius] / weight
                img[r - radius, c] = np.uint8(pixel)
    else:#BUG!!!!!!!!!!!!!!!!!!!!!!!
        if size==5:
            area_r = 176
            area_0 = 121
            for r in range(radius, height):
                for c in range(radius, width):
                    swf = np.zeros(8)
                    min_error = 256
                    min_index = -1
                    target = img[r-radius, c-radius]
                    #p=r
                    swf[0] = signal.convolve2d(padded_img[r - radius:r+radius+1, c - radius:c+radius+1], SWF_5x5_binomial[0], mode='valid') / area_r#L
                    swf[1] = signal.convolve2d(padded_img[r - radius:r+radius+1, c - radius:c+radius+1], SWF_5x5_binomial[1], mode='valid') / area_r#R
                    swf[2] = signal.convolve2d(padded_img[r - radius:r+radius+1, c - radius:c+radius+1], SWF_5x5_binomial[2], mode='valid') / area_r#U
                    swf[3] = signal.convolve2d(padded_img[r - radius:r+radius+1, c - radius:c+radius+1], SWF_5x5_binomial[3], mode='valid') / area_r#D
                    #p=0
                    swf[4] = signal.convolve2d(padded_img[r - radius:r+radius+1, c - radius:c+radius+1], SWF_5x5_binomial[4], mode='valid') / area_0#NW
                    swf[5] = signal.convolve2d(padded_img[r - radius:r+radius+1, c - radius:c+radius+1], SWF_5x5_binomial[5], mode='valid') / area_0#NE
                    swf[6] = signal.convolve2d(padded_img[r - radius:r+radius+1, c - radius:c+radius+1], SWF_5x5_binomial[6], mode='valid') / area_0#SW
                    swf[7] = signal.convolve2d(padded_img[r - radius:r+radius+1, c - radius:c+radius+1], SWF_5x5_binomial[7], mode='valid') / area_0#SE
                    for i in range(8):
                        if (abs(swf[i] - target) < min_error):
                            min_error = abs(swf[i] - target)
                            min_index = i
                    img[r - radius, c-radius] = np.uint8(swf[min_index])
        elif size==7:
            area_r = 2688
            area_0 = 1764
            for r in range(radius, height):
                for c in range(radius, width):
                    swf = np.zeros(8)
                    min_error = 256
                    min_index = -1
                    target = img[r - radius, c - radius]
                    # p=r
                    swf[0] = signal.convolve2d(padded_img[r - radius:r + radius + 1, c - radius:c + radius + 1],
                                               SWF_7x7_binomial[0], mode='valid') / area_r  # L
                    swf[1] = signal.convolve2d(padded_img[r - radius:r + radius + 1, c - radius:c + radius + 1],
                                               SWF_7x7_binomial[1], mode='valid') / area_r  # R
                    swf[2] = signal.convolve2d(padded_img[r - radius:r + radius + 1, c - radius:c + radius + 1],
                                               SWF_7x7_binomial[2], mode='valid') / area_r  # U
                    swf[3] = signal.convolve2d(padded_img[r - radius:r + radius + 1, c - radius:c + radius + 1],
                                               SWF_7x7_binomial[3], mode='valid') / area_r  # D
                    # p=0
                    swf[4] = signal.convolve2d(padded_img[r - radius:r + radius + 1, c - radius:c + radius + 1],
                                               SWF_7x7_binomial[4], mode='valid') / area_0  # NW
                    swf[5] = signal.convolve2d(padded_img[r - radius:r + radius + 1, c - radius:c + radius + 1],
                                               SWF_7x7_binomial[5], mode='valid') / area_0  # NE
                    swf[6] = signal.convolve2d(padded_img[r - radius:r + radius + 1, c - radius:c + radius + 1],
                                               SWF_7x7_binomial[6], mode='valid') / area_0  # SW
                    swf[7] = signal.convolve2d(padded_img[r - radius:r + radius + 1, c - radius:c + radius + 1],
                                               SWF_7x7_binomial[7], mode='valid') / area_0  # SE
                    for i in range(8):
                        if (abs(swf[i] - target) < min_error):
                            min_error = abs(swf[i] - target)
                            min_index = i
                    img[r - radius, c - radius] = np.uint8(swf[min_index])
