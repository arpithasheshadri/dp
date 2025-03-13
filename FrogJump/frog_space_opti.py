def frog_jump(n,cost):
    if n == 0:
        return 0
    
    prev1 = 0
    prev2 = 0

    for i in range(1,n+1):
        left = prev1 + abs(cost[i] + cost[i-1])
        right = float('inf')
        if i > 1:
            right = prev2 + abs(cost[i] - cost[i-2])
        prev2 = prev1
        prev1 = min(left,right)

    return prev1


cost = [10,20,30,10,50]
n = len(cost) - 1
print(frog_jump(n,cost))