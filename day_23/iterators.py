a = ["hey", "bro", "you're", "awesome"]
itr = iter(a)

print(next(itr))
print(next(itr))


# tv remote that goes through channels one at a time
class RemoteControl:
    def __init__(self):
        self.channels = ["HBO", "CNN", "ABC", "ESPN"]
        self.index = -1

    def __iter__(self):
        return self

    # goes to next channel, stops when there are no more
    def __next__(self):
        self.index += 1
        if self.index >= len(self.channels):
            raise StopIteration
        return self.channels[self.index]


r = RemoteControl()
for channel in r:
    print("Channel:", channel)
