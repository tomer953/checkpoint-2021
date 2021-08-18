from Crypto.Cipher import ARC4
import base64


def check_key(key, key_checker_data):
    """ returns True is the key is correct.
        Usage:
        check_key('{I_think_this_is_the_key}', key_checker_data)
    """
    result = ARC4.new(("CSA" + key).encode()).decrypt(key_checker_data)
    # print(result)
    return result == b'success'


print("testing key...")

# read key_checker_data file as binary
file_name = 'key_checker_data'
with open(file_name, mode='rb') as file:  # b is important -> binary
    key_checker_data = file.read()


# Using readlines()
f = open('keys.txt', 'r')
keys = f.readlines()

for key in keys:
    if key[-1] == '\n':
        key = key[:-1]
    result = check_key(key, key_checker_data)
    if result:
        print('found')
        exit()
print('done')
