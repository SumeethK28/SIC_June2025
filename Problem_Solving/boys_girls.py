def is_valid(first, second):
    arrangement = []
    for i in range(len(first)):
        arrangement.append(first[i])
        arrangement.append(second[i])
    return arrangement == sorted(arrangement)

def can_arrange(boys, girls):
    boys.sort()
    girls.sort()
    
    return is_valid(boys, girls) or is_valid(girls, boys)


test_case = int(input("Enter number of test cases: "))

for _ in range(test_case):
    total_number = int(input("Enter number of boys and girls: "))
    boys = list(map(int, input().split()))
    girls = list(map(int, input().split()))

    if can_arrange(boys, girls):
        print("Yes")
    else:
        print("No")