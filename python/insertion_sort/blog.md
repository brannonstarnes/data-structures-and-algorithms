# Insertion Sort

Insertion sort is a sorting algorithm that
starts at the 1th index of a list and decides where the current index in question should be placed in relation to all previous indexes. It traverses the list one time only.

### Ok, what?

Let's take a look at the pseudocode for the Insertion Algorithm, then go through it visually.

`InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp

`

As we can see above, the function takes in a list of integers to sort, the  **_for_** loop is initialized with a counter **_i_** (which designates our current count in the length of the list) set to 1 and **_j_** (which determines which indexes are being compared) is always initialized one index space behind i (or i-1).

![diagram 1](<./insertion_sort(1).png>)

Inside the **for** loop is a **while** loop. The while loop is where all the magic starts to happen.

First, since the temp value (from the i position) is less than j, but comes **after** j, the value at j+1 will be reassigned to j's value. This means the 4 would have been lost had we not saved it to a temp variable.

![diagram 2](<./insertion_sort(2).png>)

After that, j cannot be reduced below zero (thanks while loop) and is set to the value of the next index position (in this case, 8). The for loop is revisited, i then increments up to 2 and stores it's value in temp, and j is set to 1.

![diagram 3](<./insertion_sort(3).png>)

Now the while loop starts again. However, since j is greater than 0 but temp (whose value is now 23) is NOT less than j (whose value is 8), the code contained within the while loop is not evaluated and the 23 remains in its current position. The whole process starts over.

![diagram 4](<./insertion_sort(4).png>)

![diagram 5](<./insertion_sort(5).png>)

Once again, since 16 is less than 42 (temp < arr[j]), the while loop is entered. The 42 is reassigned to 16's spot, so the 16 is lost, only to be stored in 'temp'. Now... j becomes j - 1 (index 2 in this case.) Since temp is less than arr[j] (16 < 23), the reassignment shuffle happens again.

![diagram 6](<./insertion_sort(6).png>)

Again, j is decremented and compared to temp.

![diagram 7](<./insertion_sort(7).png>)

The 23 is reassigned to the the 'empty' index.

![diagram 8](<./insertion_sort(8).png>)

![diagram 9](<./insertion_sort(9).png>)

j is decremented and compared to temp. Since temp is NOT less than 8, the while loop is exited.

![diagram 10](<./insertion_sort(10).png>)

i, j, and temp are reassigned back in the for loop.

![diagram 11](<./insertion_sort(11).png>)

Comparisons again take place, and since 42 is greater than 15, it moves into 15's index. Good thing 15 was held in 'temp'.

![diagram 12](<./insertion_sort(12).png>)

The while loop takes us down the list to find a spot where temp is NOT less than j...

![diagram 13](<./insertion_sort(13).png>)

![diagram 14](<./insertion_sort(14).png>)

Until temp finally find's it's home, and the list is properly sorted.
