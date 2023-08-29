from collections import deque

def findPermutations(nums):
    # I'm using this to practice a leetcode problem. It's a subset problem.
    result = []
    # Create a queue to get the largest size subset. Insert an empty list to start the algorithm.
    permutations = deque()
    permutations.append([])
    for current in nums:
        n = len(permutations)
        for _ in range(n):
            # Usual subset pattern solution
            currentPerm = permutations.popleft()
            lengthPerm = len(currentPerm)
            for j in range(lengthPerm+1):
                temp = list(currentPerm)
                temp.insert(j, current)
                if len(temp) == len(nums):
                    result.append(temp)
                else:
                    permutations.append(temp)
    return result

# I hope I helped someone stuck on this problem. :]
print(findPermutations([5, 4, 2, 1]))

# GOOD LUCK ON APPLICATIONS TO INTERNSHIPS!!!
