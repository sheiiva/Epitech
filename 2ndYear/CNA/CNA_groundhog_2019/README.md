Groundhog
===

Time:       4 weeks

Team:       2

Language:   Python


The project
----
Several industries rely on weather forecasts: insurance, farming, construction, airlines, shipping, power gen-eration and supply, drinks, clothing, sports, etc... In fact, it’s quite challenging to find a business which is not affected by climatic conditions.
That’s why the weather forecasting market is so burgeoning. Despite popular opinion, weather forecasts are becoming more accurate than ever. Thanks to ingenious andtalented people like you, who use smart tools to get better, faster and stronger predictions than the others.

Your job is to **extract some relevant information** from the data received in real-time on standard input (each float representing a temperature), **in order to detect weather aberrations** (droughts, severe colds, hurricanesor any other extreme climatic condition whatsoever) as soon as possible.

#### Warning
* **aberration**: deviation from what is normal, expected, or usual.
* **forecast**: a forecast is a statement of what is expected to happen in the future, especially in relation toa particular event or situation.

> collinsdictionnary.com


To do so, your program must, given a number of days (calledperiod) as argument:

1. **wait** for the next value to be written on the standard input,
2. output, once enough data has been gathered, some technical indicators:
   1. the **temperature increase average**, *g* , observed on the last period
   2. the **relative temperature evolution**,*r*, between the last given temperature and the temperatureobserved n-days ago
   3. the **standard deviation**,*s*, of the temperatures observed during the last period
   4. when appropriate, an **alert** as soon as it detects **a switch in global tendency**
3. return to the first step, until the **STOP** keyword is read


## USAGE:

```
>> ./groundhog period
```

#### DESCRIPTION
* period        the number of days defining a period

Author **Corentin COUTRET-ROZET** and **PATRICIA MONFA-MATAS**