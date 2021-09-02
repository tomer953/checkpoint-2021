# Fun With Flags
180

Welcome to Dr. Sheldon Cooper and Dr. Amy Farrah Fowler's flags shop!

Where you can buy and sell some of our favorite flags.
Colors? Stripes? Stars? We've got them all!

We've given you some coins, don't spend them all at once :)
Hope you'll have Fun With Flags!

Disclaimer:
Dr. Sheldon Cooper, who created the shop, allowed only himself to buy certain flags, so don't be disappointed if you can't have all of them.
He also decided to log every transaction, in case anyone tries to buy the special flags that are not allowed, so don't try to trick him!

```nc fun-with-flags.csa-challenge.com 6666```


**Solution:**
We need to review the code and we found two bugs:

1. 
on line `181`:
```
flag_to_sell = None
for _ in range(amount):
```

should be reversed, because if we use the mass sell option (selling more than one item)
the `flag_to_sell` is not being reset, leading to a bug when we can sell the most expensive flag we have, than just press on invalid index
so `if flag_to_sell is not None:` is now not None, and we gain the selling coins over and over...


2. 
now that we have money, we exploit the second bug we found:
line 43:
`result += "star (total {}) - {:0.2f}.\n".format(total_stars, user_value / total_stars)`
if the `total_stars` is `0` and we still own some flags, we dividing by zero, causing to exception, allowing us to buy the CSA FLAG (we do not check for vip)


**FLAG**

`CSA{M4y_Th3Re_ALwaY5_8E_A_ST4R_0n_y0UR_fL4G}`