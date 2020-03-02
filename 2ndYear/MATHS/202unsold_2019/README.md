202unsold
===

Time:       2 weeks

Team:       2

Language:   Python


The project
----
Steven is a suit-seller in Mississippi. Once a year, he gets rid of his unsold stock, selling separately jackets and trousers, at *$10*, *$20*, *$30*, *$40* and *$50*.
He’d like to know how much each piece of clothing is likely to yield (expected value and variance).
Steven gave his statistician friend a mission: to deduce from his past results the probability to sell a **$x jacket** and **$y trousers** together.

It appears that the probability is defined by the following formula (**a** and **b** being integers greater than 50, depending on the economic climate):

    (a−x)(b−y)(5a−150)(5b−150)

Let’s call **X**, **Y** and **Z**, respectively, the random variables that represent “**the price of a sold jacket**”, “**the price of sold trousers**” and “**the price of a sold suit**”. Given the values of *a and *b*, your software must print:
* an array summing up the joint law of(X, Y), and the marginal laws of X and Y
* an array summing up the law of Z
* expected values and variances of X, Y and Z

## USAGE:

```
>> ./202unsold a b
```

#### DESCRIPTION
* a       constant computed from past results
* b       constant computed from past results

Author **Corentin COUTRET-ROZET** and **PATRICIA MONFA-MATAS**