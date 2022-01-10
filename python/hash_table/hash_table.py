from linked_list.linked_list import LinkedList, Node

class HashTable():
    def __init__(self, size=1024):
        self.buckets = [None] * size

    def add(self, key, value):
        bucket_location = self.hash(key)
        drop = self.buckets[bucket_location]
        if drop == None:
            bucket_list = LinkedList()
            bucket_list.head = Node({key: value})
            drop = bucket_list.head
        else:
            drop.next = Node({key:value})

    def get(self, key):
        bucket_location = self.hash(key)
        value = ((self.buckets[bucket_location])[key])
        return value

    def contains(self, key):
        comparator_bucket = self.hash(key)
        drop = (self.buckets[comparator_bucket])
        if drop != None and drop.includes(key) :
            print("True")
            return True
        print("False")
        return False

    def hash(self, key):
        # add together ascii values of each char
        ascii_total = 0
        for i in str(key):
            val = ord(i)
            ascii_total += val
            # multiply by a prime number
        primed = ascii_total * 599
        # modulus by the size
        result = primed % 1024
        return result


