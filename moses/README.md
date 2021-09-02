## Moses
100

Grab that flag will you?

**Solution**:

we got two files:

1. moses.txt
2. book.txt

first we decode the moses.txt fill with Morse code:

```
HELLO WE GOT THE FOLLOWING MESSAGE FROM ONE OF OUR SPIES
BUT SHE COULD NOT SPACE BETWEEN LETTERS AND WORDS
WE KNOW SHE WAS TRYING TO SEND A SEQUENCE OF WORDS AS THEY APPEAR IN THIS BOOK
HELP US FIND THE SEQUENCE UNFORTUNATELLY
SOME OF TONES WERE NOT CLEAR SO WE REPLACED THEM WITH X BECAUSE WE WERE NOT SURE IF IT WAS A DOT OR A LINE
----------------------------------------
x.xx...x.xxx..-xx-.xxxx.-.-xxx.-.x..x.xxxx..x.xxx.-.-.xx-.-xxx..-.xx.x.x.--x.xxx
----------------------------------------
THE FLAG IS THE SEQUENCE SEPARATED BY UNDERSCORES INSIDE CURLY BRACKETS AFTER UPPERCASE CSA
```

not we build all the options for the morse code,
replace `x` with `.` or `-` - but this has too many options `2^39`
so we take only partial string with less options - and look for candidates in the book


ie:
 `x.xx...x.xxx..-xx-.xxxx.-.-` which has `2^13` options

 foreach option, we look a sequence of words in the book.txt that is equal to that option in Morse code.
 
 if we found a match - we test it against the full pattern.


**Flag**:

`CSA{still_other_of_them_that_are_gone_before}`