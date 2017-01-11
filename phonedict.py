class PhoneDict(dict):
    def __missing__(self, key):
        self.setdefault(key, 0)
        return self[key]

    def increment(self, key):
        self[key] = self[key] + 1
