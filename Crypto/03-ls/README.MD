# ls
299

Boss wanted to give people access to only see the directories list in a filesystem.

Now you can run anything on my OS... so long as it's ls (with parameters).
Send the commands in one or more files, then zip that file. I only accept zips, everything else is inefficient.

I'll verify that you aren't playing games, if I see a command that isn't ls, I'm not running it.
I don't like redundancy, so I'll save the hash of the zips that were already verified...using the best hash algorithm of them all: MD5!

POST to:
https://ls.csa-challenge.com/upload-zip


**Solution**:

1. make dual zip of `ls` and `cat flag.txt` with this asm:

- https://github.com/corkami/collisions/blob/master/scripts/zip.asm

2. find collision with this script:

- https://github.com/cr-marcstevens/hashclash/blob/master/scripts/poc_no.sh
(run twice to fill the template)

**References**:

- https://github.com/corkami/collisions#unicoll-md5
- https://github.com/cr-marcstevens/hashclash


FLAG:

`CSA{K1LL_MD5_A1r34dy_p1z}`