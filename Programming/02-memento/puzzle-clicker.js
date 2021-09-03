let boardStr = "W1szLDYsMiwxMCw4LDMsMTgsNV0sWzE1LDEsMTMsMTYsMjAsMSwxNSwxMF0sWzE5LDcsNCwxNCw0LDE3LDgsMTFdLFs2LDEyLDE5LDE2LDksMTMsMTEsMTddLFs3LDE0LDksMjAsNSwyLDEyLDE4XV0=";
let board = JSON.parse(atob(boardStr));


console.log('start...');
function getPairs(board) {
    console.log(board);
    let pairs = []
    for (let n = 1; n <= 20; n++) {
        let pair = [];
        for (let i = 0; i< board.length; i++) {
            for (let j = 0; j < board[i].length; j++) {
                if (board[i][j] == n) {
                    pair.push([i,j]);
                }
            }
         }
       pairs.push(pair);
    }

//     console.log(pairs);
    return pairs;
}


function clickOnPairs() {
    let pairs = getPairs(board);
    for (let i = 0; i< pairs.length; i++) {
        const pair = pairs[i];
        let a = pair[0];
        let b = pair[1];
        setTimeout(() => { document.getElementById(`${a[0]}-${a[1]}`).click(); }, i * 100);
        setTimeout(() => { document.getElementById(`${b[0]}-${b[1]}`).click(); }, i * 100 + 100);
    }
    return pairs
}

clickOnPairs();