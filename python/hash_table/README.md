# Hashtables

<!-- Short summary or background information -->

Creates a Hashtable class which can be used to store and quickly retrieve data via key/value recall.

## Challenge

<!-- Description of the challenge -->

Create a Hashtable class with the instance methods that allow the user to add key/value pairs, determine if key is already present, get a value from a key input, and hash a key.

## Approach & Efficiency

<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

Retrieval of Hash Table Values is an O(1) operation.

## API

<!-- Description of each method publicly available in each of your hashtable -->

-   .add(self, key, value) - adds a new key/value pair to the table as a Node in a Linked List. Returns nothing.
-   .contains(self, key) - takes and hashes a key, checks associated bucket for the key value. Returns a boolean.
-   .get(self, key) - takes a key, returns the associated value.
-   .hash(self, key) - takes a key, passes it through hashing algorithm, result determines the bucket 'address' where the data will be stored.
