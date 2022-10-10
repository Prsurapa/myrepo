def avg_of_three(p, q, r):
    a = p + q + r
    avg = a / 3
    print("avg of three elements:", avg)
    return round(avg,3)
x = avg_of_three(2, 2, 6)
if x == 3.333:
    print("test passed")
else:
    print("test failed")
x = avg_of_three(5, 5, 5)
if  x == 5:
    print("test1 passed")
else:
    print("test1 failed")