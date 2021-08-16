
// we look on all options to sum 15
let sum15Options = [
  [9, 5, 1],
  [9, 4, 2],
  [8, 6, 1],
  [8, 5, 2],
  [8, 4, 3],
  [7, 6, 2],
  [7, 5, 3],
  [6, 5, 4],
];

// count how many times each number appear in the above options
let counterPerNumber = {
  5: 4,
  2: 3,
  4: 3,
  6: 3,
  8: 3,
  1: 2,
  3: 2,
  7: 2,
  9: 2,
};
// it's hint us that 5 should be in the center, 2,4,6,8 in corners, and 1,3,7,9 in the middle

// if we spread the numbers 1-9 in the following way
// all we need is to play tic-tac-toe agains the computer (pretty easy) to force a tie
let board = [
  [6, 1, 8],
  [7, 5, 3],
  [2, 9, 4],
];
// csa{https://www.youtube.com/watch?v=NHWjlCaIrQo}