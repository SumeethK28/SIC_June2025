coins_in_harry_bag = int(input("Enter the number of coins to be there in Harry's Bag: "))

harry_bag = []
print("Enter the worth of each Gold coin: ")
for _ in range(coins_in_harry_bag):
    harry_bag.append(int(input()))

q_instructions, capacity_monk_bag = map(int, input("Enter the number of instructions you want to perform and the capacoty of Monk's Bag: ").split())

monk_bag = []

result = -1

print("Enter your instructions (Harry or Remove)")
for _ in range(q_instructions):
    instruction = input()

    if instruction == "Harry":
        value = harry_bag.pop(0)
        monk_bag.append(value)
    elif instruction == "Remove":
        monk_bag.pop()

    if sum(monk_bag) == capacity_monk_bag:
        result = len(monk_bag)

print(result)