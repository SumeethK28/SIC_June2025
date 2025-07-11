# def getMinimumCost(k, c):
#     c.sort(reverse = True)
#     sum = 0
#     for idx, price in enumerate(c):
#         sum += price * (1 + idx // k)
#     return sum

def getMinimumCost(k, c):
    flowers = len(c)
    c.sort()
    price = 0
    for multiplier in range(1, flowers // k + 1):
        for _ in range(k):
            price += multiplier * c.pop()
    price += sum(c) * (flowers // k + 1)
    return price

k = 2
c = [2,5,6]
minimum_cost = getMinimumCost(k, c)

print(minimum_cost)