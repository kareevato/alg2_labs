def ceil(x, y):
    return (x + y - 1) // y

def minEatingSpeed(piles, H):
    if not (1 <= len(piles) <= 10**4):
        raise ValueError("Кількість куп має бути від 1 до 10^4")
    if not (len(piles) <= H <= 10**9):
        raise ValueError("H має бути не менше кількості куп і не більше 10^9")
    if not all(1 < pile <= 10**19 for pile in piles):
        raise ValueError("Кожна купа повинна містити від 2 до 10^19 бананів")

    def canFinish(K):
        total_hours = 0
        for pile in piles:
            total_hours += ceil(pile, K)
            if total_hours > H:
                return False  
        return True

    left, right = 1, max(piles)

    if not canFinish(right):
        return -1  

    while left < right:
        mid = (left + right) // 2
        if canFinish(mid):
            right = mid
        else:
            left = mid + 1 
    return left 
print(minEatingSpeed([3,6,7,11], 8))  # Очікується: 4
print(minEatingSpeed([30,11,23,4,20], 5))  # Очікується: 30
print(minEatingSpeed([30,11,23,4,20], 6))  # Очікується: 23
