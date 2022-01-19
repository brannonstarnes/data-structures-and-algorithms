from linked_list.linked_list import LinkedList

class HashTable():
    def __init__(self, size=1024):
        self.buckets = [None] * size

    def add(self, key, value):
        hash = self.hash(key)
        bucket = self.buckets[hash]

        if bucket == None:
            bucket = LinkedList()
            self.buckets[hash] = bucket
        bucket.append((key,value))


    def get(self, key):
        hash = self.hash(key)
        bucket = ((self.buckets[hash])[key])

        if bucket:
            node = bucket.head
            while node:
                node_key, node_value = node.value
                if node_key == key:
                    return node_value
                node = node.next

        return None

    def contains(self, key):
        comparator_bucket = self.hash(key)

        bucket = (self.buckets[comparator_bucket])

        if bucket:
            node = bucket.head
            while node:
                node_key = node.value[0]
                if node_key == key:
                    return True
                node = node.next

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


# ht = HashTable()

# assert ht
# assert ht.buckets
# assert ht.hash('cat') == ht.hash('act')
# assert ht.hash("car") != ht.hash('cat')

# cat_hash = ht.hash("cat")
# ht.add('cat', 'Cleo')
# assert ht.buckets(cat_hash).head.value == ('cat','Cleo')

# print("tests pass")
