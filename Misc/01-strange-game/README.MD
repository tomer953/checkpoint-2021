# Strange Game
100

It's just winning a simple game.
What could go wrong?

`nc strange-game.csa-challenge.com 4444`


- [screenshot](../../images/strange-game.png?raw=true)


**Solution:**

1. create all combinations of 3 numbers, which sums to 15:
```
  9, 5, 1
  9, 4, 2
  8, 6, 1
  8, 5, 2
  8, 4, 3
  7, 6, 2
  7, 5, 3
  6, 5, 4
```

2. count how many times each number apper:
```
  5: 4
  2: 3
  4: 3
  6: 3
  8: 3
  1: 2
  3: 2
  7: 2
  9: 2
```

3. that hints us to create a magic square of 3x3 and sum 15, with 5 in the middle:
```
[ 8 1 6 ] 
[ 3 5 7 ] 
[ 4 9 2 ] 
```

4. now we can just play tic-tac-toe against the pc, easy to force a tie.

**FLAG** 

    `CSA{https://www.youtube.com/watch?v=NHWjlCaIrQo}`