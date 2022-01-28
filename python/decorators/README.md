# Decorators

## Implementation

Decorators create high readability for high order functions. The decorator I have made, called ```@func_duration``` can be used to
decorate any function. It will return the time it takes to execute the decorated function. At first, the necessary syntax was not completely clear in order to create a working decorator, but after achieving the final product, the concept is fairly simple.

## func_duration

This decorator makes use of the python ```timeit``` module, which provides numerous methods for timing bits of code. The timer method initalizes with a number value of 1,000,000, which means it would track the time it takes to run a bit of code 1 million times. Due to the very fast nature of computing, the smallest changes in computing power may throw off accurate readings, unless large numbers are used/averaged. To find a balance between overburdening the cpu and getting accurate timer readings, I elected to only run each tested function 10 times and increasing the load on the tested function via its arguments (eg: make_list(250000) would make a list from 1-249999 ten times).

## Testing

Testing proved to be difficult due to the tiny fluctuations in computing speed. Tests I expected to pass easily would fail sometimes, and pass sometimes. I'll have to revisit ways to make better tests or more accurate time readings.
