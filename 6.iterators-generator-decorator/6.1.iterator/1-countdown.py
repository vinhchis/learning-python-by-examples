class CountdownIterator:
    def __init__(self, start):
        self.start = start

    # The __iter__() method initializes the iterator and returns itself
    def __iter__(self):
        return self

    # the __next__() method retrieves the next value in the sequence and advances the iterator.
    def __next__(self):
        if self.start < 0:
            raise StopIteration
        else:
            # update state
            self.start -= 1
            # return  the next element
            return self.start + 1


# Using the iterator
countdown = CountdownIterator(5)
for number in countdown:
    print(number)
# Output: 5 4 3 2 1 0
print(countdown.start)
# -1 


#  __iter__() run when:
# 1. for start.
# 2. iter() function.