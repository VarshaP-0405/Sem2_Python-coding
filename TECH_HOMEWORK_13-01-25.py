def canCompleteCircuit(gas, cost):
    total_gas = 0
    total_cost = 0
    current_gas = 0
    start_index = 0
    for i in range(len(gas)):
        total_gas += gas[i]
        total_cost += cost[i]
        current_gas += gas[i] - cost[i]
    if current_gas < 0:
            start_index = i + 1  
            current_gas = 0  
    if total_gas < total_cost:
        return -1
    return start_index
gas = list(map(int, input("Enter numbers separated by spaces for gas values:").split()))
cost = list(map(int, input("Enter numbers separated by spaces for cost values:").split()))
print(canCompleteCircuit(gas, cost))
##2##
ratings = [1, 0, 2]
n = len(ratings)

if n == 0:
    print(0)
else:
    candies = [1] * n
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
    total_candies = sum(candies)
    print(total_candies)
