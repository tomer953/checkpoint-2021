# Pass it on

200

Help!
My grandpa lost his password and cannot seem to recall it!

He is very secretive and will not elaborate, but I have heard him complain several times about how long it takes the program to verify his password.
Weird right?

- [screenshot](../../images/pass-it-on.png?raw=true)

**Solution**:

the description is a very solid hint for **timing attack**

1. extract the flag length from the source code (ie: with Ida)
    - optional: brute force the flag length in the same way we describe below
2. send `AAAAAAAAAAAAAAAAAAAAAAAAAAA` and measure the response time
3. replace the first letter with every another ascii char, take the maximum response time, choose that letter, and move on

for example the first 4 iteration will give you:

- [screenshot](../../images/pass-it-on-sol.png?raw=true)

```
CAAAAAAAAAAAAAAAAAAAAAAAAAA
CSAAAAAAAAAAAAAAAAAAAAAAAAA
CSAAAAAAAAAAAAAAAAAAAAAAAAA
CSA{AAAAAAAAAAAAAAAAAAAAAAA
```

**Flag**:

`CSA{1_V1LL_me55_w1Th_t1mE!}`