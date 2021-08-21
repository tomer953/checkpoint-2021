
from itertools import product
from enigma.machine import EnigmaMachine

ciphertext = "HSVNNPBLMSXATWWPEBXTCRRCBMULAALCDLOMGRKIPALACVXMUECSWIKGVLQZDALRCAACQTBZMYAEVSMESIXDVCUWMSBLVSRBXGPQFATUMMSAQVYMVKXQERVBFLTSRATSKEERQBBXTE"

rotors = ["I", "II", "III", "IV", "V"]
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# 3 4 7 - could be the ring combination or the position 'CDG'
# or if based-0 index so position 'BCF'

def crack_enigma():

    # for each rotors combination ('I IV II')
        # for every ring combination ('1 17 3')
            # for each position alphabet ('YAD')

    # for each rotors combination ('I IV II')
    for _rotor in product(rotors, repeat=3):
        rotor = ' '.join(_rotor)
        print(rotor)

        ring = '3 4 7'
        # for every ring combination ('1 26 3')
        # for _ring in product(range(1, 27), repeat=3):
        #     ring = ' '.join([str(x) for x in _ring])
        #     # print(ring)

        # set machine with selected rotor and ring
        machine = EnigmaMachine.from_key_sheet(
            rotors=rotor, reflector='B', ring_settings=ring)

        # for each position alphabet ('YAD')
        for _position in product(alphabet, repeat=3):
            position = ''.join(_position)
            # position = 'BCF'
            machine.set_display(position)

            # decrypt cipher
            plaintext = machine.process_text(ciphertext)
            if 'FROM' in plaintext and 'STOP' in plaintext:
                print('-- found --')
                print(plaintext)
                print(rotor)
                print(ring)
                print(position)
                print(' ----- ')
    print('finish')
    return



crack_enigma()