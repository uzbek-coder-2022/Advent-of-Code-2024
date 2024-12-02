# --- Part Two ---

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
        nums1 = nums[:]
        flag = False
        for i in range(len(nums)):
            nums1.pop(i)
            flag = flag or isSorted(nums1) or isSorted(nums1, reverse=True)
            nums1 = nums[:]
        ans += flag
        
    return ans

        
if __name__ == "__main__":
    print(solve())