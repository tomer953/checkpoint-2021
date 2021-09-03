# FROM HINT1 - IN_SECOND_HINT_MAKE_ODD_0_AND_EVEN_255
import cv2
import numpy as np
import types

# Decode the data in the image

def get_pixel_color(value):
    if (value % 2 == 0):
        return 255
    return 0

def parse_hint():
    # read the image that contains the hidden image
    image = cv2.imread("second_hint.bmp")  # read the image using cv2.imread()
    new_image = np.copy(image)
    i = 0
    for values in new_image:
        for pixel in values:
            pixel[0] = get_pixel_color(pixel[0])
            pixel[1] = get_pixel_color(pixel[1])
            pixel[2] = get_pixel_color(pixel[1])

    cv2.imwrite('solve_hint2.bmp', new_image)



parse_hint()