import hashlib
import bisect

class ConsistentHashRouter:
    def __init__(self, nodes=None, replicas=3):
        self.replicas = replicas
        self.ring = dict()
        self.sorted_keys = []
        
        if nodes:
            for node in nodes:
                self.add_node(node)

    def _hash(self, key):
        """Returns the hash of a key."""
        return int(hashlib.md5(key.encode('utf-8')).hexdigest(), 16)

    def add_node(self, node):
        """Adds a node to the ring."""
        for i in range(self.replicas):
            key = self._hash(f"{node}:{i}")
            self.ring[key] = node
            bisect.insort(self.sorted_keys, key)

    def remove_node(self, node):
        """Removes a node from the ring."""
        for i in range(self.replicas):
            key = self._hash(f"{node}:{i}")
            if key in self.ring:
                del self.ring[key]
                self.sorted_keys.remove(key)

    def get_node(self, key):
        """Returns the node responsible for the given key."""
        if not self.ring:
            return None
        
        hash_val = self._hash(key)
        start = bisect.bisect(self.sorted_keys, hash_val)
        
        if start == len(self.sorted_keys):
            start = 0
            
        return self.ring[self.sorted_keys[start]]
