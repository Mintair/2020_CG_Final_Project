import numpy as np
from scipy import signal

#Only filtered a channel(R,G,B) each time.
def filter(img, size, width, height, sigmaSpace, sigmaColor):
    radius = (size - 1) >> 1
    space_coeff = -0.5 / (sigmaSpace*sigmaSpace)
    color_coeff = -0.5 / (sigmaColor*sigmaColor)
    temp_img = img.copy()
    #Space weight
    space_weight = np.zeros((size, size))
    for i in range(-radius, radius + 1):
        for j in range(-radius, radius + 1):
            space_weight[i + radius, j + radius] = np.exp(space_coeff * (i * i + j * j))
    #Color weight
    color_weight = np.zeros(256)
    for i in range(256):
        color_weight[i] = np.exp(color_coeff * i * i)

    for r in range(height):
        for c in range(width):
            weight = 0
            value = 0
            for i in range(-radius, radius+1):
                x = r + i
                for j in range(-radius, radius+1):
                    y = c + j
                    if x < 0 or x >= height or y < 0 or y >=width:
                        val = 0
                    else:
                        val = temp_img[x, y]
                    w = np.float32(color_weight[np.abs(int(temp_img[r, c]) - val)]) * np.float32(space_weight[i + radius, j + radius])
                    weight += w
                    value += val * w
            img[r, c] = np.uint8(value / weight)
