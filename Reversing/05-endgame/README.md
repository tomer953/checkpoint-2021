# Endgame

300

This guy Thanos snapped his fingers and now the flag is scattered across the universe.
Can you be the hero that saves the world?

**Solution**:

we open the flag file with hex editor,
we look at 10 bytes in a row, and we can see the following pattern

```
1A 05 1B 03 AB AB EF 08 FF 80
1C B3 1D 91 BA CD EF 22 FF 80
1E 05 1F 05 CD EF EF 19 FF 80
1B 30 1D 08 DC BD EF 06 FF 80
1A 01 1B 02 CD AB 1B 05 CD AB
1C 1E CD AC 1E B2 1F 05 CD EF
CD AE 1B E7 1C C6 AB BC 1D C1
1E 62 AB DE 1F AD AB DF AB BD
AB AB 1B 04 CD AB 1B FA 1C FA
AB BC CD AB 1B F1 1C C8 AB BC
AB AB 1D 7D CD AD 1B FA 1C 04
CD BC 1F 68 BA BF CD AB 1C FD
AB AC 1C 64 CD AC 1B 0A 1C 40
CD BC CD AB 1B F3 1C 3A 1D DC
AB CD AB BC AB AB 1F 04 CD AF
1B 05 1C 64 CD BC CD AB 1B 03
1C 64 CD CB CD BC 1D 32 BA BD
CD AB 1F 03 CD CF 1B 44 AB CB
CD AC 1B 06 1C 0A CD BC CD BC
CD BC CD BC 1D 7B AB BD AB AB
1B C8 CD AB CD BC 1F 02 DC BF
1C 73 BA BC CD AB 1C 3E AB BC
AB AB CD FF CD AF 1C 35 AB BC
1D 02 DC BD CD AB 1B F9 AB AB
1C 0A CD AC DC CD AB AC CD AF
1B 01 AB AB 00 00
```

### 4 first lines
```
0  1  2  3  4  5  6  7  8  9
1A 05 1B 03 AB AB EF 08 FF 80
1C B3 1D 91 BA CD EF 22 FF 80
1E 05 1F 05 CD EF EF 19 FF 80
1B 30 1D 08 DC BD EF 06 FF 80
```

we understand this could be some assembly op codes,
but for a language that made only for this challange.
so it must be something simple

we look in index 0 and index 2 and we assume its registers:

### List of Registers:

`1A, 1B, 1C, 1D, 1E, 1F`

in index 1 and 3, its data that moves to the registers


### List of Commands:

```
MOV     syntax: REG data             example: 1A 05           - 1A = 0x05

ADD     syntax: AB [XY]              example: AB CD           - 1C = 1C + 1D
SUB     syntax: BA [XY]              example: BA CD           - 1C = 1C - 1D
MUL     syntax: CD [XY]              example: CD EF           - 1E = 1E * 1F
DIV     syntax: DC [XY]              example: DC BD           - 1B = 1B / 1D

???     syntax: EF number           - unknown
???     syntax: FF 80               - unknown
EOF     syntax: 00 00
```


from here we can just parse 4 bytes each time, and apply the operands

it can be memory assignment, or some math operand

in the end, we look at the final memory state:

```
1A:89490564489314326449816467341755769981
1B:1
1C:5
1D:2
1E:98
1F:4
```

1A looks like the flag, so we convert it to hex number, then to string, and we get the flag.


**Flag**:

    `CSA{cs@5s3mbl3d}`