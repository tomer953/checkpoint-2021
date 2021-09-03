# Slot Machine Reloaded
300

Remember the Slot Machine from CSA 2019?
Well, this one is a little harder...

http://slot-machine-reloaded.csa-challenge.com/


- [screenshot](../../images/slot-machine-website.png?raw=true)


**Solution:**

- the random function is getting a new seed for each session, and only for that session
- the random library used `mersenne-twister` (MT19937) - which could be predicted if we have 624 numbers of 32 bits
- we have 192 bit numbers, so we only need 104 numbers to predict the next results
- we know the first 200 spins, since the alphabet is fixed and not shuffled per slot
- after the 200 round, each slot has the flag letter in index 0, so now if we know the number the whole algorithm could be reversed to extract the flag

so the steps are:
1. initial a new session with the server (delete your old one)
2. for the 200 first spins, just seed the MT19937 cracker\predictor, by reversing the server result to 192 bits number
3. in the 201, we could not know what the number that chosen by the server by the string result - but we can use our predictor
4. since all the letters of the flag is in index 0, we just observe  the numbers from the predictor and wait for `000000` in the relevant index

**References**:
- https://github.com/kmyk/mersenne-twister-predictor#mersenne-twister-predictor

**FLAG** 
 `CSA{I_L1K3_THE_TW1ST_4T_THE_END}`