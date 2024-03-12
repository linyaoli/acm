class SimpleRedisCache:
    def __init__(self):
        self.cache = {}
        self.transactions = []
        self.in_transaction = False

    def set(self, key, value):
        if self.in_transaction:
            # Save the current state for rollback if not already saved.
            if key not in self.transactions[-1]:
                self.transactions[-1][key] = self.cache.get(key)
            self.cache[key] = value
        else:
            self.cache[key] = value

    def get(self, key):
        return self.cache.get(key, None)

    def delete(self, key):
        if self.in_transaction:
            # Save the current state for rollback if not already saved.
            if key not in self.transactions[-1]:
                self.transactions[-1][key] = self.cache.get(key)
            self.cache.pop(key, None)
        else:
            self.cache.pop(key, None)

    def multi(self):
        self.in_transaction = True
        self.transactions.append({})  # Start a new transaction with an empty state.

    def exec(self):
        if self.in_transaction:
            self.transactions.pop()  # Discard the saved state since we're committing.
            if not self.transactions:
                self.in_transaction = False  # No open transactions left

    def discard(self):
        if self.in_transaction:
            # Restore the original state from the last transaction.
            last_transaction = self.transactions.pop()
            for key in last_transaction:
                if last_transaction[key] is None:
                    self.cache.pop(key, None)
                else:
                    self.cache[key] = last_transaction[key]
            if not self.transactions:
                self.in_transaction = False  # No open transactions left

# Example Usage
cache = SimpleRedisCache()
cache.set('key1', 'value1')
print(cache.get('key1')) # value1

cache.multi()  # Start transaction
cache.set('key1', 'updated_value')
print(cache.get('key1'))  # Output: updated_value
cache.discard()  # Rollback transaction
print(cache.get('key1'))  # Output: value1 - reverted to original value after rollback

cache.multi()  # Start another transaction
cache.set('key1', 'another_value')
print(cache.get('key1'))  # Output: another_value
cache.exec()  # Commit transaction
print(cache.get('key1'))  # Output: another_value - remains after commit
