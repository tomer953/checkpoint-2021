#coding: utf-8
from PIL import Image


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


image = Image.open("challenge.bmp")

extracted = ''

pixels = image.load()
# Iterate over pixels of the first row

chosen_pixels = get_chosen_pixels(image.width * image.height)
tri_arr = get_triangular_array(750)
i = 0
for x in range(0,image.width):
    for y in range(0, image.height):
        if i not in tri_arr:
            i += 1
            continue
        i += 1
        p = pixels[x,y]
        # Store LSB of each pixel
        extracted += bin(p)[-1]

print(extracted)
chars = []
for i in range(int(len(extracted)/8)):
    byte = extracted[i*8:(i+1)*8]
    chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))

print(chars)