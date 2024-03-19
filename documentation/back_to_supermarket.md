# Back to the supermarket

Your task is to implement the code for a checkout system that handles pricing schemes such as “apples cost 50 cents, three apples cost $1.30.”

In a normal supermarket, things are identified using Stock Keeping Units, or SKUs. 

In our store, we’ll use individual letters of the alphabet (A, B, C, and so on). 

Our goods are priced individually. In addition, some items are multipriced: buy `n` of them, and they’ll cost you `y` cents. 

For example, item `A` might cost 50 cents individually, but this week we have a special offer: buy three `A` and they’ll cost you $1.30. 

In fact this week’s prices are:

| Item | Unit Price | Special Price |
| ---- | ---------- | ------------- |
| A    | 50         | 3 for 130     |
| B    | 30         | 2 for 45      |
| C    | 20         |               |
| D    | 15         |               |



Our checkout accepts items in any order, so that if we scan a B, an A, and another B, we’ll recognize the two B’s and price them at 45 (for a total price so far of 95).  

Because the pricing changes frequently, we need to be able to pass in a set of pricing rules (`items_pricing`) each time we start handling a checkout transaction.

Here’s a set of acceptance tests for a python implementation.

```python
 assert price(items_pricing, "") == 0
 assert price(items_pricing, "A") == 50
 assert price(items_pricing, "AB") == 80
 assert price(items_pricing, "CDBA") == 115
 assert price(items_pricing, "AA") == 100
 assert price(items_pricing, "AAA") == 130
 assert price(items_pricing, "AAAA") == 180
 assert price(items_pricing, "AAAAA") == 230
 assert price(items_pricing, "AAAAAA") == 260
 assert price(items_pricing, "AAAB") == 160
 assert price(items_pricing, "AAABB") == 175
 assert price(items_pricing, "AAABBD") == 190
 assert price(items_pricing, "DABABA") == 190
```

