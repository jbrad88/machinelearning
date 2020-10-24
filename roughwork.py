def BabylonianAlgorithm(number):
    if(number == 0):
        return 0

    g = number/2.0
    g2 = g + 1
    while(g != g2):
        n = number/ g
        g2 = g
        g = (g + n)/2

    return g
print('The Square root of 2 =', BabylonianAlgorithm(2))


#References
# 1. https://www.w3resource.com/python-exercises/math/python-math-exercise-18.php

x = 2 * 10 ** 200

r = x

def test_diffs(x, r):
    d0 = abs(x - r**2)
    dm = abs(x - (r-1)**2)
    dp = abs(x - (r+1)**2)
    minimised = d0 <= dm and d0 <= dp
    below_min = dp < dm
    return minimised, below_min

while True:
    oldr = r
    r = (r + x // r) // 2

    minimised, below_min = test_diffs(x, r)
    if minimised:
        break

    if r == oldr:
        if below_min:
            r += 1
        else:
            r -= 1
        minimised, _ = test_diffs(x, r)
        if minimised:
            break

print(f'{r // 10**100}.{r % 10**100:0100d}')