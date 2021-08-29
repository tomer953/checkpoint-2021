
### 4 first lines
```
0  1  2  3  4  5  6  7  8  9
1A 05 1B 03 AB AB EF 08 FF 80
1C B3 1D 91 BA CD EF 22 FF 80
1E 05 1F 05 CD EF EF 19 FF 80
1B 30 1D 08 DC BD EF 06 FF 80
```

### List of Registers:

`1A, 1B, 1C, 1D, 1E, 1F`

### List of Commands:

```
MOV     syntax: REG number          - move the number into the register

ADD     syntax: AB AB               - 05+03 = 0x08
SUB     syntax: BA CD               - B3-91 = 0x22
MUL     syntax: CD EF               - 05*05 = 0x19
DIV     syntax: DC BD               - 30/08 = 0x06

???     syntax: EF number           - unknown
???     syntax: FF 80               - unknown
```

MOV Commands found (column index 0-1, 2-3)
```
MOV 1A, 05
MOV 1B, 03
MOV 1C, B3
MOV 1D, 91
MOV 1E, 05
MOV 1F, 05
MOV 1B, 30
MOV 1D, 08
```

1A 05 1B 03 AB AB EF 08 FF 80
1C B3 1D 91 BA CD EF 22 FF 80
1E 05 1F 05 CD EF EF 19 FF 80
1B 30 1D 08 DC BD EF 06 FF 80

```
1A = 05
1B = 03
ABAB (ADD) 08
1C = B3
1D = 91
BA CD (SUB) 22
1E = 05
1F = 05
CD EF (MUL) 19
1B = 30
1D = 08
DB BD (DIV) 06



```