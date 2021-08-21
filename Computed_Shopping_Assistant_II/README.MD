
# Computed Shopping Assistant II
## 287

Welcome to Computed Shopping Assistant II

Sadly, some users found a way to abuse the system and use a secret coupon.
This time, we have added a new coupon that can't be revealed!

Note: the flag is in the format of CSA{...}

`nc csa-2.csa-challenge.com 2222`


differences from v1:

diffs:

`#define HIGH_DISCOUNT_AMOUNT 90`

`load_coupon("coupon_100.txt", 100);`

```
case TYPE_COUPON:
    if (item->coupon.have_entered)
    {
        if (item->coupon.discount_amount < HIGH_DISCOUNT_AMOUNT)
        {
            printf("(index %d) - %d%% OFF coupon - %s\n", i, item->coupon.discount_amount, item->coupon.code);
        }
        else
        { // need to be a little more discrete about special coupons
            printf("(index %d) - %d%% OFF coupon - *CENSORED*\n", i, item->coupon.discount_amount);
        }
    }
    break;
```