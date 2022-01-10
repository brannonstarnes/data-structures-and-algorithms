

class HashTable():
    def __init__(self, size=1024):
        self.buckets = [None] * size

    def add(self, key, value):
        bucket_location = self.hash(key)
        self.buckets[bucket_location] = {key: value}


    def get(self, key):
        bucket_location = self.hash(key)
        value = ((self.buckets[bucket_location])[key])
        return value

    def contains(self, key):
        pass

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

my_hash = HashTable()
my_hash.hash('spam')
my_hash.add('spam', 'eggs')
my_hash.get('spam')

