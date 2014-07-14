Elevator Optimization Algorithm
=============

This algorithm is designed to minimize the total waiting time 
of all individuals waiting in a building. Given there are equal
number of people on each floor, with a uniform appearance of individuals
to use the elevator at each floor. Assuming there are several
hours a day which are "rush-hour times," the algorithm is designed to 
provide the most "fair" way to destribute the elevators to the various floors.

That is to say, the algorithm allocates resources in an attempt
to make the average wait time per elevator to be the exact same per floor.


The algorithm requires the following variables:

* Number of Floors
* Number of Elevators

The algorithm assumes the following constants. 
The variables can be adjusted, but do not effect the algorithm:

* Same Number of Elevator Users per Floor - 100 individuals
* Speed of Elevator (ignoring speed-up or slow down) - 5 seconds per floor
* Waiting Time per Floor (onboarding and departing) - 20 seconds

This program/algorithm was written for austingwalters.com. It is more or less
a simple resource allocation algorithm and is a common interview question. 

If you have any suggestion or improvements, don't hesitate to contribute.