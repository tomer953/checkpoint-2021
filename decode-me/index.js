const { decode } = require('hi-base32');
const xor = require('bitwise-xor');

// inputs
let str = `WFKZLTABVKWVLXGMASVPYVP2ZRTKVHKV6XGBJKVEKX44YCVKXBK4XTBDVKSVL2WMACVLOVPEZQJ2VHCV`;
let xorKey = 'cc55aa';


// base32 decode
let s1 = decode.asBytes(str);
let s1HexStr = bufferToHex(s1);
console.log('base32', s1HexStr);

// xor (repeat)
let paddedXorKey = xorKey.padEnd(s1HexStr.length, xorKey); // CC55AACC55AACC55AA....
let xorBuffer = xor(new Buffer.from(s1HexStr, 'hex'), new Buffer.from(paddedXorKey, 'hex'));
let result = xorBuffer.toString();
console.log('xor', result);

// ceaser
result = cipherRot13("}?TavQ0P3Q_AhS_tavi@U{NFP");
console.log('ceaser 13', result);

// reverse string
result = result.split('').reverse().join('');
console.log('reverse', result);


// print buffer as hex string
function bufferToHex(buffer) {
    return Buffer.from(buffer).toString('hex');;
}

// ROT-13 Cipher (shifting 13 times)
function cipherRot13(str) {
    str = str.toUpperCase();
    return str.replace(/[A-Z]/g, rot13);

    function rot13(correspondance) {
        const charCode = correspondance.charCodeAt();
        //A = 65, Z = 90
        return String.fromCharCode(
            ((charCode + 13) <= 90) ? charCode + 13
                : (charCode + 13) % 90 + 64
        );

    }
}