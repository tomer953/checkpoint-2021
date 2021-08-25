#!/usr/bin/env python3

import random
import collections
import math
from secret import flag

PRINTABLE = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+-/:.;<=>?@[]^_`{}" # len 64
flag_len = len(flag) # 32
printable_len = len(PRINTABLE) # 64
NO_COINS = "NO MORE COINS! GOODBYE."
NOT_ENOUGH_COINS = "YOU DON'T HAVE ENOUGH COINS!"
INVALID_COIN_NUMBER = "COIN NUMBER CAN'T BE NEGATIVE"
INITIAL_COINS = 10
# INITIAL_COINS = 100000000000


class Slotmachine(object):
    def __init__(self):
        seed = random.SystemRandom().getrandbits(64) # Using SystemRandom is slow, use only for seed.
        self.random = random.Random(seed) # This will make sure no one messes with my seeds!
        self.slots = [list(PRINTABLE) for i in range(flag_len)]
        self.attempt_num = 0
        self.total_coins = INITIAL_COINS
        self.last_result = ""
        self.last_gamble = 0

    def get_prize(self):
        result = self.last_result
        prize = sum([x for x in collections.Counter(result).values() if x > 2])
        prize *= self.last_gamble
        self.total_coins += prize
        return prize

    def prepend_flag(self):
        for i in range(flag_len):
            self.slots[i].remove(flag[i])
            self.slots[i] = [flag[i]] + self.slots[i]

    def check_invalid_input(self, coins):
        if self.total_coins <= 0:
            self.last_result = ""
            return NO_COINS
        if self.total_coins < coins:
            self.last_result = ""
            return NOT_ENOUGH_COINS
        if coins < 0:
            self.last_result = ""
            return INVALID_COIN_NUMBER
        return None


    # My cat wrote this function
    def choice(self):
        printable_bin = f'{len(PRINTABLE) - 1:b}' # 111111 (63)
        printable_bin_len = len(f'{len(PRINTABLE) - 1:b}') # 6
        y = flag_len * len(printable_bin)         # flag_len (32) * 6 = 192
        z = (1 << y)                   # shift left by y bits (2^y) 2^192 = 6277101735386680763835789423207666416102355444464034512896

        math_log = math.log(len(PRINTABLE), 2) # math.log(64, 2) = 6.0
        slots_len = len(self.slots)            # 32
        rand_below_z = self.random._randbelow(z -1) # random like 2124743868953491128378980738951458169372743440940745409359
        format_modulu = (slots_len * int(math_log) + 2) # 32 * 6 + 2 = 194
        rand_num = format(rand_below_z, '#0%db' % format_modulu)[2:] # binary rep of the random number in 192 bit long
        result = ""
        j = 0
        # for i in range(0,192,6) (start,step,stop) total of 32 iteration, one for each char of the flag
        for i in range(0,len(rand_num),printable_bin_len): 
            partial_rand_num = rand_num[i:i+printable_bin_len] # i:i+6 (0:6, 6:12, 12:18) pick random 6 bits (0-63)
            char_index = int(partial_rand_num,2) # convert to base 10 (0-63)
            if j == 31 and char_index == 0:
                # print(i)
                print(rand_num)
                # print(partial_rand_num)
                print(self.attempt_num)

            result += self.slots[j][char_index] # pick letter in that index
            j += 1
        return result

    def spin(self, coins):
        invalid_message = self.check_invalid_input(coins)
        if invalid_message:
            return invalid_message.center(flag_len)
        
        self.last_gamble = coins
        self.total_coins -= coins
 
        if self.attempt_num == 200:
            self.prepend_flag()
            pass
        self.attempt_num += 1

        result = self.choice()
        self.last_result = result
        return result


def main():
    slotmachine = Slotmachine()
    print(f"You have {slotmachine.total_coins} coins")
    get_next_num = True
    i=0
    while get_next_num and slotmachine.attempt_num < 2000:
        try:
            # print(i)
            i+=1
            prize = 0
            coins = 1
            result = slotmachine.spin(coins)

            if result == NO_COINS:
                get_next_num = False
            elif result != NOT_ENOUGH_COINS:
                prize = slotmachine.get_prize()
            # print(result)
            # print(f"You won {prize} coins!")
            #print(f"{slotmachine.total_coins} coins left.")

        except ValueError:
            print('valueError')
            get_next_num = False
        except NameError:
            print('nameError')
            get_next_num = False

if __name__ == "__main__":
    main()
