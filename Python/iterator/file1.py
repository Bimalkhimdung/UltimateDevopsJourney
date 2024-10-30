class Person:
    def __iter__(self):
      self.a = 1
      return self
    def __next__(self):
       x = self.a 
       self.a += 1
       return x
p_ = Person()
it_ = iter(p_)

for x in it_:
   print(x)
