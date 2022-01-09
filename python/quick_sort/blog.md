# Quick Sort

#### Author: Brannon Starnes

Today we will be looking at yet another sorting algorithm: QuickSort! Just like MergeSort, QuickSort uses a "divide and conquer" approach to sorting out those pesky, unorganized lists. Let's break it down.

First, let's "talk it out". Let's say you have five identical looking spheres sitting on a table in front of you and you want to sort them by their weight, from least to greatest, left to right. They range from 'light-as-a-feather' to 'I-can-barely-move-it'. To get them sorted by weight, you have decided to start by selecting one sphere at random. This sphere will be the benchmark by which all other spheres will be tested. We will call it the 'pivot', and it seems to have a middle-of-the-road weight to it. So, going down the line, you pick up the first sphere, at the far left. It is obviously lighter than the pivot, so you place it back to the left. The next one feels a bit heavier than the pivot, so you place it to the right. The next one is also heavier than the pivot, so to the right it goes. and the last one, definitely lighter. To the left with you.

Now at this point, all you know is that the pivot can be placed back into the line, and it is in the **_correct_** position. In this case, dead center. The spheres to the left and right of center sphere, however, have not found their homes yet. So, how about we do it all over again for both the left and right side? (_COugh cOUGH reCursion_)

Ahem, excuse me.

Now, to the **_bones_** of this whole operation...the psuedo-code.

```
ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right.
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp
```

Phew, it looks like there's a lot going on here! Fear not, we'll take it one bite at a time. The first function defined, called QuickSort, defines the boundaries of left and right based on where the pivot will be. It takes in an array, or list, as well as left and right (think start and end of list).

Partition takes all the same arguments and sets the pivot as the last element of the list, or the RIGHTmost. In order to track what index is currently the end of the low side, low is set to left -1 and will be incremented every time an element is moved to the left. That being accomplished, we can now compare all items in the list to our pivot. Anything that is lower than the pivot is taken from its current position and placed on the left side (think left[0]), swapping places with whatever element happened to be in that 0th index position. If the item being compared is NOT lower than the pivot, it is ignored (not moved to left).

Lastly, Swap is a basic variable swapping function that allows a variably to be redefined without losing any data.

This will continue until all elements of the list have had an opportunity to be compared and placed into the correct position.

Now, let's get visual!

![sorted final](./quick_sort.png)

As you can see in the diagram, the pivot is selected and its value is compared again the rest of the list. Anything larger moves to the right of the pivot, less to the left. Once each round of comparisons is completed the index position of the pivot is 'locked in'. Once everything is locked in and there's nothing else to compare to, you're sorted!
