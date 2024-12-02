# --- Day 2: Red-Nosed Reports ---

def isSorted(nums: list, reverse: bool = False) -> bool:   
    if reverse:
        return all(nums[i] < nums[i - 1] and 0 < nums[i - 1] - nums[i] < 4 for i in range(1, len(nums))) 
    return all(nums[i] > nums[i - 1] and 0 < nums[i] - nums[i - 1] < 4 for i in range(1, len(nums))) 
            

def solve() -> int:
    file = open('Advent-of-Code-2024/Day2/Day2.in', 'r')
    inputData = file.readlines()
    
    nums = []
    ans = 0
    
    for line in inputData:
        nums = list(map(int, line.strip().split()))
        ans += isSorted(nums) or isSorted(nums, reverse=True)
        # print(ans)
        
    return ans

        
if __name__ == "__main__":
    print(solve())
    # print(isSorted([9, 7, 4, 4, 1]))  # False
    # isSorted([3, 2, 1])        # True
    # isSorted([1, 2, 3, 4, 5])  # True
    # isSorted([1, 2, 3, 5, 4])  # False