from snippet_01 import add
from snippet_02 import Counter

print("Running Milestone-1 Snippets...\n")

# Test snippet_01
print("add(5, 7) =", add(5, 7))

# Test snippet_02
c = Counter()
c.inc()
c.inc()
print("Counter value after 2 increments =", c.get())
