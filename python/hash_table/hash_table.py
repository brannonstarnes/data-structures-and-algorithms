from linked_list.linked_list import LinkedList, Node

class HashTable():
    def __init__(self, size=1024):
        self.buckets = [None] * size

    def add(self, key, value):
        bucket_location = self.hash(key)
        bucket = self.buckets[bucket_location]
        if bucket == None:
            bucket = LinkedList()
            self.buckets[bucket_location] = bucket
        bucket.append((key,value))

        # else:
        #     bucket.next = Node({key:value})

    def get(self, key):
        bucket_location = self.hash(key)
        value = ((self.buckets[bucket_location])[key])
        return value

    def contains(self, key):
        comparator_bucket = self.hash(key)
        bucket = (self.buckets[comparator_bucket])
        if bucket != None and bucket.includes(key) :
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
        result = primed % len(self.buckets)
        return result


ht = HashTable()

assert ht
assert ht.buckets
assert ht.hash('cat') == ht.hash('act')
assert ht.hash("car") != ht.hash('cat')

cat_hash = ht.hash("cat")
ht.add('cat', 'Cleo')
assert ht.buckets(cat_hash).head.value == ('cat','Cleo')

print("tests pass")
