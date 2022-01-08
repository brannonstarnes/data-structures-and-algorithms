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

Phew, it looks like there's a lot going on here! Fear not, we'll take it one bite at a time.
