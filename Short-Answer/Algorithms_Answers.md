#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) It's O(n), because it increases linearly as the input (n) increases. There is only one while loop, which is O(n) also, and only one mutation on the stored counter (a).

b) It's O(n^2), because there is a loop nested inside another loop. Each loop is O(n), and we multiply the runtime complexity of each loop if they are nested.

c) It's O(log n), because as recursion happens, the input is reduced by 1.

## Exercise II

Thoughts:

    -endless floors
    -there is a break point floor, where eggs will start breaking if thrown
    -eggs are abundant
    -floor is the differentiator

    We want to find that break point. I'd do a binary search, find the middle of the building and see if the eggs break when thrown off that floor. If not, I'd search find a new middle between the old middle and the highest floor, and chuck the eggs of that floor. If they didn't break, I'd go higher, etc.

    Similarly, if the egg broke on that initial middle floor, I'd find a new middle floor by halfing the 1st floor with old middle. I'd chuck an egg off that floor to see if it breaks. If it does, I'd keep finding a new middle in the last lower half, etc.

    Eventually, I'd iterate (or recurse?) until I found the break point floor.

    What's important is finding the highest floor before the eggs start breaking.
