const solutions = [
    [3, 1, "v"],
    [5, 2, "<"],
    [4, 0, "v"],
    [4, 3, "^"],
    [2, 0, ">"],
    [4, 0, "v"],
    [4, 5, "^"],
    [6, 4, "<"],
    [3, 4, ">"],
    [6, 2, "v"],
    [6, 4, "<"],
    [1, 4, ">"],
    [2, 6, "^"],
    [2, 3, "v"],
    [4, 6, "<"],
    [2, 6, "^"],
    [2, 1, "v"],
    [0, 2, ">"],
    [3, 2, "<"],
    [0, 4, "^"],
    [0, 2, ">"],
    [3, 4, ">"],
    [5, 4, "^"],
    [5, 2, "<"],
    [3, 2, "<"],
    [1, 2, "v"],
    [1, 4, ">"],
    [3, 3, ">"],
    [3, 5, "^"],
    [2, 3, ">"],
    [5, 3, "<"]
]


let pythonOutput = `
[(1, 3, 'v'),
 (2, 1, '>'),
 (0, 2, 'v'),
 (0, 4, '<'),
 (2, 3, '<'),
 (2, 0, '>'),
 (2, 4, '^'),
 (2, 6, '<'),
 (3, 2, '^'),
 (0, 2, 'v'),
 (3, 0, '>'),
 (3, 2, '^'),
 (3, 4, '<'),
 (3, 6, '<'),
 (3, 4, '^'),
 (0, 4, 'v'),
 (4, 2, '^'),
 (1, 2, 'v'),
 (4, 0, '>'),
 (4, 3, '<'),
 (5, 4, '^'),
 (4, 6, '<'),
 (6, 2, '^'),
 (3, 2, 'v'),
 (6, 4, '<'),
 (6, 2, '^'),
 (4, 1, '>'),
 (4, 3, '>'),
 (2, 4, 'v'),
 (4, 5, '<'),
 (5, 3, '^')]`

 let toJson = pythonOutput.replace(/\(/g, "[").replace(/\)/g, "]").replace(/\'/g, '"');
 toJson = JSON.parse(toJson);
 toJson = toJson.map(x => [x[1], x[0], x[2]])
 console.log(toJson);
 console.log(JSON.stringify(toJson));