const morse = require("morse-decoder");
const fs = require("fs");

// read book as buffer
let book = fs.readFileSync("book.txt");
// make array of uppercase words from the book, ignoring spaces and special chars
book = book.toString().toUpperCase().split(/\s/).map(x => x.replace(/[^a-z0-9]/gi, '')).filter(x => !!x);


const FULL_PATTERN = `x.xx...x.xxx..-xx-.xxxx.-.-xxx.-.x..x.xxxx..x.xxx.-.-.xx-.-xxx..-.xx.x.x.--x.xxx`;

function main() {
  let partialPattern = `x.xx...x.xxx..-xx-.xxxx.-.-`; // 2^13 options
  let options = getOptionsForPattern(partialPattern); // get all options from pattern

  console.log("options length:", options.length);
  console.log("book length:", book.length);

  // try to solve with the partial pattern
  getMatchesFromBook(partialPattern, options, 0);

  console.log('finish');
}

function getMatchesFromBook(pattern, options) {

  // iterate over array words
  for (let i = 0; i < book.length; i++) {

    // add some words toghether to match the pattern length (also partial)
    let word = book[i]; // the current word;
    let j = i + 1;
    while (word.length < pattern.length && book[j]) {
      word += book[j];
      j++;
    }

    // encode selected words to morse (remove spaces)
    let morseStr = morse.encode(word).replace(/\s/g, "");

    // compare the morseStr with any of our options

    for (const o of options) {
      if (morseStr.startsWith(o)) {
        console.log("found candidate", word);
        fs.appendFileSync('candidates.txt', word + '\n');
        // since its only partial, if we find a match - keep trying to get a full match
        if (testCandidate(FULL_PATTERN, morseStr)) {
          return getFullMatch(i)
        }
      }
    }
  }
}

function getFullMatch(i) {
  // we found the partial solution, lets try to find the whole phrase
  let word = book[i];
  let j = i + 1;
  morseStr = morse.encode(word).replace(/\s/g, "");
  // keep adding the next word each time, until we match the FULL_PATTERN
  while (testCandidate(FULL_PATTERN, morseStr)) {
    word += book[j];
    j++;
    morseStr = morse.encode(word).replace(/\s/g, "");
  }
  let finalResult = book.slice(i, j - 1);
  printFlag(finalResult);
  return;
}

function printFlag(result) {
  // the lowercase is because the original words in the book are lowercased.
  // THE FLAG IS THE SEQUENCE SEPARATED BY UNDERSCORES INSIDE CURLY BRACKETS AFTER UPPERCASE CSA
  console.log(`CSA{${result.join("_").toLowerCase()}}`);
}

function testCandidate(pattern, result) {
  for (let i = 0; i < result.length; i++) {
    const c = result[i];
    if (!(pattern[i] == 'x' || pattern[i] == c)) {
      return false;
    }
  }
  return true;
}

// build options array to hold all possible morse codes for a given pattern
function getOptionsForPattern(pattern) {
  let options = [];
  for (const char of pattern) {
    _addCharToOptions(options, char);
  }
  return options.map(x => x.join(''));
}

// helper to increase the options array with a given char
function _addCharToOptions(options, char) {
  // initial option
  if (!options.length) {
    if (char == "x") {
      options.push(["."], ["-"]);
    } else {
      options.push([char]);
    }
  } else {
    const total = options.length;
    for (let i = 0; i < total; i++) {
      const o = options[i];
      if (char == "x") {
        options.push([...o, "-"]);
        o.push(".");
      } else {
        o.push(char);
      }
    }
  }
}

main();