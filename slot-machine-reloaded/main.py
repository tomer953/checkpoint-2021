#!/usr/bin/env python3
from mt19937predictor import MT19937Predictor
import requests

PRINTABLE = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+-/:.;<=>?@[]^_`{}" # len 64

def spin_result_to_number(result):
    index_arr = [ PRINTABLE.find(c) for c in result]
    bin = [format(i, '06b') for i in index_arr]
    bin = "".join(bin)
    return int(bin,2)


def parse_number_to_flag(number,res_str,flag):
    bin_192 = format(number, '0192b')
    new_flag = flag
    j = 0
    for i in range(0,192,6): 
        partial_num = bin_192[i:i+6]
        if partial_num == '0' * 6 and flag[j] == "•":
            new_flag = new_flag[:j] + res_str[j] + flag[j+1:]
        j += 1
    return new_flag


def main():
    predictor = MT19937Predictor()
    flag = "•" * 32
    print(flag)
    cookies = {'sessionid': 's6lgjc22o2uyp0vfl47n8fft3b2gfwu6'}

    missing_chars = len(flag)
    i=0
    while missing_chars > 0:
            i+=1

            if i % 50 == 0:
                print(i)
            
            # get result from server
            # time.sleep(0.05)
            response = requests.get('http://slot-machine-reloaded.csa-challenge.com/spin/?coins=1', cookies=cookies)
            resJson = response.json()
            res_str = resJson['result']

            # fill 104 numbers to the predictor
            if i < 105:
                rnd_num = spin_result_to_number(res_str)
                predictor.setrandbits(rnd_num,192)
            else:
                # we now should know the next numbers, lets test
                clone_rnd = predictor.getrandbits(192)

            if i > 200:
                # print(clone_rnd)
                flag = parse_number_to_flag(clone_rnd, res_str, flag)
                print(flag)
                missing_chars = flag.count("•")

    print(flag)


main()
