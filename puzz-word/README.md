
# Puzz-word
300

One of my colleagues just loves puzzles.
He wrote this API that you can send and get a puzzle, and if you can solve it, you get the secret key to his bitcoin fortune.
We couldn't get it :(
Can you?

You can try it here:
https://puzzword.csa-challenge.com/help


- [screenshot](../images/puzz-word-help.png?raw=true)

**Input example:**

```
0: "  ...  "
1: "  ...  "
2: "......."
3: "...O..."
4: "......."
5: "  ...  "
6: "  ...  "

puzzle_id: "c5e41811-14e4-4bd6-9f4c-ab28af7fe823"

0: "  OOO  "
1: "  OOO  "
2: "OOOOOOO"
3: "OOO.OOO"
4: "OOOOOOO"
5: "  OOO  "
6: "  OOO  "
```


**Solution:**

- Make reuse of some java solver found on github
- Modify the Java source code to support multiple initial points
- add all the logic to communicate with the server and parse jsons
- finally the flag is the first letter of each solving message


**References**:
- https://github.com/mkhrapov/peg-solitaire-solver

**FLAG** 
 `CSA{In_Th3OrY_wE_tRuST}`


