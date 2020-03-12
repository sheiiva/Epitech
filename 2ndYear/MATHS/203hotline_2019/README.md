203hotline
===

Time:       2 weeks

Team:       2

Language:   Python


The project
----
Uncle Luigi runs a 25-phone hotline in Pondicherry. He reckons **3500 people** could possibly call during each **8-hour day**, and would like to know the probability of an **overload** (that is, the probability of no linebeing available), depending on the average duration of calls.
The random variable representing the number of people calling at a given time follows the **binomial distribution**, with calls being independent from each other. You’re also thinking about estimating the binomial ditribution with a **Poisson distribution**, so it can be used on a larger scale.

Your first task is to compute the binomial coefficient (n k) given *k* and *n* (emphasizing the computation speedand stack optimization).

Your second task is to compare the binomial and Poisson distributions, given the average duration of calls, by printing:
* The probabilities of getting *n* simultaneous calls (forni *n* creasing from 0 to 50)
* The probability of an overload
* The computation time

## USAGE:

```
>> ./203hotline [n k | d]
```

#### DESCRIPTION
* n       value for the computation of C(n, k)
* k       k value for the computation of C(n, k)
* d       average duration of calls (in seconds)

Author **Corentin COUTRET-ROZET** and **PATRICIA MONFA-MATAS**