# HINT2 - LSBIT_STEGANOGRAPHY_OVER_TRIANGULAR_SERIES
import cv2
import numpy as np





def triangle(n):
    return (((n**2)+n)//2)


# return array of triangular array with n values
# n = 6 return [0, 1, 3, 6, 10, 15]
def get_triangular_array(n):
    return [triangle(i) for i in range(n)]


def showData(image):

    # flip the image vertically
    image = cv2.flip(image, 0)
    # get array with triangular series
    tri_arr = get_triangular_array(280)

    # print(tri_arr)
    binary_data = ""
    i = 0
    for values in image:
        for pixel in values:
            # skip non triangular series numbers
            if i not in tri_arr:
                i += 1
                continue
            i += 1
            # extracting data from the least significant bit
            binary_data += bin(pixel)[-1]

    # split by 8-bits
    all_bytes = [binary_data[i: i+8] for i in range(0, len(binary_data), 8)]
    # convert from bits to characters
    decoded_data = ""
    for byte in all_bytes:
        decoded_data += chr(int(byte, 2))
    return decoded_data


def main():
    # read the image that contains the hidden image
    image = cv2.imread("challenge.bmp", 0)  # open as grayscale

    # Decode the data in the image
    text = showData(image)
    print(text)


main()

