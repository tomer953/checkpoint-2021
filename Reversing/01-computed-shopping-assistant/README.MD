# Computed Shopping Assistant
200

Welcome to Computed Shopping Assistant!

The place where you can manage your shopping cart, and get substantial discounts with our special promotion coupons!
We have given all CSA candidates a free 10% OFF coupon:

NOT_A_FLAG{I_4M_A_N3WB1E}

Enjoy!

Please be aware that the system is not perfect, so don't go around buying loaves of soup...


`nc csa.csa-challenge.com 1111`


- [screenshot](../../images/shopping-assistant.png?raw=true)


**Solution:** 

we found two bugs:

1. 

in `shopping_cart.c` line 51:


```
	else if (((item->type == TYPE_BREAD) && (item->grocery_item.amount_loaves > 0)) || ((item->type == TYPE_PASTA) && (item->grocery_item.amount_kilograms > 0)) ||
			 ((item->type == TYPE_SOUP) && (item->grocery_item.amount_liters > 0)) || ((item->type == TYPE_DRINK) && (item->grocery_item.amount_liters > 0)) ||
			 ((item->type == TYPE_VEGETABLE) && (item->grocery_item.amount_kilograms > 0)) || ((item->type = TYPE_FRUIT) && (item->grocery_item.amount_items > 0)))
	{
		return true;
	}
	else if ((item->type = TYPE_COUPON))
	{
```

we have:

`item-type = TYPE_FRUIT` istead of `==`

`item-type = TYPE_COUPON` instead of `==`


2.

each item in the shopping cart is a `union` of coupon and and regular item (shared memory)


```
struct shopping_cart_item {
	enum item_type type;
	union {
		struct coupon_item coupon;
		struct grocery_item grocery_item;
	};
};
```

it cause that the property `amount_of_kilogram` is changing the `have_entered` of a coupon


**Steps to solve:**
- `5` - apply coupon - insert `bla`
    - this loads the first two coupons two index 0 and index 1
    - index 1 is the flag
- `2` - edit index `1` and insert `amount_of_kilogram` to `1`
    - this update the coupon `have_entered` to `1`
- `2` - edit index `1` and insert `Amount of items` to `0`
- `2` - edit index `1` - now since the amount is 0, the if contidion will be false, and will convert the item to a coupon
- `4` - thats it, we can see the coupon code in the description



**Flag**:

`CSA{iN_L1nuX_1T_W0UlDnT_H4PP3N}`