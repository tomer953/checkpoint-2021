# HINT2 - LSBIT_STEGANOGRAPHY_OVER_TRIANGULAR_SERIES
import cv2
import numpy as np
import types


def messageToBinary(message):
    if type(message) == str:
        return ''.join([format(ord(i), "08b") for i in message])
    elif type(message) == bytes or type(message) == np.ndarray:
        return [format(i, "08b") for i in message]
    elif type(message) == int or type(message) == np.uint8:
        return format(message, "08b")
    else:
        raise TypeError("Input type not supported")


def showData(image, chosen_pixels):

    tri_arr = get_triangular_array(750)[1:]
    print(tri_arr)
    binary_data = ""
    i = 0
    for values in image:
        for pixel in values:
            if i not in tri_arr:
                i += 1
                continue
            i += 1
            # convert the red,green and blue values into binary format
            p = messageToBinary(pixel)
            # extracting data from the least significant bit of red pixel
            binary_data += p[-1]
            # extracting data from the least significant bit of red pixel
            # extracting data from the least significant bit of red pixel
    # split by 8-bits
    print(binary_data)
    all_bytes = [binary_data[i: i+8] for i in range(0, len(binary_data), 8)]
    print(all_bytes)
    # convert from bits to characters
    decoded_data = ""
    for byte in all_bytes:
        decoded_data += chr(int(byte, 2))
    return decoded_data


def triangle(n):
    return int(((n**2)+n)/2.0)


# return array of triangular array with n values
# n = 6 return [0, 1, 3, 6, 10, 15]
def get_triangular_array(n):
    return [triangle(i) for i in range(n)]


def get_chosen_pixels(pixel_cnt):
    chosen_pixels = []
    # get some big array of triangular series values
    tri_arr = get_triangular_array(200)
    # print(tri_arr)
    # increase i with the next value of triangular series
    i = 0
    j = 0
    while i < pixel_cnt:
        chosen_pixels.append(i)
        j += 1
        i += tri_arr[j]
    return chosen_pixels


# Decode the data in the image


def main():
    # read the image that contains the hidden image
    image = cv2.imread("challenge.bmp", 0) # open as grayscale
    # calc total pixels
    pixel_cnt = int(image.size)
    print(pixel_cnt)

    chosen_pixels = get_chosen_pixels(pixel_cnt)
    print(chosen_pixels)

    text = showData(image, chosen_pixels)
    print(text)


main()
