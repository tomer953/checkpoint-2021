from Crypto.Cipher import ARC4


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
f1 = open('keys1.txt', 'r')
f2 = open('keys2.txt', 'r')
keys1 = f1.readlines()
keys2 = f2.readlines()

# combine partial keys into a key
i = 0
key = ''
for key1 in keys1:
    if key1[-1] == '\n':
        key1 = key1[:-1]
    print(i)
    print(key)
    i+=1
    for key2 in keys2:
        if key2[-1] == '\n':
            key2 = key2[:-1]
        key = '{' + key1 + '_' + key2 + '}'
        # test if the key decode the data
        result = check_key(key, key_checker_data)
        if result:
            print('found')
            print(key) # {hEY_th@T_l5_thE_9RE4T_p[ZZL3}
            exit()
print('done')

