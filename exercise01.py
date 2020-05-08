L = [x*x for x in range(5)]
g = (x*x for x in range(5))
print(L)
for i in range(5):
    print(next(g))
