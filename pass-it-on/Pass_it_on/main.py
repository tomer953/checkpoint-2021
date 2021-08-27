from pwintools import pwintools
import string
import time

r = pwintools.Process(r'Pass_it_on.exe')

def main():
    flag = ''
    flag_len = 27
    time = 0
    r.recvline()
    for i in range(flag_len):
        for chr in (string.digits + string.ascii_letters + '_{}!'):
            input_flag = flag + chr + 'A' * (flag_len -1 - i)
            tmp_time = send_flag(input_flag)
            if tmp_time > time:
                time = tmp_time
                tmp_char = chr
                print(f'{chr} - time {tmp_time}')

        flag += tmp_char
        print(flag)


def send_flag(flag):
    start = time.time()
    r.sendline(flag)
    r.recvline(timeout=5000)
    r.recvline(timeout=5000)
    end = time.time()
    return (end - start)


main()
