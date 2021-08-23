const fs = require("fs");
const axios = require("axios");
const dijkstrajs = require("dijkstrajs");
const product = require("cartesian-product");

const serverUrl = "http://memento.csa-challenge.com:7777/verifygame";

const boardGraph = {
  // row 0
  "0-0": { "0-1": 1, "1-0": 1 },
  "0-1": { "0-0": 1, "0-2": 1, "1-1": 1 },
  "0-2": { "0-1": 1, "0-3": 1, "1-2": 1 },
  "0-3": { "0-2": 1, "0-4": 1, "1-3": 1 },
  "0-4": { "0-3": 1, "0-5": 1, "1-4": 1 },
  "0-5": { "0-4": 1, "0-6": 1, "1-5": 1 },
  "0-6": { "0-5": 1, "0-7": 1, "1-6": 1 },
  "0-7": { "0-6": 1, "1-7": 1 },
  // row 1
  "1-0": { "0-0": 1, "2-0": 1, "1-1": 1 },
  "1-1": { "1-0": 1, "1-2": 1, "0-1": 1, "2-1": 1 },
  "1-2": { "1-1": 1, "1-3": 1, "0-2": 1, "2-2": 1 },
  "1-3": { "1-2": 1, "1-4": 1, "0-3": 1, "2-3": 1 },
  "1-4": { "1-3": 1, "1-5": 1, "0-4": 1, "2-4": 1 },
  "1-5": { "1-4": 1, "1-6": 1, "0-5": 1, "2-5": 1 },
  "1-6": { "1-5": 1, "1-7": 1, "0-6": 1, "2-6": 1 },
  "1-7": { "1-6": 1, "0-7": 1, "2-7": 1 },
  // row 2
  "2-0": { "1-0": 1, "3-0": 1, "2-1": 1 },
  "2-1": { "2-0": 1, "2-2": 1, "1-1": 1, "3-1": 1 },
  "2-2": { "2-1": 1, "2-3": 1, "1-2": 1, "3-2": 1 },
  "2-3": { "2-2": 1, "2-4": 1, "1-3": 1, "3-3": 1 },
  "2-4": { "2-3": 1, "2-5": 1, "1-4": 1, "3-4": 1 },
  "2-5": { "2-4": 1, "2-6": 1, "1-5": 1, "3-5": 1 },
  "2-6": { "2-5": 1, "2-7": 1, "1-6": 1, "3-6": 1 },
  "2-7": { "2-6": 1, "1-7": 1, "3-7": 1 },
  // row 3
  "3-0": { "2-0": 1, "4-0": 1, "3-1": 1 },
  "3-1": { "3-0": 1, "3-2": 1, "2-1": 1, "4-1": 1 },
  "3-2": { "3-1": 1, "3-3": 1, "2-2": 1, "4-2": 1 },
  "3-3": { "3-2": 1, "3-4": 1, "2-3": 1, "4-3": 1 },
  "3-4": { "3-3": 1, "3-5": 1, "2-4": 1, "4-4": 1 },
  "3-5": { "3-4": 1, "3-6": 1, "2-5": 1, "4-5": 1 },
  "3-6": { "3-5": 1, "3-7": 1, "2-6": 1, "4-6": 1 },
  "3-7": { "3-6": 1, "2-7": 1, "4-7": 1 },
  // row 4
  "4-0": { "3-0": 1, "4-1": 1 },
  "4-1": { "4-0": 1, "4-2": 1, "3-1": 1 },
  "4-2": { "4-1": 1, "4-3": 1, "3-2": 1 },
  "4-3": { "4-2": 1, "4-4": 1, "3-3": 1 },
  "4-4": { "4-3": 1, "4-5": 1, "3-4": 1 },
  "4-5": { "4-4": 1, "4-6": 1, "3-5": 1 },
  "4-6": { "4-5": 1, "4-7": 1, "3-6": 1 },
  "4-7": { "4-6": 1, "3-7": 1 },
};

function getPairs(board) {
  let pairs = [];
  for (let n = 1; n <= 20; n++) {
    let pair = [];
    for (let i = 0; i < board.length; i++) {
      for (let j = 0; j < board[i].length; j++) {
        if (board[i][j] == n) {
          pair.push([i, j]);
        }
      }
    }
    pairs.push(pair);
  }

  //   console.log(pairs);
  return pairs;
}

function allShortestPath(board) {
  let result = [];
  let pairs = getPairs(board);
  for (let i = 0; i < pairs.length; i++) {
    const pair = pairs[i];
    let a = pair[0];
    let b = pair[1];
    result.push(getShortestPath(a, b));
  }
  console.log(result);
}

function getShortestPath(a, b) {
  const path = dijkstrajs.find_path(
    boardGraph,
    `${a[0]}-${a[1]}`,
    `${b[0]}-${b[1]}`
  );
  //   console.log(path, path.length - 1);
  return path.length - 1;
}

async function checkBoard(level, board) {
  let url = `${serverUrl}?level=${level}&board=${board}`;
  let res = await axios.get(url);
  console.log(level, res.data);
  //   if (res.data) {
  //   }
}

function createBoard(dist) {
  let board;

  if (dist == 1) {
    board = [
      [1, 1, 2, 2, 3, 3, 4, 4],
      [5, 5, 6, 6, 7, 7, 8, 8],
      [9, 9, 10, 10, 11, 11, 12, 12],
      [13, 13, 14, 14, 15, 15, 16, 16],
      [17, 17, 18, 18, 19, 19, 20, 20],
    ];
  } else if (dist == 2) {
    board = [
      [1, 2, 1, 2, 3, 4, 3, 4],
      [5, 6, 5, 6, 7, 8, 7, 8],
      [9, 10, 9, 10, 11, 12, 11, 12],
      [13, 14, 13, 14, 15, 16, 15, 16],
      [17, 18, 17, 18, 19, 20, 19, 20],
    ];
  } else if (dist == 3) {
    board = [
      [1, 2, 3, 1, 2, 3, 4, 5],
      [8, 7, 6, 8, 7, 6, 13, 12],
      [14, 15, 16, 14, 15, 16, 5, 4],
      [9, 10, 11, 9, 10, 11, 12, 13],
      [17, 18, 19, 17, 18, 19, 20, 20],
    ]; // sometimes 1
  } else if (dist == 4) {
    board = [
      [1, 2, 3, 4, 1, 2, 3, 4],
      [5, 6, 7, 8, 5, 6, 7, 8],
      [9, 10, 11, 12, 9, 10, 11, 12],
      [13, 14, 15, 16, 13, 14, 15, 16],
      [17, 18, 19, 20, 17, 18, 19, 20],
    ];
  } else if (dist == 5) {
    board = [
      [1, 3, 5, 2, 4, 6, 7, 8],
      [19, 17, 14, 12, 10, 13, 11, 9],
      [2, 4, 6, 1, 3, 5, 18, 12],
      [20, 16, 18, 11, 9, 8, 16, 10],
      [14, 15, 19, 17, 20, 7, 15, 13],
    ];
  } else if (dist == 6) {
    board = [
      [9, 12, 14, 19, 18, 15, 20, 10],
      [15, 3, 1, 5, 6, 4, 2, 11],
      [18, 17, 13, 7, 8, 12, 14, 16],
      [6, 4, 2, 9, 10, 3, 1, 5],
      [8, 19, 20, 16, 11, 17, 13, 7],
    ];
  } else if (dist == 7) {
    board = [
      [1, 6, 8, 10, 11, 9, 7, 1],
      [2, 12, 14, 14, 15, 15, 13, 2],
      [3, 16, 16, 17, 17, 18, 18, 3],
      [4, 13, 19, 19, 20, 20, 12, 4],
      [5, 11, 9, 7, 6, 8, 10, 5],
    ]; // 7 and 1
  } else if (dist == 8) {
    board = [
      [1, 9, 7, 11, 11, 8, 10, 2],
      [2, 12, 12, 13, 13, 14, 14, 1],
      [3, 5, 15, 15, 16, 16, 6, 4],
      [4, 17, 17, 18, 18, 19, 19, 3],
      [6, 8, 10, 20, 20, 9, 7, 5],
    ]; // 8 and 1
  }

  let boardStr = Buffer.from(JSON.stringify(board)).toString("base64");
  console.log(boardStr);
  return boardStr;
}

function main() {
  let boardStr = createBoard(1);
  let board = JSON.parse(Buffer.from(boardStr, "base64"));
  //   console.log(board);

  allShortestPath(board);

  for (let i = 0; i < 25; i++) {
    checkBoard(i, boardStr);
  }
}

let res = product([
["I","R","D","M","V"],
["E","N","W","I","R"],
["E","N","W","I","R"],
["E","N","W","I","R"],
["B","K","T","F","O","X"],
["E","N","W","I","R"],
["F","O","X","A","J","S"]
]);
console.log(res.length);

// write results to file (with stream, faster)
var file = fs.createWriteStream("keys.txt");
file.on("error", console.error);

res.forEach((v) => file.write(v.join("") + "\n"));
file.end();

// main();

// level 0 - shortest 5 [g,p,y]
// level 1 - shortest 3 [e,n,w]
// level 2 - shortest 3 [e,n,w]
// level 3 - shortest 7 [i,r]
// level 4 - shortest 3 [e,n,w]
// level 5 - shortest 3 [e,n,w]
// level 6 - shortest 6 [h,"q","z"]
// level 7 - shortest 8 [a,j,s]
// level 8 - shortest 1 [c,l,u]
// level 9 - shortest 1 [c,l,u]
// level 10 - shortest 6 [h,q,z]
// level 11 - shortest 3 [e,n,w]
// level 12 - shortest 3 [e,n,w]
// level 13 - shortest 3 [e,n,w]
// level 14 - shortest 2 [d,m,v]
// level 15 - shortest 6 [h,q,z]
// level 16 - shortest 2 [d,m,v]
// level 17 - shortest 7 [i,r]
// level 18 - shortest 7 [i,r]
// level 19 - shortest 7 [i,r]
// level 20 - shortest 4 [f,o,x]
// level 21 - shortest 7 [i,r]
// level 22 - shortest 8 [a,j,s]
// level 23 - probably 9 [b,k,t]
// level 24 - shortest 2 [d,m,v]

flag = [4,2,2,6,2,2,5,7,0,0,5,2,2,2,1,5,1,6,6,6,3,6,7,8,1]