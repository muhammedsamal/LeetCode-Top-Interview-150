class RandomizedSet:

    def __init__(self):
      self.rand = set()
        

    def insert(self, val: int) -> bool:
      if val in self.rand:
        return False
      self.rand.add(val)
      return True

    def remove(self, val: int) -> bool:
      if not val in self.rand:
        return False
      self.rand.remove(val)
      return True

    def getRandom(self) -> int:
      return random.choice(tuple(self.rand))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()