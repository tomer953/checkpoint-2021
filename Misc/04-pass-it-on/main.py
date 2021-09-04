
import string
import time
import subprocess

p = subprocess.Popen(['Pass_it_on.exe'],
                 stdin=subprocess.PIPE,
                 stdout=subprocess.PIPE,
                 )
                 

def main():
    flag = ''
    flag_len = 27
    p.stdout.readline()
    for i in range(flag_len):
        time = 0
        for chr in (string.ascii_letters + string.digits + '_{}!'):
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
    p.stdin.write(str.encode(flag + '\n'))
    p.stdin.flush()
    p.stdout.readline()
    p.stdout.readline()
    end = time.time()
    return (end - start)


main()
