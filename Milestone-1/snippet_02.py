class Counter:
    def __init__(self):
        self.value = 0

    def inc(self):
        self.value += 1

    def get(self):
        return self.value

if __name__ == "__main__":
    c = Counter()
    c.inc()
    print("Snippet 02 Output:", c.get())
