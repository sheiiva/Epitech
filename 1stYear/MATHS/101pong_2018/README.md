101pong
===

Time:       2 weeks

Team:       2

Language:   Python


The project
----
**Pong**, an arcade game developped in **1972** by **Ralph Baer (Atari)**, is the first ever successful video game. It was inspired by the very first video game, Tennis for Two, developped in 1958 by William Higinbotham onan oscilloscope.The goal of this project is to work on a 3D version of this game (or of theBreakoutgame...). Only one paddle will be considered, located in the (Oxy) plane (which is defined by the equationz= 0).

**Your program must print**:
* The velocity vector of the ball
* The coordinates of the ball after a given amount of time
* The angle at which the ball will hit the paddle (if it will actually hit it, at anytime from t = 0)

## USAGE:

```
>> ./101pong x0 y0 z0 x1 y1 z1 n
```

#### DESCRIPTION
* x0  ball abscissa at time t - 1
* y0  ball ordinate at time t - 1
* z0  ball altitude at time t - 1
* x1  ball abscissa at time t
* y1  ball ordinate at time t
* z1  ball altitude at time t
* n   time shift (greater than or equal to zero, integer)


Author **Corentin COUTRET-ROZET** and **Lilian VERLHAC**