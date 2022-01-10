# Challenge Summary

Create an Animal Shelter using Queue/Pseudoqueue methods to place and remove dogs and cats by first-in-last-out (FIFO) rules.

## Whiteboard Process

[whiteboard](./animal_shelter.png)

## Approach & Efficiency

Approach is to use two Stacks to manage the Queue. Push, Pop, and Peek methods will be used to manage data in the Stacks in conjuction with the PseudoQueue methods.

## Solution

<!-- Show how to run your code, and examples of it in action -->

Two queues are used in the animal shelter: one for dogs and one for cats. Animals will be added to their specific queue using the enqueue method, taking in a Dog or Cat object, including the name. (ex. shelter.enqueue(Dog("Champ"))). Requesting an animal is accomplished by passing in 'cat' or 'dog' to the shelter's dequeue method (ex. shelter.dequeue('cat')).
