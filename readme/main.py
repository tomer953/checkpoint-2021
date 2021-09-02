
import itertools
from Crypto.Cipher import ARC4
import time
import random

mapper = {
  "A": ["A", "a", "4", "@"],
  "B": ["B", "b", "8"],
  "C": ["C", "c", "©", "¢"],
  "D": ["D", "d", "6"],
  "E": ["E", "e", "3"],
  "F": ["F", "f", "7"],
  "G": ["G", "g", "9"],
  "H": ["H", "h"],
  "I": ["I", "i", "1", "l"],
  "J": ["J", "j", "7"],
  "K": ["K", "k"],
  "L": ["L", "l", "1"],
  "M": ["M", "m", "8"],
  "N": ["N", "n", "2"],
  "O": ["O", "o", "0", "*"],
  "P": ["P", "p", "9"],
  "Q": ["Q", "q"],
  "R": ["R", "r"],
  "S": ["S", "s", "5"],
  "T": ["T", "t"],
  "U": ["U", "u", "["],
  "V": ["V", "v"],
  "W": ["W", "w", "3"],
  "X": ["X", "x", "*"],
  "Y": ["Y", "y"],
  "Z": ["Z", "z"],
}

def get_all_options(str):
    x = []
    # for each char, append the relevant array from the mapper, or the char itself if not exist
    for c in str:
        ch = c.upper()
        x.append(mapper[ch] if ch in mapper else [c])
    
    # this should decrease search time
    for a in x:
        random.shuffle(a)
    return itertools.product(*x)


def check_key(key, key_checker_data):
    key = 'CSA{' + key + '}'
    result = ARC4.new((key).encode()).decrypt(key_checker_data)
    return result == b'success'


def main():
    # read key_checker_data file as binary
    with open('key_checker_data', mode='rb') as file:
        key_checker_data = file.read()

    # check every option of that pharse from the readme
    # using the 1337 codes map in the file 
    print('searching flag...')
    start = time.time()

    i = 0
    for key in get_all_options("hey_that_is_the_great_puzzle"): 
        key = "".join(key)
        # print(key)
        if check_key(key, key_checker_data):
            print("Found flag: CSA{" + key + "}")
            break
        # print progress...
        i += 1
        if (i % 1000000 == 0):
            print(i / 1000000)

    end = time.time()
    print('finish time')
    print((end - start) / 1000)


main()